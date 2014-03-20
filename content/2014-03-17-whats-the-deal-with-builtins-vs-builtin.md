Title: What's the deal with __builtins__ vs __builtin__
Date: 2014-03-19
Category: Projects
Tags: harry potter, nagini, python
Slug: whats-the-deal-with-builtins-vs-builtin
Author: Amy Hanlon
Status: draft

Seriously, what's the difference? When you first fire up the Python interpreter, `__builtins__` is in your namespace for free:

    :::python
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

What. What does that mean. Let's see what happens when we `import` a script that uses `__builtins__`.

We'll start with a script, `a.py`, see if 



1. Maybe I should use __builtin__ instead of __builtins__
2. What is the difference?
3. It appears one is sometimes a dict? How does that work?
4. Test:

a.py:

    :::python
    import __builtin__

    print "Before importing b"
    print __builtin__ is __builtins__

    import b

    print "In a, after importing b"
    print __builtin__ is __builtins__

b.py:

    :::python
    import __builtin__

    print "In b"
    print __builtin__ is __builtins__

When running a.py, we get:

When running b.py we get:

5. Okay. One related thing I'm confused about:

    :::python
    import sys
    sys.__builtins__
    exists as a thing

    :::python
    del __builtin__.float
    import numpy

float error
but doesn't numpy have its own builtins?

but doesn't numpy import float on its own? so it should be fine?

it actually imports float *from* __builtin__, and __builtin__ already exists in main! So in order to not duplicate work, python will check to see if __builtin__ exists in sys.modules() and if it does, it will use that __builtin__. 