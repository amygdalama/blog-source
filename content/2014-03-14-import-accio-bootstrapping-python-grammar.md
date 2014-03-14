Title: Replacing `import` with `accio`: A Dive into Bootstrapping and Python's Grammar
Date: 2014-03-14
Category: Projects
Tags: python, harry potter, bootstrapping, cpython, compilers, grammar
Slug: import-accio-bootstrapping-python-grammar
Author: Amy Hanlon
Status: draft

At Hacker School, I've been building an alternate universe Harry Potter-themed Python by overwriting Python builtin functions and statements with Harry Potter spells. This is a thing you can do at Hacker School!

Although this project started as a joke, I've quickly descended into Python internals so far that I've, with the guidance of the fabulous Hacker School facilitator Allison Kaptur, made edits to the CPython source code, and compiled a Python to compile a Python. All to replace the `import` statement with `accio`.

But before we get into compiling the Harry Potter Python I lovingly call Nagini, let's first talk about some Python internal basics, with spells as examples, of course.

#Builtin Functions vs Statements

Overwriting builtin *functions* in Python is surprisingly trivial:  

    :::python
    >>> wingardium_leviosa = __builtins__.float

    >>> del __builtins__.float

    >>> float(3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'float' is not defined

    >>> wingardium_leviosa(3)
    3.0

However, overwriting `import` is not so easy. Let's try:

    :::python
    >>> accio = import
      File "<stdin>", line 1
        accio = import
                     ^
    SyntaxError: invalid syntax

Looks like Python is expecting the name of something to import after `import`, so this doesn't work. This is an effect of import being a *statement* which invokes a function `__builtins__.__import__` rather than just a function. Maybe we can overwrite the function instead:

    :::python
    >>> accio = __builtins__.__import__
    
    # No errors! Let's see if we can accio sys:

    >>> accio sys
      File "<stdin>", line 1
        accio sys
                ^
    SyntaxError: invalid syntax

    # :(
    # What if we tried calling it like a function?

    >>> accio(sys)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'sys' is not defined 
    
    # Maybe we need to pass 'sys' as a string?

    >>> accio('sys')
    <module 'sys' (built-in)>

    # Ooh!

    >>> sys = accio('sys')
    >>> sys
    <module 'sys' (built-in)>

So we have a way to add `accio`, but it's ugly and doesn't work exactly like `import` so I'm unsatisfied. Can we delete import?

    :::python
    >>> del import
      File "<stdin>", line 1
        del import
                 ^
    SyntaxError: invalid syntax

    >>> del __builtins__.__import__
    >>> import os
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ImportError: __import__ not found

Kind of! Although I want `import os` to be a SyntaxError rather than an ImportError because clearly `import` is the wrong thing to type and the user should know to type `accio` instead.

To edit what Python interprets as a *statement*, we'll need to clone CPython and mess with the source code! Sweet!

#CPython

#Yo Dawg, I Heard You Like Pythons
