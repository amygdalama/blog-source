Title: Dissecting the Reduce Function
Date: 2014-04-07
Category: Projects
Tags: hacker school, python, functional programming
Slug: dissecting-the-reduce-function
Author: Amy Hanlon

Good morning, [sinners](http://www.vice.com/columns/good-morning-sinners-with-warren-ellis). Today we're going to figure out what the hell is going on inside a Python expression like:

    :::pycon
    >>> reduce(lambda a, x: a + [x], things, [])

(What `things` is doesn't matter too much, as long as it's an iterable. We'll look at a more specific example in a bit.)

Mary Rose Cook [defines](http://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming) the `reduce` function nicely:

> Reduce takes a function and a collection of items. It returns a value that is created by combining the items.

Here, the function passed as a parameter to the `reduce` function is a `lambda` statement, which Mary also defines:

> [A `lambda` statement is] an anonymous, inlined function [...] The parameters of the `lambda` are defined to the left of the colon. The function body is defined to the right of the colon. The result of running the function body is (implicitly) returned.

A caveat: our `reduce` function also takes in a third parameter, the empty string, which I'll discuss in detail later.

Another caveat: if you're using Python3, `reduce` is no longer a builtin function. To use it, you'll need to:

    :::pycon
    >>> from functools import reduce

So, how do we better understand what's happening inside this expression?

## A Mental Model

Let's look at a specific example of our expression and examine a mental model -- which may or may not be correct -- for what's happening to the values of `a` and `x` inside the expression.

I said earlier that `things` needs to be an iterable. So, presumably, `things` could be a string. Let's try:

    :::pycon
    >>> things = '012'
    >>> reduce(lambda a, x: a + [x], things, [])
    ['0', '1', '2']

What's going on in this statement? My (not functional) mental model for how this works is:

For each `x` in `things`, convert `x` to a list and then append `[x]` to `a`, which starts as an empty list on the first iteration (this is because of the third parameter we passed to `reduce`, which I'll explain later). After each iteration, `a` grows one element longer (because we're adding whatever `[x]` is during the iteration to `a`). Return the result of the last iteration.

So, the first time we pass `a` and `x` through to the `lambda` statement:

    :::python
    x == things[0]
      == '0'

    a == []

The `lambda` then implicitly returns the list given by:

    :::python
    a + [x] == [] + [things[0]]
            == [] + ['0']
            == ['0']

The second time we pass `a` and `x` to `lambda`, we have:

    :::python
    x == things[1]
      == '1'

    # set `a` to the value the previous step implicitly returned
    a == ['0']

    a + [x] == ['0'] + ['1']
            == ['0', '1']

For the third and final step, we have:

    :::python
    x == things[2]
      == '2'

    a == ['0', '1']

    a + [x] == ['0', '1'] + ['2']
            == ['0', '1', '2']

So why did we have to pass `[]` as the third parameter to `reduce`? Well, if `reduce` isn't given a third parameter, for the first iteration it sets `a = x`, and then jumps to the second iteration. So, in my mental model, the first iteration would look like:

    :::python
    x == things[0]
      == '0'

    a == x
      == '0'

    # no calculation of a + [x]
    # instead, implicitly returns the value of `a`, which is '0'

And then in the second iteration:

    :::python
    x == things[1]
      == '1'

    # set `a` to the value implicitly returned from the first iteration
    a == '0'

    a + [x] == '0' + ['1']

This results in an error because you can't concatenate a string and a list.

Is my mental model correct? We can tell that the model ultimately returns the same value as the expression, but how can we tell if these are really the values of `a` and `x` at each step?

## Testing the Model

We'll need to figure out some clever way of printing or storing the values of `a` and `x` at each step.

Let's recall the original expression:

    :::pycon
    >>> reduce(lambda a, x: a + [x], things, [])

Here we append the value of `x` to `a`. Could we also append the value of `a` itself? Then maybe we could see what `a` is at each step. Let's try:

    >>> reduce(lambda a, x: a + [{'a' : a, 'x' : x}], things, [])

There's a lot going on in that expression, so let's break it up:

    :::pycon
    >>> things = '012'
    >>> f = lambda a, x: a + [{'a' : a, 'x' : x}]
    >>> reduce(f, things, [])

Let's apply the mental model to help us understand this example.

####Step 1:

    :::python
    x == things[0]
      == '0'

    a == []

    # this step implicitly returns the value:
    a + [{'a' : a, 'x': x}]
      == [] + [{'a' : [], 'x' : '0'}]
      == [{'a' : [], 'x' : '0'}]

####Step 2:

    :::python
    x == things[1]
      == '1'

    a == [{'a' : [], 'x' : '0'}]

    a + [{'a' : a, 'x': x}]
      == [{'a' : [], 'x' : '0'}] + [{'a' : [{'a' : [], 'x' : '0'}], 'x': '1'}]
      == [{'a' : [], 'x' : '0'}, {'a' : [{'a' : [], 'x' : '0'}], 'x': '1'}]

####Step 3:

    :::python
    x == things[2]
      == '2'

    a == [{'a' : [], 'x' : '0'}, {'a' : [{'a' : [], 'x' : '0'}], 'x': '1'}]

    a + [{'a' : a, 'x': x}]
        == [{'a' : [], 'x' : '0'}, {'a' : [{'a' : [], 'x' : '0'}], 'x': '1'}]
            + [{'a' : [{'a' : [], 'x' : '0'}, {'a' : [{'a' : [], 'x' : '0'}], 'x': '1'}], 'x': '2'}]
        == [{'a' : [], 'x' : '0'},
            {'a' : [{'a' : [], 'x' : '0'}], 'x': '1'},
            {'a' : [{'a' : [], 'x' : '0'}, {'a' : [{'a' : [], 'x' : '0'}], 'x': '1'}], 'x': '2'}]

This is pretty complicated and difficult to read. You might want to write out the steps for yourself. I did (obviously). And I screwed it up the first few times.

Let's see if our result from step 3 is the same as what Python evaluates for our expression:

    :::pycon
    >>> answer = reduce(f, things, [])
    >>> result = [{'a' : [], 'x' : '0'},
    ... {'a' : [{'a' : [], 'x' : '0'}], 'x': '1'},
    ... {'a' : [{'a' : [], 'x' : '0'}, {'a' : [{'a' : [], 'x' : '0'}], 'x': '1'}], 'x': '2'}]
    >>> answer == result
    True

Victory! But what does this mean?

## Wait what were we trying to do again?

We've been attempting to understand what happens inside a `reduce` function. We developed a mental model for what happens to the values of `a` and `x` at each iteration, and we came up with a way to test to see if the mental model was accurate. And it was!

I think this might be one of those posts that is less about what I intended it to be about (dissecting the `reduce` function) and more about the approach I would take to accomplish what I intended it to be about. Meta, sinners.
