Title: Death to the rubber stamp!
Date: 2015-07-19
Category: Projects
Tags: code review
Slug: death-to-the-rubber-stamp
Author: Amy Hanlon

You work really hard on some code, submit a pull request, hoping for some feedback, and then, dun dun dunnnn...
> ✨ lgtm! ✨

<iframe src="//giphy.com/embed/3h5pe45FM9qUM" width="480" height="267" frameBorder="0" style="max-width: 100%" class="giphy-embed" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>

Come on. We all know that all software is broken. No pull request is perfect -- there's always room for improvement. Yet so often we respond with an even shorter version of *"yeah, sure, whatever"*.

This response is not helpful for you as the reviewer, and it's not helpful for the author, and it's not helpful for your organization. So, let's say someone assigns you a pull request. How can you do something more useful than simply giving it a rubber stamp of approval?

### Ask lots of questions!

When I get a pull request, here are some questions I ask myself (and if the answer isn't clear, I ask the author).
These questions both help find improvements in the patch, and also can start meaningful discussions that can help each of you learn more about how to think about code.

### Meta

* What problem is this pull request is solving?
* Is it solving the right problem?
* Does it solve the problem?
* What are other ways the problem could be solved? Why did the author choose this solution?

### History

* Do the commit messages accurately describe what problem is being solved?
* Do the structure and history of the commits make sense? 
* Are there any surprises in any of the commits (eg things you wouldn't expect to be included in the commit based on the commit message)?

### Design

> Good programmers write code that humans can understand.
*- Martin Fowler*

* Is the code well-tested?
* Is the code easy to read?
* Are there any parts that are confusing?
* Are the names informative?
* Are there any functions that do things that surprise you?
* Do the functions do only one thing?
* Are the statements in each function all at the same level of abstraction?
* Are there any other code smells?

If the code is confusing or hard to read, that's a problem with the code, not you (the reader). Ask the author to clarify and to make it easier to read.

### Details

* Does the code comply to your org's coding standards?
* Could the tests ever fail?
* Do you see any obvious bugs? (This one's hard!)
* Does the patch touch any particularly volatile or high-risk parts of the codebase?
* If the patch has bugs, what's the worst thing that could happen?

What questions do you ask when reviewing code?

### Related reading

* [Code reviews with a rubber stamp](https://rachelbythebay.com/w/2012/03/10/review/)
* [Please don't rubber stamp code reviews](https://groups.google.com/a/chromium.org/forum/#!topic/chromium-dev/b0Lb_mXfp0Y)
* [Asking questions is a superpower](http://jvns.ca/blog/2014/06/13/asking-questions-is-a-superpower/)
* [Your Brain's API: Giving and receiving technical help](https://www.youtube.com/watch?v=hY14Er6JX2s)
* [Clean Code](http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/01323508820)
