Title: After Six Months of Learning The Python, I Can Finally Print "Hello World!"
Date: 2014-04-01
Category: Projects
Tags: python, python internals, hello world, hacker school
Slug: after-six-months-of-learning-the-python-i-can-finally-print-hello-world
Author: Amy Hanlon

I've been trying to learn how to write a function in the Python that prints two words, only two, "Hello World." I've been trying for six months. And today, friends, I've done it.

I've read so many places that you can make print statements in the Python like so:

    :::python
    print "Hello World!"

But where do you type this in? How do you tell the computer, the Python, the whatever, that you want it to take this sequence of characters, interpret it as code, and execute it?

Well, I hope you are sitting down, because I've found the answer: the [`exec`](https://docs.python.org/2/reference/simple_stmts.html#the-exec-statement) statement (or function if you're into the Python 3)! 

Let's say you want the Python to execute the definition of a function like:

    :::python
    def foo():
        print "Hello World!"

You can accomplish this by firing up the Python interpreter and typing:

    :::pycon
    >>> exec("def foo():\n    print 'Hello World!'\n")

[`exec`](https://docs.python.org/2/reference/simple_stmts.html#the-exec-statement) here takes in a string of the Python code and executes it! The `\n` and the whitespace between the `\n` and the `print` statement are very important! The Python needs those to understand where the function ends.

So now, we can see that `foo` exists and is a function that prints "Hello World!"

    :::pycon
    >>> foo
    <function foo at 0x10b611230>
    >>> foo()
    Hello World!

`exec` can also take in `code` objects. We can make a `code` object by using the [`compile`](https://docs.python.org/2/library/functions.html#compile) function:
    
    :::pycon
    >>> c = compile("def bar():\n    print 'Hello World!'\n", '', 'exec')
    >>> c
    <code object <module> at 0x10b5f88b0, file "", line 1>

`compile` takes in a string of code, a filename (we can just pass it the empty string), and a mode, which can be 'exec', 'eval', or 'single'.

Let's pass `c` into `exec` to execute the code and define our `bar` function:

    :::pycon
    >>> exec(c) 
    >>> bar()
    Hello World!    

Yes! We did it again! This is a victorious day. 

Interestingly enough, functions themselves have `code` objects assigned to them as attributes:

    :::pycon
    >>> bar.__code__
    <code object bar at 0x10b5f81b0, file "", line 1>

And we can overwrite these `code` objects with our own `code` objects! 

    :::pycon
    >>> new_code = compile("print 'Hello, We Are Victorious Beings!'\n", '', 'exec')
    >>> new_code
    <code object <module> at 0x10b5f81b0, file "", line 1>
    >>> bar.__code__ = new_code
    >>> bar.__code__
    <code object <module> at 0x10b5f81b0, file "", line 1>
    >>> bar()
    Hello, We Are Victorious Beings!

Neat! We don't need the `"def bar():"` part in the string we pass to `compile` because at this point, `bar` already exists and we're just overwriting the code in the body of the `bar` function.

Share in the comments if you know of any other ways to print statements in the Python!