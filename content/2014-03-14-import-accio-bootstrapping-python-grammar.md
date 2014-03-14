Title: Replacing `import` with `accio`: A Dive into Bootstrapping and Python's Grammar
Date: 2014-03-14
Category: Projects
Tags: python, harry potter, bootstrapping, cpython, compilers, grammar, hacker school
Slug: import-accio-bootstrapping-python-grammar
Author: Amy Hanlon

At [Hacker School](https://www.hackerschool.com/), I've been building an alternate universe Python by overwriting builtin functions and statements with Harry Potter spells. This is a thing you can do at Hacker School!

Although this project started as a joke, I've quickly descended so deeply into Python internals that I've, with the guidance of the fabulous Hacker School facilitator [Allison Kaptur](http://akaptur.github.io/), made edits to the CPython source code, and compiled a Python to compile a Python. All to replace the `import` statement with `accio`.

But before we get into compiling the Harry Potter Python I lovingly call Nagini, let's first talk about some Python internals basics, with spells as examples, of course.

#Overwriting Builtin Functions

Python builtin functions are stored in a module called `__builtins__` that's automatically imported on startup. 

    :::text
    >>> dir(__builtins__)
    ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']

Overwriting Python builtins is surprisingly easy! 

    :::text
    >>> wingardium_leviosa = __builtins__.float

    >>> del __builtins__.float

    >>> float(3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'float' is not defined

    >>> wingardium_leviosa(3)
    3.0

However, overwriting `import` is not so easy. Let's try:

    :::text
    >>> accio = import
      File "<stdin>", line 1
        accio = import
                     ^
    SyntaxError: invalid syntax

Python is expecting the name of a module after `import`, and thus it throws a `SyntaxError`. This is an effect of `import x` being a *statement*, rather than a *function*. 

Hm. I remember seeing the function `__import__` listed when we ran `dir(__builtins__)`. Maybe we can overwrite that instead:

    :::text
    >>> accio = __builtins__.__import__
    >>> accio sys
      File "<stdin>", line 1
        accio sys
                ^
    SyntaxError: invalid syntax

    # :(

What if we tried calling `accio` like a function?

    :::text
    >>> accio(sys)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'sys' is not defined 
    
Maybe we need to pass 'sys' as a string?

    :::text
    >>> accio('sys')
    <module 'sys' (built-in)>

    # Ooh!

    >>> sys = accio('sys')
    >>> sys
    <module 'sys' (built-in)>

Aha. So the statement `import x` probably does something like:  
    1. call the `__import__` function on `x`: `__builtins__.__import__('x')`  
    2. assign the name `x` to the module returned by `__import__`  

And `import sys` is like shorthand for the command:

    :::text
    >>> sys = __builtins__.__import('sys')

(Here I'm only describing simple `import` statements, but more complex statements like `from x import y.w, y.z` work similarly.)

So we have a way to add `accio` as a function, but not as a statement. I'm unsatisfied. 

For fun, can we delete import?

    :::text
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

Kind of! Although I want `import os` to be a `SyntaxError` rather than an `ImportError` because clearly `import` is the wrong thing to type and the user should know to type `accio` instead.

So, to completely overwrite `import` with `accio`, we'll need to learn where Python defines statements.

#Grammar

Eli Bendersky wrote a great [blog post](http://eli.thegreenplace.net/2010/06/30/python-internals-adding-a-new-statement-to-python/) about adding an `until` statement to Python. Since we want to *replace* a statement, rather than add one, our method will be a bit different.

Regardless, it looks like the place to start for changing Python's statements is in the `Grammar` file in the Python [source code](http://docs.python.org/devguide/setup.html). **Python source code!** Isn't this *fun?!* 

Python's source code is stored in a Mercurial repository, so first we'll have to install Mercurial.

    :::bash
    $ brew install mercurial

Then we can clone CPython (like `git clone`):

    :::bash
    $ hg clone http://hg.python.org/cpython

This will take a whole minute. Grab a coffee.

In the Python Mercurial repo, different versions of Python have different branches. By default we're on a Python3 branch. I'm still running Python2 on my machine, so let's checkout version 2.7:

    :::bash
    $ cd cpython
    $ hg checkout 2.7

Now let's [compile CPython](http://docs.python.org/devguide/setup.html) and see if it works!

    :::bash
    $ ./configure --with-pydebug
    $ make -s -j2

I get a warning message saying some modules were unable to be built, but I am unstoppable. We are unstoppable. Let's continue.

It seems like the place to start is in the file `Grammar/Grammar`, so let's start poking around there. [This](http://docs.python.org/2/reference/grammar.html) is what it looks like. Searching for 'import' brings us to lines 52-60:

    :::text     # figure out how to do line nos
    import_stmt: import_name | import_from
    import_name: 'import' dotted_as_names
    import_from: ('from' ('.'* dotted_name | '.'+)
                  'import' ('*' | '(' import_as_names ')' | import_as_names))
    import_as_name: NAME ['as' NAME]
    dotted_as_name: dotted_name ['as' NAME]
    import_as_names: import_as_name (',' import_as_name)* [',']
    dotted_as_names: dotted_as_name (',' dotted_as_name)*
    dotted_name: NAME ('.' NAME)*

Cool! We can kind of understand what's going on here just from reading. It looks like an `import_stmt` is either an `import_name` or an `import_from` which have the format `import x` and `from x import y`, respectively. What happens if we just change 'import' to 'accio' in lines 53 and 55? Let's try it. After making the change and saving the `Grammar` file, type the following command to compile:

    :::bash
    $ make -s -j2

Ach. If only it was that easy. This throws an error:

    :::pytb
    Traceback (most recent call last):
      File "/Users/amyhanlon/projects/nagini/cpython/Lib/runpy.py", line 151, in _run_module_as_main
        mod_name, loader, code, fname = _get_module_details(mod_name)
      File "/Users/amyhanlon/projects/nagini/cpython/Lib/runpy.py", line 113, in _get_module_details
        code = loader.get_code(mod_name)
      File "/Users/amyhanlon/projects/nagini/cpython/Lib/pkgutil.py", line 283, in get_code
        self.code = compile(source, self.filename, 'exec')
      File "/Users/amyhanlon/projects/nagini/cpython/Lib/sysconfig.py", line 4
        import sys
                 ^
    SyntaxError: invalid syntax

This error occurs while trying to execute a Python script! Compiling CPython requires running Python scripts! Interesting. Maybe at this point we remember that Python is [bootstrapped](http://en.wikipedia.org/wiki/Bootstrapping_(compilers)). We look back at the [Python Developer's Guide](http://docs.python.org/devguide/setup.html) and we find that *"Vast areas of CPython are written completely in Python: as of this writing, CPython contains slightly more Python code than C."*

So then we wonder - when CPython is compiling, does it execute Python scripts with the Python that's currently being compiled? Or does it use another already-compiled muggle Python, like our environment Python? If it uses the Python that's currently being compiled, we'll need to change these .py scripts to say `accio` instead of `import`. Otherwise, what do we do? Our muggle Python only understands `import` and not `accio`...

Let's look into one of the .py scripts within `Lib` to investigate. Here's the first line of the `Lib/keyword.py` script:

    :::text
    #! /usr/bin/env python

Aha! This script is executed via our environment Python! Our environment Python only understands `import`. So `keyword.py` needs to have `import` and not `accio`. However, since we got a `SyntaxError` on an `import` statement, that must mean that at least sometimes during the process of compiling we're required to use `accio` instead of `import`. Hrm... Any ideas?

#Yo Dawg, I Heard You Like Pythons

What if we did something crazy like compiled an intermediary Python that understands *both* `accio` *and* `import`, and used *that* Python to compile *another* Python that only understands `accio`? (Full credit for this idea goes to [Allison Kaptur](http://akaptur.github.io/).)

So, for our intermediary Python we'll need to edit the `Grammar` file like so:
    
    :::text
    import_name: 'import' dotted_as_names | 'accio' dotted_as_names
    import_from: (('from' ('.'* dotted_name | '.'+)
                  'import' ('*' | '(' import_as_names ')' | import_as_names)) |
                  ('from' ('.'* dotted_name | '.'+)
                  'accio' ('*' | '(' import_as_names ')' | import_as_names)))

Thus this Python should understand both `import` and `accio`. Let's compile.

    :::bash
    $ make -s -j2

Eep! No errors! Just the warning about missing modules that we also received before we made any changes! Now we need to prepend our $PATH so that this Python will become our environment Python (but only for this terminal session). That way this intermediary Python will be used to compile our final Python. Let's make a symlink to the `python.exe` that was created when we ran `make`, and then add the path to that symlink to our $PATH:

    :::bash
    $ mkdir bin
    $ cd bin
    $ ln -s ../python.exe python
    $ export PATH=`pwd`:$PATH

Now we'll need to duplicate this entire `cpython` directory and make our final Python:

    :::bash
    $ cd ../
    $ cp -r cpython nagini-python
    $ cd nagini-python

We want to change the `Grammar` file for this Python to only allow `accio`:

    :::text
    import_name: 'accio' dotted_as_names
    import_from: ('from' ('.'* dotted_name | '.'+)
                  'accio' ('*' | '(' import_as_names ')' | import_as_names))

And then we want to replace every instance of `import` in every .py file to `accio`. We'll use a blackbox bash command to accomplish that:
    
    :::bash
    $ for i in `find . -name '*.py'`; do sed -i '' 's/[[:<:]]import[[:>:]]/accio/g' $i; done

Now we just need to compile this new Python!

    :::bash
    $ make -s -j2

Let's make a symlink to this Python...

    :::bash
    $ mkdir bin
    $ cd bin
    $ ln -s ../python.exe python
    $ export PATH=`pwd`:$PATH
    $ python

And fire it up...

    :::pytb
    >>> import sys
      File "<stdin>", line 1
        import sys
                 ^
    SyntaxError: invalid syntax
    >>> accio sys
    >>> sys.modules.keys()
    ['copy_reg', 'sre_compile', '_sre', 'encodings', 'site', '__builtin__', 'sysconfig', '__main__', 'encodings.encodings', 'abc', 'posixpath', '_weakrefset', 'errno', 'encodings.codecs', 'sre_constants', 're', '_abcoll', 'types', '_codecs', 'encodings.__builtin__', '_warnings', 'genericpath', 'stat', 'zipimport', '_sysconfigdata', 'warnings', 'UserDict', 'encodings.ascii', 'sys', '_osx_support', 'codecs', 'os.path', 'sitecustomize', 'signal', 'traceback', 'linecache', 'posix', 'encodings.aliases', 'exceptions', 'sre_parse', 'os', '_weakref']


HOLY SHIT IT WORKS!

#Fin

That's it. We just compiled two Pythons and fooled around with source code for the sake of a joke. Grab yourselves a beer, friends. Victory.

My super messy and not-really-prepared-for-the-general-public GitHub [repo](https://github.com/amygdalama/nagini) contains both versions of Pythons, for reference. 
