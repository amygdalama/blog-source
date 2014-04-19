Title: Projects
Date: 2014-03-21
Author: Amy Hanlon
Slug: projects

## Nagini: Replacing `import` with `accio`

I spent about a week at Hacker School mischievously replacing Python builtin functions and statements with Harry Potter spells. I've named this custom Harry Potter-themed Python Nagini, after Voldemort's snake.

In order to replace the import statement, I needed to compile an intermediary Python that understood both "import" and "accio" as valid statements and then use that Python to compile another Python that only understood "accio" as a valid statement (rather than "import"). The main modifications to the CPython source code occured in the Grammar files. Here are the two versions of the files:  

* [Both "accio" and "import" defined as statements](https://github.com/amygdalama/nagini/blob/master/cpython/Grammar/Grammar)  
* [Only "accio" defined as a statement](https://github.com/amygdalama/nagini/blob/master/nagini-python/Grammar/Grammar)  

*(The relevant lines start at around line 53 in both of those files.)*

I wrote a [blog post](http://mathamy.com/import-accio-bootstrapping-python-grammar.html) about this project and the internet loved it - it was on the front page of [Hacker News](https://news.ycombinator.com/item?id=7402620) and on Reddit and a bunch of people Tweeted about it. 

I also gave a [talk](http://www.slideshare.net/AmyHanlon/replacing-import-with-accio) on this project at NYC PyLadies and at Hack and Tell.  

Things I learned about:

* CPython source code, in general. I'm fairly comfortable with its organization and structure.
* Python Grammar file, specifically. The Grammar file is where valid Python statements are defined. I had to edit this file a couple of times in order to replace the import statement with "accio", a Harry Potter spell, which is one letter shorter, so strictly better, than "import".
* Compilers and bootstrapping. In order to change Python's Grammar, I needed to compile a Python to compile a Python. This was really interesting! Much credit goes to Allison Kaptur for helping me figure this out. 
* Mercurial. I had never used Mercurial before! I still don't know a whole lot about it, but I now have it set up on my computer and can clone repositories and change branches.
* PYTHONSTARTUP. This is an environment variable that you can use to make Python scripts execute automatically any time the Python interpreter is run. I use this to run a Python script that replaces a bunch of builtin functions with Harry Potter spells any time I run nagini.
* Bash and Unix. I learned about Unix environments, the `sed` command, symlinks, and executables.

The code for this project is on [GitHub](https://github.com/amygdalama/nagini).

## Furrier Transform: Converting a picture of my cat to sound  

This was an attempt at creating a sound from an image of my cat. The idea was that, since a spectrogram is an "image" representation of a sound, an arbitrary image could be interpreted as a spectrogram of a sound. With that assumption, I attempted to create a sound that would have the spectrogram of an image of my cat.

I quickly realized that starting with an image of my cat was a bad idea, because I had no way of telling if the sound I created was correct or not. So, I decided to start with an actual spectrogram of an actual sound, and then try to reconstruct the original sound from the spectrogram. Then I could tell if I was even close or not.

Later I found that this is actually a ["longstanding problem in audio signal processing"](http://arxiv.org/abs/1209.2076) and is anything but trivial. So, needless to say, I never "completed" this project. But I think I'm finally okay with that.

Fair warning: you do not want to listen to any audio files that this program creates. They are wildly unpleasant.

Things I learned about: 

* Fourier Transforms, Additive Synthesis, signal processing, and how sound works in the analog and digital worlds. This was super interesting and fun to learn about!
* numpy, scipy, matplotlib, and ipython notebooks.  

The code for this project is on [GitHub](https://github.com/amygdalama/furrier-transform).

## Phonebook Command Line Tool  

A phonebook command line tool, which sounds boring, but it was super interesting to make!

Things I learned about:

* Sqlite3 specifically, and databases in general. I had never worked with a database before! I essentially wrote a wrapper for sqlite3 to interact with databases that store phonebook (name and phone number) entries.
* Raising Exceptions. I hadn't really done this before, either!
* Python's argparse module. Whoa - this module is cool. This is the first time I've used it, and it was super interesting! I learned how to create parsers and subparsers, set default values for arguments, and set default functions to execute for each subparser.
* Tests! I had never written extensive tests before. I learned about Python's unittest and nose modules. I spent a lot of time thinking about how to design my test cases and how to test if any unexpected behavior occurred.

The code for this project is on [GitHub](https://github.com/amygdalama/phonebook).

## Weekly Blog  

I've maintained a slightly-more-frequent-than-weekly [blog](http://mathamy.com/) since starting Hacker School. I realized that writing is one of the ways I learn best - explaining things forces me to think very explicitly about them. Often, when I sit down to write a blog post, I realize that I didn't understand the topic as well as I thought, so I put in extra effort to understand the topic very well.

Some posts:

* [Python Closures and Free Variables](http://mathamy.com/python-closures-and-free-variables.html)
* [Dissecting the Reduce Function](http://mathamy.com/dissecting-the-reduce-function.html)
* [After Six Months of Learning The Python I Can Finally Print 'Hello World'!](http://mathamy.com/after-six-months-of-learning-the-python-i-can-finally-print-hello-world.html)
* [A Love Affair With Broken Things](http://mathamy.com/a-love-affair-with-broken-things.html)
* [What's the deal with `__builtins__` vs `__builtin__`](http://mathamy.com/whats-the-deal-with-builtins-vs-builtin.html)
* [Replacing `import` with `accio`: A Dive Into Bootstrapping and Python's Grammar](http://mathamy.com/import-accio-bootstrapping-python-grammar.html)
* [How Should I Learn Programming?](http://mathamy.com/how-should-i-learn-programming.html)
* [Migrating to GitHub Pages using Pelican](http://mathamy.com/migrating-to-github-pages-using-pelican.html)


## Personal Website  

I entered the batch with a simple Wordpress blog and quickly realized that I could not stand formatting code blocks in Wordpress's editor. Plus Wordpress is so *boring*. So I made a static site hosted on GitHub Pages.
After setting up my new website, I wrote a [blog post](http://mathamy.com/migrating-to-github-pages-using-pelican.html) on how I did it, and was able to help a bunch of other Hacker Schoolers who wanted a similar setup.

Things I learned about:

* Pelican, a static site-generator, like Octopress, but written in Python. Static site generators are super rad because they allow you to write posts in Markdown, which brings me to...
* Markdown!
* Git. I can't count how many times I accidentally deleted or corrupted my git repositories for my blog. Because I was really clumsy with Pelican at first, I'd often make horrible, horrible mistakes and then use git to revert changes. The worst was when I thought I merged something gracefully, published my changes, and then found a bunch of ">>> HEAD" marks floating all over my website. At 11pm. But, now. Now I am a master.
* Git hooks, which allows you to run scripts before or after particular git commands. This was super wonderful because I have two separate repos for my blog - one for the content in Markdown and another for the HTML output that Pelican makes. Git hooks allows me to automatically add, commit, and push the output repo to GitHub any time I push the source repo. Super awesome.
* SimpleHTTPServer! I learned about the process of local development, and serving my site locally.
* Jinja, a Python package which handles Pelican's templating.
* CSS and HTML, and how they fit together.
* Chrome's lovely "Inspect Element" tool. What would I do without you.

[Here](https://github.com/amygdalama/blog-source)'s the repo containing my source content, customized theme, and configuration files.