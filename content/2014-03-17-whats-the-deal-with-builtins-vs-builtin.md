Title: What's the deal with __builtins__ vs __builtin__
Date: 2014-03-23
Category: Projects
Tags: python, builtins
Slug: whats-the-deal-with-builtins-vs-builtin
Author: Amy Hanlon

Seriously, what's the difference? When you first fire up the Python interpreter, `__builtins__` is in your namespace for free:

    :::pycon
    >>> globals().keys()
    ['__builtins__', '__name__', '__doc__', '__package__']
    >>> __builtins__
    <module '__builtin__' (built-in)>
    >>> sys.modules['__builtin__']
    <module '__builtin__' (built-in)>

But it appears to be the `__builtin__` module! If you:

    :::python
    >>> import __builtin__
    >>> __builtin__ is __builtins__
    True

Hrm. So they are both names that point to the same object, the module `__builtin__`. Weird. Why does Python do this? Do they always behave the same?

I read on [StackOverflow](http://stackoverflow.com/questions/11181519/python-whats-the-difference-between-builtin-and-builtins) that

> By default, when in the `__main__` module, `__builtins__` is the built-in module `__builtin__` (note: no 's'); when in any other module, `__builtins__` is an alias for the dictionary of the `__builtin__` module itself.

What. What does that mean. 

This talk of the "`__main__` module" and "any other module" reminds me of a sequence of words that I've known for quite a while, but haven't completely grokked:

> We can access the name of the current module with the builtin variable `__name__`. 

You're probably familiar with the related canonical statement:

    :::python
    if __name__ == '__main__':
        main()

But what does "current module" mean? What does the `__name__` variable look like when it does not equal `__main__`?

I happen to know, because I've obsessively read about the `import` statement, another sequence of words: 

> Any code executed as a result of an `import` isn't executed in the `__main__` module. 

Let's use these bits of knowledge to observe the behavior of `__builtins__` both inside and outside of the `__main__` module. We can also check out the `__name__` variable while we're at it.

First, let's make a script, `a.py`, which will allow us to observe the behavior of `__builtin__`, `__builtins__`, and `__name__`.

    :::python
    import __builtin__

    print "In a"
    print "__name__ is:", __name__
    print "__builtin__ is __builtins__:", __builtin__ is __builtins__
    print "type(__builtin__):", type(__builtin__)
    print "type(__builtins__):", type(__builtins__)

Let's see what happens when we execute `a.py`:
    
    :::console
    $ python a.py
    In a
    __name__ is  __main__
    __builtin__ is __builtins__ True
    type(__builtin__) <type 'module'>
    type(__builtins__) <type 'module'>

Okay. So we're in the `__main__` module, and in here `__builtin__` is pointing to the same module object as `__builtins__`. 

What happens if we `import a` in another script? The code in `a` will execute, but it won't be executed within the `__main__` module. Instead, it'll be executed within the `a` module. Let's write another script, `b.py`, to find out what happens to `__builtins__` outside of `__main__`:

    :::python
    import __builtin__

    print "In b, before importing a"

    # the output from this should be the same as when we ran
    # $ python a.py
    print "__name__ is:", __name__
    print "__builtin__ is __builtins__:", __builtin__ is __builtins__
    print "type(__builtin__):", type(__builtin__)
    print "type(__builtins__):", type(__builtins__)
    print "\n"

    import a
    # code from a will execute here

Let's see what happens when we run `b.py`:

    :::console
    $ python b.py
    In b, before importing a
    __name__ is: __main__
    __builtin__ is __builtins__: True
    type(__builtin__): <type 'module'>
    type(__builtins__): <type 'module'>


    In a
    __name__ is: a
    __builtin__ is __builtins__: False
    type(__builtin__): <type 'module'>
    type(__builtins__): <type 'dict'>

Aha. So when we're outside the context of the `__main__` module, `__name__` is just equal to the name of the module where code is currently being executed. That seems logical. And outside of `__main__`, `__builtins__` is a dict, rather than a module. 

We were told earlier that, outside the context of `__main__`, *"`__builtins__` is an alias for the dictionary of the `__builtin__` module"*. I think that means that `__builtins__ is __builtin__.__dict__`. Let's see if my hypothesis is true, by adding another line to the bottom of our `a.py` file:
    
    :::python
    print "__builtins__ is __builtin__.__dict__", __builtins__ is __builtin__.__dict__

Running `b.py` again, we get:

    :::console
    $ python b.py
    In b, before importing a
    __name__ is: __main__
    __builtin__ is __builtins__: True
    type(__builtin__): <type 'module'>
    type(__builtins__): <type 'module'>


    In a
    __name__ is: a
    __builtin__ is __builtins__: False
    type(__builtin__): <type 'module'>
    type(__builtins__): <type 'dict'>
    __builtins__ is __builtin__.__dict__ True

Yes! My hypothesis was correct. Okay. So now I get why using `__builtin__` is better than `__builtins__`: 

**The type, and thus behavior, of `__builtins__` changes based on the context of where it's being executed, while the type and behavior of `__builtin__` is constant. Rad.**

Thanks, stranger, for the learning opportunity. And thanks, always, to Allison Kaptur, for exploring this topic with me.

The code for this blog post is on [GitHub](https://github.com/amygdalama/builtins), of course.