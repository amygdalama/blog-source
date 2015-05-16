Title: Talks
Date: 2014-03-21
Author: Amy Hanlon
Slug: talks

## Investigating Python Wats

[PyCon 2015](https://us.pycon.org/2015/schedule/presentation/384/), [PyGotham 2014](https://pygotham.org/)

Many of us have experienced a "wat" in Python - some behavior that totally mystifies us. We'll look at three areas where wats arise - identity, mutability, and scope. For each of these three topics, we'll look at some common surprising behaviors, investigate the cause of the behaviors, and cover some practical tips on how to avoid related bugs.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sH4XF6pKKmk" frameborder="0" allowfullscreen></iframe>
<br>


## Replacing `import` with `accio`: Compiling Pythons with Custom Grammar for the sake of a joke!

[Open Source Bridge 2014](http://opensourcebridge.org/)

In Python, overwriting builtin functions is fairly easy. You can even do it in the interpreter! But can you overwrite a statement, like import, just as easily? Let's go on an adventure, discovering how the import statement works, and how Python statements are defined in the CPython source code. We'll face some consequences of bootstrapping, and, to get our custom Harry Potter-themed Grammar to work, we'll have to compile a Python to compile a Python.

Here are the [slides](http://www.slideshare.net/AmyHanlon/replacing-import-with-accio).
