Title: Pipeline
Date: 2014-03-08
Category: Projects
Tags: 
Slug: pipeline
Author: Amy Hanlon
Status: draft

Ideas for future posts:

* Furrier Transforms: A Journey that ends in failure
    (has a file already)
* My Personality is Open Source
    On how over the years I've learned to emulate characteristics of people that I like and how I welcome others to emulate me
    git clone, git fork, git merge, pull requests, etc
* How To Learn Programming Series
    I've covered the meta - now let's talk how to actually do it
    * git - learn git! make your code publicly available! use git every chance you can get!
    * contribute to open source - it's not as hard as it sounds! look for bugs/changes that can be made that the owner of the project would consider a nice-to-have (not essential) but just doesn't have time to fix themselves
    * some really good books and resources - LPTHW, Dive into Python, but stop reading them if you get bored!
* What is the difference between a Python Expression vs a Statement
* Getting Closure
    On printing locals() inside a closure function.
    i.e. what we discovered in the Dive into Python reading group:

        >>> def make_contains_function(x):
        ...     print('locals of factory function', locals())
        ...     def contains(s):
        ...         print('locals of inner function', locals())
        ...         return x in s
        ...     return contains
        ...
        >>> contains_a = make_contains_function('a')
        locals of factory function {'x': 'a'}
        >>> contains_a('asdkfj')
        locals of inner function {'x': 'a', 's': 'asdkfj'}
        True

    Additional resources:
        * http://stackoverflow.com/questions/4020419/closures-in-python
        * http://stackoverflow.com/questions/12919278/how-to-define-free-variable-in-python
        * https://docs.python.org/3/reference/executionmodel.html