Title: Projects
Date: 2014-03-21
Author: Amy Hanlon
Slug: projects

## stardatetime (2015)

`stardatetime` provides [`datetime`](https://docs.python.org/2/library/datetime.html) objects converted to Star Trek time.

    :::pycon
    >>> from stardatetime import StarDateTime
    >>> StarDateTime.now()
    StarDateTime(-307992.1713)

`stardatetime` is released on [PyPI](https://pypi.python.org/pypi/stardatetime) and the source is on [GitHub](https://github.com/amygdalama/stardatetime).


## nagini: replacing a keyword in CPython (2014)

At [Hacker School](https://www.hackerschool.com/), I built a Harry Potter-themed Python interpreter.

    :::pycon
    >>> accio random
    >>> random.random()
    0.6507285787268219

    >>> type(3)
    <__main__.Slytherin object at 0x1004c3290>

    >>> wingardium_leviosa(3)
    3.0

    >>> reducto(lambda a, x: a + x, range(5))
    10

    >>> avada_kedavra()


I described the process of overwriting the `import` keyword in this [blog post](http://mathamy.com/import-accio-bootstrapping-python-grammar.html).

I also gave a [talk](http://www.slideshare.net/AmyHanlon/replacing-import-with-accio) on this project at Open Source Bridge and a few NYC meetups.

Collaborators: [Allison Kaptur](http://akaptur.github.io/)

The code for this project is on [GitHub](https://github.com/amygdalama/nagini).

## Furrier Transform: converting an image of my cat to sound (2014)

At Hacker School, I attempted to create a sound from an image of my cat. The idea was that, since a spectrogram is an image representation of a sound, an arbitrary image could be interpreted as a spectrogram of a sound. With that assumption, I attempted to create a sound that would have the spectrogram of an image of my cat.

I quickly realized that starting with an image of my cat was a bad idea, because I had no way of telling if the sound I created was correct or not. So, I decided to start with an actual spectrogram of an actual sound, and then try to reconstruct the original sound from the spectrogram. Then I could tell if I was even close or not.

Later I found that this is actually a ["longstanding problem in audio signal processing"](http://arxiv.org/abs/1209.2076) and is anything but trivial. So, needless to say, I never completed this project. But I think I'm finally okay with that!

Fair warning: you do not want to listen to any audio files that this program creates. They are wildly unpleasant.

Collaborators: Andreas Dewes, David Dalrymple, Robert P. Sokolowski, Sean Patrick Murphy

The code for this project is on [GitHub](https://github.com/amygdalama/furrier-transform).

## Iron Forger (2014)

After Hacker School, I organized a weekly "make a product or you owe $5 to a charity" challenge called [Iron Forger](http://mathamy.com/introducing-iron-maker-or-forger-or-something.html).

In eight weeks, we made the following things:

* web framework
* Pacman clone
* version control system
* regular expression engine
* compress/decompress utility
* chat server & client
* interpreter

Collaborators: Rose Ames, David Branner, Rob Sokolowski, Stacey Sern, Pablo Torres
