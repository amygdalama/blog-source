Title: Untitled
Date: 2014-03-29
Category: Projects
Tags: learning, hacker school, python, functional programming, python internals, grammar
Slug: untitled
Author: Amy Hanlon
Status: draft



What if we tried using the `**` operator? Can we pass something like `** 2` or `+ 2` as the function for `map`? Let's try:

    >>> squares = map(** 2, [0, 1, 2, 3, 4])
      File "<stdin>", line 1
        squares = map(** 2, [0, 1, 2, 3, 4])
                          ^
    SyntaxError: invalid syntax

`SyntaxError`. This makes me think that `**` is part of a statement, defined in Python's Grammar file, and the way that we've typed our code is in violation of the the definition of that statement. 


==============================

So, let's look in the [Grammar file](http://docs.python.org/2/reference/grammar.html). We're not afraid to look at the Grammar file.

Searching for "**" in the Grammar, we find the line:

    power: atom trailer* ['**' factor]

Since we've read Allison Kaptur's [post](http://akaptur.github.io/blog/2014/03/16/reading-ebnf/) on reading EBNF, the language in which Python's Grammar file is written, we know how to read this statement. Translating to English: a `power` statement consists of an `atom`, followed by zero or more `trailer`s, optionally followed by the literal string `'**'` and a `factor`.

I have no clue what an `atom`, `trailer`, or `factor` is, so let's look those up.

    atom: ('(' [yield_expr|testlist_comp] ')' |
       '[' [listmaker] ']' |
       '{' [dictorsetmaker] '}' |
       '`' testlist1 '`' |
       NAME | NUMBER | STRING+)

    trailer: '(' [arglist] ')' | '[' subscriptlist ']' | '.' NAME

    factor: ('+'|'-'|'~') factor | power

And now I feel like an ouroboros. What does this mean. 

Let's try another approach. How about we [google "python grammar power operator"](https://www.google.com/search?q=python+grammar+power+statement&oq=python+grammar+power+statement&aqs=chrome..69i57.7035j1j4&sourceid=chrome&espv=210&es_sm=91&ie=UTF-8#q=python+grammar+power+operator). The first result is this nice [Python documentation on Expressions](https://docs.python.org/2/reference/expressions.html):
 
    power ::=  primary ["**" u_expr]

So `power` consists of a `primary` followed by optionally the literal string '**' and a `u_expr`. This seems 

But now I'm confused. What's the difference between a Python *statement* and a Python *expression*? Well, there's a [StackOverflow answer](http://stackoverflow.com/a/4728147) for that.