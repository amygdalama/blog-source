Title: Dissecting Reduce and Lambda Statements
Date: 2014-03-29
Category: Projects
Tags: hacker school, python, functional programming, python internals
Slug: dissecting-reduce-and-lambda-statements
Author: Amy Hanlon
Status: draft

In Mary's functional programming [tutorial](http://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming) -- which, let me reiterate, you should read -- there's a mysterious code block:

    sum = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])

    print sum

Mary defines what `reduce` and `lambda` do:

> Reduce takes a function and a collection of items. It returns a value that is created by combining the items.

> [Lambda is] an anonymous, inlined function [...] The parameters of the lambda are defined to the left of the colon. The function body is defined to the right of the colon. The result of running the function body is (implicitly) returned.

That's great and all, but I still don't really understand what's going on.

A post on what happens to your local variables within a lambda statement.

Like:

    f = lambda a, x: a + locals().items()
    things = ['a', 'b', 'c'] 
    x = reduce(f, things, [])
    