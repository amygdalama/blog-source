Title: Talks
Date: 2014-03-21
Author: Amy Hanlon
Slug: talks

## Investigating Python Wats

Many of us have experienced a "wat" in Python - some behavior that totally mystifies us. We'll look at three areas where wats arise - identity, mutability, and scope. For each of these three topics, we'll look at some common surprising behaviors, investigate the cause of the behaviors, and cover some practical tips on how to avoid related bugs.

I gave this talk at [PyGotham 2014](http://pygotham.org/). Here's the [full proposal](https://github.com/amygdalama/wats/blob/master/pycon/proposal.md) and here are the [slides](http://www.slideshare.net/AmyHanlon/python-wats-uncovering).

## Replacing `import` with `accio`: Compiling Pythons with Custom Grammar for the sake of a joke!

In Python, overwriting builtin functions is fairly easy. You can even do it in the interpreter! But can you overwrite a statement, like import, just as easily? Let's go on an adventure, discovering how the import statement works, and how Python statements are defined in the CPython source code. We'll face some consequences of bootstrapping, and, to get our custom Harry Potter-themed Grammar to work, we'll have to compile a Python to compile a Python.

Here's the [full proposal](https://github.com/amygdalama/talks/blob/master/nagini/proposal.md) and here are the [slides](http://www.slideshare.net/AmyHanlon/replacing-import-with-accio).

I've given versions of this talk at [Open Source Bridge](http://opensourcebridge.org/), [NYC Python](http://www.meetup.com/nycpython/), and [NYC Hack and Tell](http://www.meetup.com/hack-and-tell/).