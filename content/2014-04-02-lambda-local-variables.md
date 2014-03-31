Title: Untitled
Date: 2014-03-29
Category: Projects
Tags: learning, hacker school, python, functional programming
Slug: untitled2
Author: Amy Hanlon
Status: draft

A post on what happens to your local variables within a lambda statement.

Like:

    f = lambda a, x: a + locals().items()
    things = ['a', 'b', 'c'] 
    x = reduce(f, things, [])
    