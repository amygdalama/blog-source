Title: A Love Affair With Broken Things, Plus Some Functional Programming
Date: 2014-03-29
Category: Projects
Tags: learning, hacker school, python, functional programming
Slug: a-love-affair-with-broken-things
Author: Amy Hanlon
Status: draft

I love broken things, unfinished things, breaking things, unfinishing things. Broken and unfinished things allow you to see the process in which they were created; their most intimate secrets are exposed.

##Broken Statues

A week ago, inside [The Metropolitan Museum of Art](http://www.metmuseum.org/en), my love for broken things was realized. Just *look* at these. They're so *naked, vulnerable*.

![some ladies, broken](/images/broken_ladies.JPG "broken ladies")
![a face, broken](/images/broken_face.JPG "broken face")
![a torso, broken](/images/broken_torso.JPG "broken torso")

Okay so some of them are literally naked, but you get the point. When a statue is broken, you can sneak a peek inside! You get so many clues about how it was made! Is it hollow? What's it made out of? Is the material on the outside the same as the inside? Does it have a frame?

##Breaking Code

While I can't bring myself to break art to get clues about the process of its creation, I *can* break code! Breaking code is free and doesn't hurt anyone! I do this quite a bit as a method of learning - removing the pieces of code that you don't understand reveals the purpose of those pieces. It's like removing the arm of a statue to look inside.

Let's look at some code from Mary Rose Cook's functional programming [tutorial](http://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming) (which is amazing, and you should absolutely read it and do the exercises and spend time understanding it completely if you're at all interested in functional programming). We won't understand the code at first (or at least *I* won't), but we'll take apart the pieces of the code in attempt to understand their purpose better.

Mary aptly explains what Python's builtin `map` function does:

> Map takes a function and a collection of items. It makes a new, empty collection, runs the function on each item in the original collection and inserts each return value into the new collection. It returns the new collection.

Her first example for showing how `map` works is fairly straightforward:

> This is a simple map that takes a list of names and returns a list of the lengths of those names:
>
    name_lengths = map(len, ["Mary", "Isla", "Sam"])
    print name_lengths
    # => [4, 4, 3]

In the second example of `map`, we see that Mary uses a `lambda` function: 

> This is a map that squares every number in the passed collection:
>
    squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
    print squares
    # => [0, 1, 4, 9, 16]

Why do we need a `lambda` function here? To understand, let's try removing it:

    >>> squares = map(x * x, [0, 1, 2, 3, 4])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'x' is not defined  

Okay. `x` is not defined. That makes sense, because `x` isn't in our `locals` or our `globals` or our `builtins`.

What if we tried using the `**` operator? Can we pass something like `** 2` or `+ 2` as the function for `map`? Let's try:

    >>> squares = map(** 2, [0, 1, 2, 3, 4])
      File "<stdin>", line 1
        squares = map(** 2, [0, 1, 2, 3, 4])
                          ^
    SyntaxError: invalid syntax

`SyntaxError`. This makes me think that `**` is part of a statement, defined in Python's Grammar file, and the way that we've typed our code is in violation of the the definition of that statement. So, let's look in the [Grammar file](http://docs.python.org/2/reference/grammar.html). We're not afraid to look at the Grammar file.

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