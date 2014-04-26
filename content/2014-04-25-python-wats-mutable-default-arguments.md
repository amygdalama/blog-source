Title: Python Wats: Mutable Default Arguments
Date: 2014-04-25
Category: Python
Tags: python, python internals
Slug: python-wats-mutable-default-arguments
Author: Amy Hanlon
Status: draft

Let's look at a common Python wat and try to figure out wat's actually happening!  

We'll define a function, `foo`, which takes one argument, `l`, which has the default value of an empty list.

    >>> def foo(l=[]):
    ...     l.append('cat')
    ...     return l

What happens when we call `foo` multiple times?

    >>> foo()
    ['cat']
    >>> foo()
    ['cat', 'cat']

Whoa! So mutating `l` actually mutates it for all future calls to the function. Weird.

This means that the `[]` object is *only created once*, and each time we call `foo` without a argument, `l` is referring to that same object. This may lead you to form a hypothesis: `l=[]` is kind of like a name-binding statement that executes only once, when the function is defined. 

But, if that hypothesis is true, then how should we expect the following function to behave?

    >>> def bar(l=[]):
    ...     print locals()
    ...     l = ['cat']
    ...     return l
    ... 
    >>> bar()
    # ?
    >>> bar()
    # ?

Well, if `l=[]` is *like a name-binding statement that executes only once* when the function is defined, then I would expect something like this sequence of events to happen, when we define `bar` and then call it twice:

1. `bar` is defined
    * the name `l` is bound to the object `[]`
    * none of the code inside `bar` executes yet
2. `bar` is called the first time:
    * `locals()` should return `{l : []}`
    * then we reassign `l` to `['cat']` within the scope of `bar`
    * `bar` should return `['cat']`
3. `bar` is called again:
    * `l=[]` is not executed (based on our assumption)
    * `locals()` should either return `{}` or `{l : ['cat']}`, depending on if the assignment of `l = ['cat']` persists after the function is called the first time
    * `bar` should return `['cat']`

What actually happens?

    >>> bar()
    {'l': []}
    ['cat']
    >>> bar()
    {'l': []}
    ['cat']

Hrm. This behavior reasonably leads us to believe that the assignment `l=[]` happens *each time we call the function `bar`*. But we showed that was not the case in `foo`: `l=[]` can't be a statement that executes each time the function is called, or else we'd create a new `[]` each time. 

If we assume `l=[]` executes like a name-binding statement, then it must execute either (1) only once when the function is defined, or (2) each time the function is called. In `foo`, it only executes once, but in `bar`, it executes every time we call `bar`. That just can't be. So our assumption that `l=[]` executes like a name-binding statement leads to a contradiction, and thus must be wrong! Guess what, nerds! We kind of just did a [proof by contradiction](http://en.wikipedia.org/wiki/Proof_by_contradiction)!

So then what happens when we define default values for arguments? Does the assignment (the `l=` part) happen each time, but the creation of the object on the right side of the `=` only happen once? Or is there some sort of intermediary namespace that contains the default values of arguments? Maybe! 

Let's see if we can figure out where the default values are stored.

My usual go-to for questions like this is Python internals whiz and Hacker School Facilitator [Allison Kaptur](), but you can also find the answer with a bit of googling. I learned that what actually happens when we define a default argument, is that the value of the argument gets stored inside the function's `func_defaults` method. Let's look back at the `foo` function:

    >>> def foo(l=[]):
    ...     l.append('cat')
    ...     return l

We can access `foo`'s `func_defaults` like so:

    >>> foo.func_defaults
    ([],)
    >>> foo()
    ['cat']
    >>> foo.func_defaults
    (['cat'],)

Oh! So the actual object that is being stored as the default for `foo` is being modified when we call `foo`! For fun, let's see if we can mutate the default value from outside of the function:

    >>> foo.func_defaults[0].append('dragon')
    >>> foo.func_defaults
    (['cat', 'dragon'],)
    >>> foo()
    ['cat', 'dragon', 'cat']

Eep! That was fun. So what's in the `func_defaults` of `bar`? Recall:

    >>> def bar(l=[]):
    ...     print locals()
    ...     l = ['cat']
    ...     return l

And then:

    >>> bar.func_defaults
    ([],)
    >>> bar()
    {'l': []}
    ['cat']
    >>> bar.func_defaults 
    ([],)

Okay! So since `bar` *reassigns* `l` to `['cat']`, it doesn't modify the object stored in `func_defaults`.

So what have we learned?

It appears as if the following happens when we define and call `bar`:

1. `bar` is defined
    * the object `[]` is created and stored in the `func_defaults` tuple
2. `bar` is called the first time:
    * since we didn't pass in a value for `l` as a argument, Python looks in the `func_defaults` for the value to bind to the name `l`, and grabs the `[]` object that we created when we defined `bar`
    * we reassign `l` to `['cat']` within the scope of `bar`. Since this is a reassignment, this doesn't modify the `[]` object contained in `func_defaults`. Instead, `l` is just bound to a different object in memory.
3. `bar` is called again:
    * since we didn't modify the `[]` object the first time we called `l`, the same series of events happens as in step 2!

I should probably mention something useful: a common way of setting a default value to an empty list (and having it actually work as expected) is to do the following:

    def baz(l=None):
        if not l:
            l = []
        l.append('cat')
        return l

When we call `baz` multiple times, its behavior is more expected:

    >>> baz()
    ['cat']
    >>> baz()
    ['cat']



## A Mental Model

l=[] is like a line of python code in the body of the function that happens before the rest of the function gets executed.

We'll try to figure out if it executes only once, or if it executes every time the function is called.