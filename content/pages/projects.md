Title: Projects
Date: 2014-03-21
Author: Amy Hanlon
Slug: projects

##Nagini: Replacing `import` with `accio`

Replacing Python builtin functions and statements with Harry Potter spells. The internet [loved](https://news.ycombinator.com/item?id=7402620) this one.

I first started with messing around with Python's `__builtin__` module -- seeing what I could shadow and delete. Then, I decided to go after the `import` statement, which lead me to cloning CPython source code and fiddling around with the `Grammar` file.

I [blogged](http://mathamy.com/import-accio-bootstrapping-python-grammar.html) about the project, and my code is on [GitHub](https://github.com/amygdalama/nagini).

This project was also the inspiration for my first [talk](/pages/talks).

##Furrier Transform: Converting a picture of my cat to sound

This was a huge failure. 

A signal (in this case, a sound) can be represented visually as a spectrogram, an image where the x-axis corresponds to time, the y-axis corresponds to frequency, and the pixels in the image are colored by their amplitude. So, theoretically, any image could be assumed to be a spectrogram of a sound. In practice, extracting the original signal from a spectrogram is quite difficult, and I did not manage to succeed.

My code is on [GitHub](https://github.com/amygdalama/furrier-transform), although this project is potentially indefinitely incomplete.