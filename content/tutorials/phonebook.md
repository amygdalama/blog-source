Title: Phonebook Exercise
Date: 2014-07-14
Author: Amy Hanlon
Slug: phonebook
Status: hidden

Let's make a command line tool for managing phonebook entries!

# Specifications

We'll make a [CRUD](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete) application that will support creating, retrieving, updating, and deleting phonebook entries consisting of a name and a phone number.

The application will have a command line interface supporting the following commands and behaviors:

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


# About this exercise

This exercise can be organized into the following sections:

* planning & organizing
* argument parsing
* data persistence
* partial string matching
* writing tests

Depending on your learning style and experience level, you might get through all of these sections. Or you might just get through the first one. That's okay! The main priority for this exercise is to write a lot of code and understand what the code you're writing does. Don't worry about "finishing", whatever that means.

If you don't understand a phrase or a line of code that I use, try googling it! A huge part of becoming a better programmer is learning how to google things you don't understand. If that doesn't help, ask me! I enjoy explaining things.

Most of the sections are split up into different methods by experience level. You can work on this exercise in a number of different ways, including:

* for each section, choose one method to complete, and then move on to the next section
* for each section, begin at the first method and then refactor your code as you level up to more advanced methods

Both of these strategies (or anything in between) will work well. Do whichever you think works best with your learning style and current experience level. With the first strategy, you'll be more likely to end up with a completed product. With the second strategy, you'll be more likely to end up with thorough understanding of a couple sections.


# Part I: Planning & Organizing

What are the functions that you'll need for your program? What arguments will each of those functions need? Write a skeleton program that has those functions definitions, but where the functions just `pass`, rather than actually doing anything.

Here is an example skeleton program with a function definition for `create`ing a phonebook. You'll need more functions, too, but this is a start:

    :::python
    def create_phonebook(phonebook_name):
        # placeholder for create_phonebook function
        pass


    if __name__ == '__main__':
        pass

If you don't know why I included an `if __name__ == '__main__'` statement, try googling it! Now is an excellent time to find out.

# Part II: Argument parsing

If you don't know how to parse arguments passed to the Python interpreter from the command line, see if you can figure out how to do it by googling. Maybe google "python command line arguments" as a start.

If you already know a bit about argument parsing, and want to learn about a Python module that helps with more advanced argument parsing, skip to the "Using the `argparse` module" section.

## Intro to argument parsing

Arguments passed to Python scripts from the command line are accessible using the `sys` module. Here's a simple example script that prints out the arguments passed to the Python interpreter:

    :::python
    # ex.py
    import sys

    print "The arguments given to the interpreter are: "
    print sys.argv

What happens when you execute the script giving it some arguments?

    :::console
    $ python ex.py red flowers hi
    The arguments given to the interpreter are:
    ['ex.py', 'red', 'flowers', 'hi']

So `sys.argv` is a list, containing the name of the script (`'ex.py'`), and then the three arguments we passed, all represented as strings.

## Rolling your own argument parser

For your phonebook application, you might choose to manually parse your arguments, which could look something like this:

    :::python
    import sys


    def create_phonebook(phonebook_name):
        # placeholder for create_phonebook function
        pass


    def add_entry(name, number, phonebook_name):
        # placeholder for add_entry function
        pass


    if __name__ == '__main__':
        args = sys.argv
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

        # define similar elif statements for update, lookup,
        # reverse-lookup, and delete commands

If you're not sure how the `pop` method works, google it!

There are some potential issues with this code. Try to figure out what they are. Try to improve the code.

## Level up your argument parser

Here are some optional things you could do to make your argument parsing better:

#### Unpack the arguments

Use tuple unpacking to bind variable names to the arguments in one line of code rather than in many lines of code:

    :::python
    `name, number = args`

#### Error handling

What happens when a user passes an incorrect number of arguments? Try giving your program too few arguments. Now try with too many arguments.

It might be useful for your users to `raise` or `print` descriptive error messages if the number of arguments is incorrect. How could you add this to your program?

If you don't know how to `raise` exceptions and you want to learn, now is a great time! google it!

#### Mapping commands to functions

This section is a bit more advanced than the others. Feel free to skip it!

Having an `if`/`elif` statement for each command is kind of ugly. Try creating a dictionary mapping the commands to their corresponding functions, like this:

    :::python
    command_funcs = {
        'create' : create,  # create is a function defined elsewhere
        'add' : add,
        'update' : update,
        'delete' : delete,
        'lookup' : lookup,
        'reverse-lookup' : reverse_lookup
    }

Then, you could look up the appropriate function for the given command like this:

    :::python
    func = command_funcs[command]

Here the variable `command` is the main command you grabbed from the command line arguments.

Having functions be values in a dictionary might be pretty foreign to you. But it can be really useful!

Now we need to figure out

 and the variable `args`, which should be a `list` of all the other arguments after the main command.

Not sure how


## Using the `argparse` module