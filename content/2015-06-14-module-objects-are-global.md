Title: Module objects are global!
Date: 2015-06-14
Category: Projects
Tags: python, import, debugging
Slug: module-objects-are-global
Author: Amy Hanlon

One of my favorite kinds of bugs is when a test that seems entirely unrelated to a code change fails. I've trained myself to look for the common causes, usually having to deal with shared state due to a test missing a proper teardown. But this week, I had a new kind of failure, one to do with module objects and how Python's import mechanism works, which, if you didn't know, is also [one of my favorite things](http://mathamy.com/import-accio-bootstrapping-python-grammar.html).

I've been experimenting with [faker](https://github.com/joke2k/faker), a package for generating random phone numbers, email addresses, etc, for use in tests. My goal was to have a wide surface area of phone numbers used across tests, but also for each test to use the same phone number(s) every test run.

Using `faker` is pretty simple:

    :::pycon
    >>> from faker import Faker
    >>> fake = Faker()

    >>> fake.seed(0)
    >>> fake.phone_number()
    u'742-547-3459x52762'

    >>> fake.seed(0)
    >>> fake.phone_number()
    u'742-547-3459x52762'

Here, I'm seeding the `Faker` instance so we get the same phone number for each call. Having to do this in the setup for every test, though, seemed like a lot of tedious work, and probably easy to forget, so I wanted to see if I could build a nose plugin that would seed a `Faker` instance for me based on the hash of the test name.

This worked great... until I ran our entire test suite, and a test that _didn't_ use `faker` mysteriously started failing due to an invalid phone number.

However, after a bit of digging, I found that the failing test _did_ use the `random` module, generating a phone number like this:

    :::python
    >>> phone_number_digits = [random.randint(2, 9) for _ in xrange(10)]
    [8, 8, 5, 4, 6, 5, 8, 4, 5, 6]

I immediately recognize that this has some possibility to generate an invalid phone number (`999` isn't a valid area code). I try running the test suite again, assuming that there's a small chance that this test will fail, and maybe I just got unlucky. Nope, it failed a second time. No matter how many times I run the test suite, this test fails.

Hrm.

Does seeding `faker` also seed `random`? Let's test this out in our REPL:

    :::pycon
    >>> fake.seed(0)
    >>> random.randint(0, 100)
    85
    >>> fake.seed(0)
    >>> random.randint(0, 100)
    85
    >>> fake.seed(0)
    >>> random.randint(0, 100)
    85

Aha! So `faker` seeds `random`. But how does that work? Time to look at the source for `faker` to see how `seed` works. [Here's](https://github.com/joke2k/faker/blob/e036b29268d346000453211d6f3153e99bdc2fe6/faker/generator.py#L52) the relevant code:

    :::python
    def seed(self, seed=None):
        """Calls random.seed"""
        random.seed(seed)

Here's a summary of what we know so far:

1. module `a` imports module `b`
2. module `b` seeds `random`
3. as a result, `random` is _also_ seeded in module `a`

This must mean that the `random` imported in `a` is the _same_ module object as the `random` imported in `b`. So if this is the case, we can do things like add attributes to `random` in one module, and access them in another module. Let's try!

    :::python
    # a.py:
    import random

    random.defined_in_a = "hi!"


    # b.py:
    import random

    print(random.defined_in_a)

When we try running `b.py`, do we get a `NameError`? Or does this resolve and print `"hi!"`? Let's see:

    :::console
    $ python b.py
    hi!

Neat. So module objects are global. For more on how this works, this documentation might be helpful:

* [the import system](https://docs.python.org/3/reference/import.html#the-import-system)
* [sys. modules](https://docs.python.org/3.4/library/sys.html#sys.modules)

If you're thinking that it's probably bad that seeding `faker` has side-effects outside of `faker`, you're right! [Here's](https://github.com/joke2k/faker/issues/14) a ticket explaining why this is a problem and some possible solutions.
