Title: Phonebook Exercise
Date: 2014-07-14
Author: Amy Hanlon
Slug: phonebook
Status: hidden

<a name="top"></a>
Let's make a command line tool for managing phonebook entries!

# Introduction

This exercise is organized in a few sections:

[TOC]

Depending on your learning style and experience level, you might get through all of these sections. Or you might just get through the first one. That's okay! The main priority for this exercise is to write a lot of code and understand what the code you're writing does. Don't worry about "finishing", whatever that means.

If you don't understand a phrase or a line of code that I use, ask me! I can show you what I'd do to figure out what the line of code means. Learning how to figure out the things you don't know is an important skill in programming.

The more challenging sections are marked with an asterisk (*). If you find the sections without askerisks challenging, I recommend skipping the more challenging ones for now. You can come back to them later if you're curious.

On the other hand, if you have a good idea for how to do the things outlined in a section, try doing it without reading through the section first, and just use the tutorial for reference if you get stuck.

At the end of some sections I have links to additional resources if you'd like to implement a more advanced command line tool.

# 1. Specifications

We'll write a Python program that will support creating, retrieving, updating, and deleting phonebook entries consisting of a name and a phone number.

The program will have a command line interface supporting the following commands and behaviors:

    :::console
    $ python phonebook.py create ex_phonebook
    Created phonebook 'ex_phonebook.pb' in the current directory.

    $ python phonebook.py add 'Jane Doe' '432 123 4321' ex_phonebook
    Added an entry to ex_phonebook.pb:
    Jane Doe    432 123 4321
    $ python phonebook.py add 'Jane Lin' '509 123 4567' ex_phonebook
    Added an entry to ex_phonebook.pb:
    Jane Lin    509 123 4567
    $ python phonebook.py add 'Jane Lin' '643 357 9876' ex_phonebook
    Error: Jane Lin already exists in ex_phonebook. Use the 'update' command to change this entry.

    $ python phonebook.py update 'Jane Lin' '643 357 9876' ex_phonebook
    Updated an entry in ex_phonebook.pb.
    Previous entry:
    Jane Lin    509 123 4567
    New entry:
    Jane Lin    643 357 9876

    $ python phonebook.py lookup 'Jane' ex_phonebook
    Jane Doe    432 123 4321
    Jane Lin    643 357 9876

    $ python phonebook.py reverse-lookup '643 357 9876' ex_phonebook
    Jane Lin    643 357 9876

    $ python phonebook.py remove 'Jane Doe' ex_phonebook
    Removed an entry from ex_phonebook.pb:
    Jane Doe    432 123 4321
    $ python phonebook.py remove 'John Doe' ex_phonebook
    Error: 'John Doe' does not exist in ex_phonebook.pb

[Back to top](#top)

# 2. Code Skeleton

What are the functions that you'll need for your program? What arguments will each of those functions need? Write a skeleton program that has those functions definitions, but where the functions just `pass`, rather than actually doing anything.

Here is an example skeleton program with function definitions for `create`ing a phonebook and `add`ing an entry to the phonebook. You'll need more functions, too, but this is a start:

    :::python
    def create_phonebook(phonebook_name):
        # create a new phonebook
        pass


    def add_entry(name, number, phonebook_name):
        # add a new name and number to the given phonebook
        pass


    if __name__ == '__main__':
        pass

Similarly, create functions for `update`, `lookup`, `reverse-lookup`, and `delete`.

Wondering what the `if __name__ == '__main__'` code block is for? It's where you put code that you want to execute when you run this Python script directly, but not when you `import` this script into another one. More information on what that means can be found in the [Further Reading](#__name__) section.

[Back to top](#top)

# 3. Argument parsing

## 3.1 Accessing Arguments

Arguments passed to Python scripts from the command line are accessible using the `sys` module. Here's a simple example script that prints out the arguments passed to the Python interpreter:

    :::python
    # ex.py
    import sys

    print "The arguments given to the interpreter are:"
    print sys.argv

What happens when you execute the script giving it some arguments?

    :::console
    $ python ex.py cats dragons frogs
    The arguments given to the interpreter are:
    ['ex.py', 'cats', 'dragons', 'frogs']

So `sys.argv` is a list, containing the name of the script (`'ex.py'`), and then the three arguments we passed, all represented as strings.

[Back to top](#top)

## 3.2 Parsing Arguments

For your phonebook application, you might choose to manually parse your arguments. This code should go in an `if __name__ == '__main__'` code block because parsing arguments doesn't make sense when you're `import`ing a module.

For the first two commands, `create` and `add`, your code would look something like this:

    :::python
    def create_phonebook(phonebook_name):
        # create a new phonebook
        pass


    def add_entry(name, number, phonebook_name):
        # add a new name and number to the given phonebook
        pass


    # include functions for other commands


    if __name__ == '__main__':
        args = sys.argv[:]      # make a copy
        script = args.pop(0)    # name of script is first arg
        command = args.pop(0)   # the next arg will be the main command

        if command == 'create':
            phonebook_name = args.pop(0)
            create_phonebook(phonebook_name)

        elif command == 'add':
            name = args.pop(0)
            number = args.pop(0)
            phonebook_name = args.pop(0)
            add_entry(name, number, phonebook_name)

Similarly, define `elif` statements for `update`, `lookup`, `reverse-lookup`, and `delete`.

If you're not sure how the `pop` method works, google it, and play around with it in your REPL! Some questions you can try to figure out:

1. What happens if you don't give `pop` an argument?
2. What does the comment "make a copy" mean?

[Back to top](#top)

## 3.3 Unpacking Arguments

List unpacking can make our code naming the variables in each of the `if`/`elif` blocks much cleaner.

For example, we can turn this:

    :::python
    name = args.pop(0)
    number = args.pop(0)

into this:

    :::python
    name, number = args

This takes the first element in `args` and assigns it to the variable `name`, and the second element in `args` and assigns it to the variable `number`.

Edit the code for each of your commands to use list unpacking everywhere you have multiple lines with `pop` in a row.

An example for the `add` and `create` commands would look like this:

    :::python
    def create_phonebook(phonebook_name):
        # create a new phonebook
        pass


    def add_entry(name, number, phonebook_name):
        # add a new name and number to the given phonebook
        pass


    # include functions for other arguments


    if __name__ == '__main__':
        args = sys.argv[:]      # make a copy
        script = args.pop(0)    # name of script is first arg
        command = args.pop(0)   # the next arg will be the main command

        if command == 'create':
            phonebook_name = args.pop(0)
            create_phonebook(phonebook_name)

        elif command == 'add':
            name, number, phonebook_name = args
            add_entry(name, number, phonebook_name)

We left the `pop` line for the `create` command since there should be only one argument left. What happens if you try to unpack a list with only one element? Try figuring it out in your REPL.

Similarly, define `elif` statements for `update`, `lookup`, `reverse-lookup`, and `delete`.

[Back to top](#top)

## 3.4 Handling Bad Arguments

What happens if your program isn't given any arguments? Try:

    :::console
    $ python phonebook.py
    Traceback (most recent call last):
      File "phonebook.py", line 69, in <module>
        command = args.pop(0)   # the next arg will be the main command
    IndexError: pop from empty list

What if it's given an argument that isn't supported?

    :::console
    $ python phonebook.py cats

What about if you try `add`ing a phone number, but you only give it a name, and not a number?

    :::console
    $ python phonebook.py add 'Jane Doe'
    Traceback (most recent call last):
      File "phonebook.py", line 79, in <module>
        name, number, phonebook_name = args
    ValueError: need more than 1 value to unpack

What about if you give it a name, number, and an extra nonsensical argument?

    :::console
    $ python phonebook.py add 'Jane Doe' '765-344-3421' 'cats'

It would be helpful to print out a more descriptive error message for these cases, rather than having Python print out a confusing message (or nothing at all).

For a start, we can add `print` statements and then `quit` when our program is given bad arguments:

    :::python
    if __name__ == '__main__':
        args = sys.argv[:]
        script = args.pop(0)    # name of script is first arg
        if not args:
            print "Not enough arguments"
            quit()
        command = args.pop(0)   # the next arg will be the main command

Here, we take advantage of an empty list being `False`y. If there are no arguments left in `args` after we `pop` off the script name, `not args` will evaluate to `True`, and we'll `print` an error message and `quit`. Otherwise we can move on with our program.

Similarly, we can add a check that we're given the correct number of arguments for the `create` command:

    :::python
    if command == 'create':
        if len(args) != 1:
            print "Phonebook name required"
            quit()
        phonebook_name = args.pop(0)
        create_phonebook(phonebook_name)

Add similar checks for each of the commands. Make your program `print` error messages and `quit` any time:

* there aren't enough arguments
* there are too many arguments
* an argument given is invalid

Doing checks based on the `len` of `args` is considered bad Python style. It's usually better to put code in `try`/`except` clauses. Similarly, when we write tests, we're going to want to `raise` exceptions rather than just `print`ing and `quit`ing. But for now, this will do.

Your program should now support the following:

    :::console
    $ python phonebook.py
    Command required
    $ python phonebook.py cats
    Invalid command
    $ python phonebook.py add
    Name, number, and phonebook name required
    $ python phonebook.py add 'Jane Doe'
    Name, number, and phonebook name required
    $ python phonebook.py add 'Jane Doe' '234-234-2334'
    Name, number, and phonebook name required
    $ python phonebook.py add 'Jane Doe' '234-234-2334' 'ex_phonebook'
    $ python phonebook.py add 'Jane Doe' '234-234-2334' 'ex_phonebook' 'cats'
    Name, number, and phonebook name required

Similarly, try giving the other commands (`update`, `remove`, `lookup`, and `reverse-lookup`) too few and too many arguments. You want to make sure that the behavior that you expect is what actually happens.

[Back to top](#top)

## *3.5 More Ideas

If this section hasn't challenged you enough, here are some things you could work on that might be more interesting for you:

* Parse the commands using a module like `argparse`
* `raise` exceptions instead of `print`ing error messages when the user gives bad input
* Even better, `raise` exceptions *and* `print` human-readable, helpful error messages when the user gives bad input
* Practice test-driven development! Try writing a test for what should happen for a possible input (good or bad), run the test and watch it fail, and then work on your code until the test passes. Then repeat.

[Back to top](#top)

# 4. Data Storage

Now that we have a skeleton of functions for each of our commands, and we call the appropriate functions for each command with the appropriate arguments, we need to figure out how to store and access our phonebook entries. First we'll start with saving these entries to a file, and reading them into a dictionary data structure. A more advanced option would be to save the data in a database.

## 4.1 Creating a Phonebook

Let's work on the `create_phonebook` function. This function should create a new text file in the working directory.

We can create a file by `open`ing a file in write mode:

    :::python
    f = open('filename.txt', 'w')

The `'w'` parameter designates write mode. There is also read mode and append mode, both of which we'll use later.

Any time you `open` a file you must remember to `close` it, or your changes won't be saved!

    :::python
    f = open('filename.txt', 'w')
    f.close()

Since it's easy to forget to `close` a file, it's best practice to instead `open` files using the `with` statement:

    :::python
    with open('filename.txt', 'w') as f:
        # do things with f
        pass

`with` automatically `close`s the file for you, so you don't have to remember.

Let's use this to fill out our `create_phonebook` function, which should execute with the `create` command:

    :::python
    def create_phonebook(phonebook_name):
        with open('%s.txt' % phonebook_name, 'w') as f:
            pass

The syntax `'%s.txt' % phonebook_name` is called string interpolation. The variable on the right side of the `%` gets substituted for the `%s` inside the string. This will create files with names like `phonebook.txt` or `ex_phonebook.txt`.

We just `pass` because we don't need to write anything to the file at this point.

Now let's see what happens when we use our program to `create` a phonebook:

    :::console
    $ python phonebook.py create 'ex_phonebook'
    $ ls
    ex_phonebook.txt phonebook.py

We should see that a file `ex_phonebook.txt` was created!

Let's say we manually added some entries into our `ex_phonebook.txt` file, and tried creating another phonebook with the same name? Would our data get overwritten? Or would Python throw an error? Let's see!

I'm manually typing some text into `ex_phonebook.txt` using my text editor:

    :::text
    Jane Doe    123-123-1234

Now let's try `create`ing `ex_phonebook` again:

    :::console
    $ python phonebook.py create 'ex_phonebook'

And... oh no! The contents of `ex_phonebook.txt` have been deleted! We don't want our users to accidentally delete the entire contents of their phonebooks this way. Let's rewrite the `create_phonebook` function so that it won't overwrite any existing files.

To check if the file exists, we'll need to use the `os` module. Add this import statement to the top of your `phonebook.py` script:

    :::python
    import os

And then edit the `create_phonebook` function:

    :::python
    def create_phonebook(phonebook_name):
        filename = '%s.txt' % phonebook_name
        if os.path.exists(filename):
            print "That phonebook already exists!"
            quit()
        with open(filename, 'w') as f:
            pass

Now let's check that this works:

    :::console
    $ python phonebook.py create 'ex_phonebook'
    That phonebook already exists!

Sweet!

## 4.2 Adding an Entry

Now that we can `create` phonebooks, let's work on the `add_entry` function.

Recall that we should support adding an entry with the following command:

    :::console
    $ python phonebook.py add 'Jane Doe' '234-234-2334' 'ex_phonebook'

For now, adding an entry will mean adding a line to the phonebook.

To add a line to a file, we'll need to `open` the file in append mode:

    :::python
    def add_entry(name, number, phonebook_name):
        with open(filename, 'a') as f:
            f.write('%s\t%s' % (name, number))
            f.write('\n')   # add newline

`'%s\t%s' % (name, number)` is another example of string interpolation. This will substitute the first item in the tuple after the `%` for the first `%s` and the second item in the tuple for the second `%s`. The `\t` in the middle is the symbol for a tab. So our entries will be stored in a tab-delimited format.

Let's try adding a couple entries:

    :::console
    $ python phonebook.py add 'Jane Doe' '234-234-2334' 'ex_phonebook'
    $ python phonebook.py add 'John Doe' '789-234-4567' 'ex_phonebook'

Now the `ex_phonebook.txt` file should look like:

    :::text
    Jane Doe    234-234-2334
    John Doe    789-234-4567

There are plenty of things we should do to make this `add_entry` function better, like

* check for duplicate entries
* make sure the given phonebook name exists

But for now let's move on. We can come back to these if we want.

## 4.3 Looking up an Entry by Name

Now, let's work on the `lookup_name` function. We want to read the contents of a phonebook file, and print out the matching entries, if there are any. There are so many ways to do this!

We'll need to `open` a file in read mode, and then iterate through each line of the file. We can do that with:

    :::python
    def lookup_name(name, phonebook_name):
        filename = '%s.txt' % phonebook_name
        with open(filename, 'r') as f:      # 'r' for read mode
            for line in f:
                print line

We'll first just try `print`ing the `line` to see what it looks like:

    :::console
    $ python phonebook.py lookup 'Jane Doe' 'ex_phonebook'
    Jane Doe    234-234-2334

    John Doe    789-234-4567

Hmm. This doesn't give us much information. We can use the function `repr` to tell us the actual representation of the lines:

    :::python
    def lookup_name(name, phonebook_name):
        filename = '%s.txt' % phonebook_name
        with open(filename, 'r') as f:
            for line in f:
                print repr(line)            # use repr function

After replacing this in our `phonebook.py` file, let's see what the `lookup_name` function prints:

    :::console
    $ python phonebook.py lookup 'Jane Doe' 'ex_phonebook'
    'Jane Doe\t234-234-2334\n'
    'John Doe\t789-234-4567\n'

Okay! That is more illuminating. So for each line, we have a string containing the name, followed by a tab (`\t`), followed by the number, followed by a newline (`\n`).

We need to somehow extract the names from each of these lines so we can compare it to the name we're looking up.

Python has some helpful string methods that we can use here. `rstrip` removes trailing whitespace from a string (`\n` counts as whitespace), and `split` breaks up a string into a list based on the characters of your choosing.

So, for each of these lines, let's `strip` off the whitespace, and `split` the string into a list on the `\t` character:

    :::python
    def lookup_name(name, phonebook_name):
        filename = '%s.txt' % phonebook_name
        with open(filename, 'r') as f:
            for line in f:
                print line.strip().split('\t')      # use string methods

This will `print` the results:

    :::console
    $ python phonebook.py lookup 'Jane Doe' 'ex_phonebook'
    ['Jane Doe', '234-234-2334']
    ['John Doe', '789-234-4567']

Great! Now we need to see if the name of the entry is the same as the name we're looking up, and only `print` the names that match:

    :::python
    def lookup_name(name, phonebook_name):
        filename = '%s.txt' % phonebook_name
        with open(filename, 'r') as f:
            for line in f:
                entry_name, entry_number = line.strip().split('\t')
                if entry_name == name:
                    print entry_name, entry_number

Now when we run our program:

    :::console
    $ python phonebook.py lookup 'Jane Doe' 'ex_phonebook'
    Jane Doe 234-234-2334

Great! Now it only prints matches. When we write tests for this function, we'll want to `return` the matches, rather than just `print`ing them, but for now this will do.

## 4.4 Other Functionality

Now we can create phonebooks, add entries, and look up existing entries by name. How could we remove a name? Update a name? Look up a name by phone number? Try writing these functions on your own.

I'll give you a hint: deleting a line from a file isn't very straightforward. Instead, you'll need to save the lines you want to keep in a list, remove the old contents of the file by opening it in write mode, and then write the lines you saved in the list to the file.

## *4.5 More Ideas

If this section hasn't challenged you enough, here are some things you could work on that might be more interesting for you:

* Enable partial string matching using either string methods or regular expressions (using the `re` module). i.e. make this work:


        :::console
        $ python phonebook.py lookup 'Jane' ex_phonebook
        Jane Doe    432 123 4321
        Jane Lin    643 357 9876

* Store the phonebook entries in a database! Some common Python modules that help you interact with databases are `sqlite3` and `sqlalchemy`.
* Store the phonebook entries as dictionaries using the `pickle` module!

# 5. Writing Tests

This part isn't finished yet! If you get to this point, let me know, and I can do a demo!

## 5.1 A Basic Test

## 5.2 A `tests.py` Script

## 5.3 Testing Bad Input

Let's say we wanted to test that running our program with the command

    :::console
    $ python phonebook.py create

(which is missing an argument for the phonebook name) causes an error. How would we do that? Well, we could manually type in the command and observe the results. But would we want to do that with every command variation? And for too many arguments as well as too few? That quickly becomes too many things to remember to test manually.

Thankfully, testing frameworks like Python's `unittest` provide methods that test whether code `raise`s a specific exception.

To make writing tests easier, we can define a custom exception that we'll call `ArgumentError`. To do this we just need to subclass it from the built-in `Exception` class:

    :::python
    class ArgumentError(Exception): pass

Subclassing and class inheritance is out of scope for this exercise, but it's really interesting! I definitely recommend reading about it and playing around with it.

Now to `raise` this exception when an invalid number of arguments is passed:

    :::python
    if command == 'create':
        if args:
            phonebook_name = args.pop(0)
            create_phonebook(phonebook_name)
        else:
            raise ArgumentError("Not enough arguments!")

Now see what happens when you run:

    :::console
    $ python phonebook.py create

You should see an error message like this:

    :::pycon
    Traceback (most recent call last):
      File "phonebook.py", line 25, in <module>
        raise ArgumentError("Not enough arguments!")
    __main__.ArgumentError: Not enough arguments!

Try `raise`ing our `ArgumentError` exception any time a user enters too few or too many arguments.

We should also `raise` an exception if the phone number passed as an argument isn't valid, but we'll do that later when we talk about partial string matching.

[Back to top](#top)

## *5.4 Testing with the `unittest` Module

# Further Reading

## Helpful Modules and Resources

* The [`argparse` module](https://docs.python.org/dev/library/argparse.html) for building a powerful command line argument parser
* The [`re` module](https://docs.python.org/2/library/re.html) for Regular Expressions
* [Dive Into Python](http://www.diveintopython3.net/) for generally learning about Python

<a name="__name__"></a>
## The `__name__` Variable

Why do I have `if __name__ == '__main__':` in the above code snippet?

Suppose someone (maybe you) wanted to `import` this `phonebook.py` script into another program. Maybe you want to do this so you could write tests for the program (which we'll cover later), or because you wanted to make a web front-end to the program. You would probably want some code that executes only if the script is executed directly (e.g. by calling `python phonebook.py` on the command line) that is *not* executed when you `import` the script into another Python program.

This is exactly what the `if __name__ == '__main__'` code block is for. `__name__` is a variable whose value will be `__main__` if the script was executed directly (e.g. by `python phonebook.py`) and otherwise will be the name of the module, (e.g. `phonebook`).

To make this a bit more concrete, let's make some example scripts:

First `a.py`:

    :::python
    print "__name__: ", __name__

What happens when we execute `a.py`?

    :::console
    $ python a.py
    __name__:  __main__

`a.py` is fairly straightforward -- we execute the `print` statement, and we see that the value of the variable `__name__` is the string `'__main__'`. `__name__` is a variable that is defined for us automatically in every Python program, and if the program was executed directly, its value is the string `'__main__'`. Great.

Let's define a second script, `b.py`:

    :::python
    import a

And execute `b.py`:

    :::console
    $ python b.py
    __name__:  a

`b.py` is a bit less straightforward. Here we `import a`, which *executes the code that is inside `a.py`*. I'll give a basic overview of what `import` does in a later section.

So the value of `__name__` inside `a` in this context is the string `'a'`, rather than `'__main__'`. This is because the code is being executed by result of an `import` statement, rather than being executed directly.

How could we execute different code when we `import` a script than when we execute the script directly? This is where the `if __name__ == '__main__'` part comes into play. Let's make two more example scripts to explore this.

`c.py`:

    :::python
    if __name__ == '__main__':
        print "c.py was executed directly"
    else:
        print "c.py was imported"

`d.py`:

    :::python
    import c

And let's execute each of these scripts to see what happens:

    :::console
    $ python c.py
    c.py was executed directly

    $ python d.py
    c.py was imported

Viola! So that's what the `if __name__ == '__main__'` statement does. We'll be adding some code that we don't want to execute when we `import phonebook` into this code block.

[Back to top](#top)

## Mapping commands to functions

Having an `if`/`elif` statement for each of our commands is kind of ugly. Instead, try creating a dictionary mapping the commands to their corresponding functions, like this:

    :::python
    command_funcs = {
        'create' : create,  # create is a function defined elsewhere
        'add' : add,
        'update' : update,
        'delete' : delete,
        'lookup' : lookup,
        'reverse-lookup' : reverse_lookup
    }

Having functions as values in a dictionary might be pretty foreign at first, but it can be really useful, as we're about to see!

We can look up the appropriate function for the given command like this:

    :::python
    func = command_funcs[command]

Here the variable `command` is the main command you grabbed from the command line arguments. `func` is the function associated with `command` in the `command_funcs` dictionary we created.

To invoke `func`, we could try:

    :::python
    func()

But we need to figure out how to pass the appropriate arguments to `func`. `func` could be any of `create`, `add`, `update`, `delete`, etc. These functions take varying number of arguments. So how can we pass the correct number of arguments to `func` without a messy `if` statement?

This is where the super awesome `*args` comes in handy. Try reading up on `*args`. Then try figuring out how to use it to pass `func` the rest of the arguments that were given on the command line. Try to figure out how to handle when an incorrect number of arguments is passed.

[Back to top](#top)