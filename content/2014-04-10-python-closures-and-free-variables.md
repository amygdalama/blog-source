Title: Python Closures and Free Variables
Date: 2014-04-10
Category: Python Internals
Tags: python, python internals, functional programming, closures
Slug: python-closures-and-free-variables
Author: Amy Hanlon

Today, friends, we will continue to dissect functional programming concepts in Python. We're going to try to figure out what the hell is going on in this chunk of code:

    :::pycon
    >>> def make_contains_function(x):
    ...     def contains(s):
    ...             return x in s
    ...     return contains

What happens when we pass `make_contains_function` a string?

    :::pycon
    >>> make_contains_function('a')
    <function contains at 0x10a1e2cf8>

We get a function! Whoa. A function that returns a function. Cool. Let's assign this returned function a name and try to use it:

    :::pycon
    >>> contains_a = make_contains_function('a')
    >>> contains_a
    <function contains at 0x10a1e2c80>
    >>> contains_a('cat')
    True
    >>> contains_a('bro')
    False

We can create a function called `contains_a` by calling the `make_contains_function` and passing the string `'a'` as a parameter. Then, when we pass `contains_a` a string, the function returns a boolean representing whether `'a'` is in the string or not.

Let's look at the original code again and try to understand what it does and why it works:

    :::pycon
    >>> def make_contains_function(x):
    ...     def contains(s):
    ...             return x in s
    ...     return contains

First let's translate this to English. We're creating a function called `make_contains_function`, which takes one parameter, `x`. In the body of the `make_contains_function`, we create an inner function called `contains`, which takes one parameter, `s`. The inner function returns `x in s`, and then the outer function returns the inner function.

But how does `contains` have access to `x`? Shouldn't that throw a `NameError`? Here's my mental model for how Python looks up the value associated with a name of a variable, `x`:

1. Check to see if `x` is in the `locals()` dictionary. If it is, then the value of `x` is the value associated with `x` in `locals()`. i.e.:

        :::python
        if x in locals():
            return locals()[x]

2. Check to see if `x` is in the `globals()` dictionary. If it is, then the value of `x` is the value associated with `x` in `globals()`. i.e.:

        :::python
        elif x in globals():
            return globals()[x]

3. Check to see if `x` is in the `__builtins__.__dict__` dictionary. If it is, then the value of `x` is the value associated with `x` in `__builtins__.__dict__`. i.e.:

        :::python
        elif x in __builtins__.__dict__:
            return __builtins__.__dict__[x]

4. Otherwise, throw a `NameError`.

My mental model for how `locals()` works is that it returns all local variables, which are defined in the *most narrowly-defined* current scope. In the case of `x` in our example, the most narrowly-defined current scope is the function `contains`. Since `x` isn't assigned a value within the function `contains`, `locals()` won't contain a value for `x` (based on my mental model).

My model for how `globals()` works is that it returns the variables which are defined at the module-level (i.e. variables which aren't defined within a scope like a function or a class. Since `x` is defined within a function, namely within the `make_contains_function`, it won't be included in the `globals()` dictionary either.

`x` is pretty clearly not defined in `__builtins__.__dict__`, because it isn't defined in the `builtin` module. (It isn't automatically imported any time you run Python).

Poor `x`.

So is my mental model correct? If it is, we should be getting a `NameError` when we execute the `contains_a` or `contains_b` functions. Since we're not getting a `NameError`, something about my mental model must be inaccurate.

Shucks.

Let's try printing the `locals()` within each of the functions in our code block, to see where `x` is defined:

    :::pycon
    >>> def make_contains_function(x):
    ...     print "Inside make_contains_function"
    ...     print "locals(): ", locals()
    ...     def contains(s):
    ...             print "Inside contains function"
    ...             print "locals(): ", locals()
    ...             return x in s
    ...     return contains

If my mental model is correct, `x` should be returned by `locals()` within the `make_contains_function`, but not by `locals()` within the `contains` function. Let's put my model to the test!

    :::pycon
    >>> contains_a = make_contains_function('a')
    Inside make_contains_function
    locals():  {'x': 'a'}
    >>> contains_a('cat')
    Inside contains function
    locals():  {'x': 'a', 's': 'cat'}
    True

Oh! So `x` is returned by `locals()` inside the `contains` function. That's why we don't get a `NameError` when we try using `x`. My mental model of how `locals()` works and what it returns must be wrong. Let's look at the [documentation](https://docs.python.org/2/library/functions.html#locals) for `locals()`:

> Update and return a dictionary representing the current local symbol table. Free variables are returned by `locals()` when it is called in function blocks but not in class blocks.

Hm. What is a "free variable"? Does that apply to our situation? I suspect it does. Either that or my definition of a local variable is wrong. Googling "python free variable" brings us to the trusty Python [Execution Model](https://docs.python.org/2/reference/executionmodel.html) page, which I strongly believe every Python programmer should read and re-read often.

> When a name is used in a code block, it is resolved using the nearest enclosing scope. The set of all such scopes visible to a code block is called the block's *environment*.

> If a name is bound in a block, it is a local variable of that block. If a name is bound at the module level, it is a global variable. (The variables of the module code block are local and global.) If a variable is used in a code block but not defined there, it is a *free variable*.

Let's apply this information to our example, and list what we know:

1. `contains` is a function.

2. `x` is a free variable in `contains`, because it is referenced in `contains` but isn't defined there.

3. Free variables are not local variables.

4. However, free variables are returned when calling `locals()` within a function block.

Okay! When Python looks up the name `x`, it finds a value for it in the `locals()` dictionary, even though `x` isn't a local variable. My mental model wasn't *too* far off. I just need to adjust how I think about how `locals()` behaves within functions.

And, so that you understand the title of this post, and so that you can sound smart around other programmers, you should know that a function that uses a *free variable* is called a *closure*. So, in our example, `x` is a *free variable* and the function `contains` is a *closure*.

Credit to [Tom Ballinger](https://twitter.com/ballingt) for the example code block and for intoducing me to [Dive Into Python3](http://www.diveintopython3.net/), an excellent read and the inspiration for this post.