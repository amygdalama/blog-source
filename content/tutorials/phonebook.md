Title: Phonebook Exercise
Date: 2014-07-14
Author: Amy Hanlon
Slug: phonebook
Status: hidden

Let's make a command line tool for managing phonebook entries!

# Prologue

Depending on your learning style and experience level, you might get through all of these chapters. Or you might just get through the first one. That's okay! The main priority for this exercise is to write a lot of code and understand what the code you're writing does. Don't worry about "finishing", whatever that means.

If you don't understand a phrase or a line of code that I use, try googling it! A huge part of becoming a better programmer is learning how to google things you don't understand. If that doesn't help, ask me! I enjoy explaining things.

Most of the chapters are split up into sections roughly ordered by difficulty level. The more difficult sections are marked as optional. Also, feel free to skip or skim through the sections that cover content you're already familiar with.

# Table of Contents

[TOC]

# 1. Specifications

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


# 2. Planning & Organizing

What are the functions that you'll need for your program? What arguments will each of those functions need? Write a skeleton program that has those functions definitions, but where the functions just `pass`, rather than actually doing anything.

Here is an example skeleton program with a function definition for `create`ing a phonebook. You'll need more functions, too, but this is a start:

    :::python
    def create_phonebook(phonebook_name):
        # placeholder for create_phonebook function
        pass


    if __name__ == '__main__':
        pass

If you don't know why I included an `if __name__ == '__main__'` statement, try googling it! Now is an excellent time to find out.

# 3. Argument parsing

If you don't know how to parse arguments passed to the Python interpreter from the command line, see if you can figure out how to do it by googling. Maybe google "python command line arguments" as a start.

## 3.1 Accessing command line arguments

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

## 3.2 Rolling your own argument parser

For your phonebook application, you might choose to manually parse your arguments, which could look something like this:

    :::python
    # skeleton code from ch2 defining your functions
    # like create_phonebook and add_entry

    if __name__ == '__main__':
        args = sys.argv
        script = args.pop(0)    # name of script is first arg
        command = args.pop(0)   # the next arg will be the main command

        if command == 'create':
            phonebook_name = args.pop(0)
            create_phonebook(phonebook_name)    # create_phonebook function should be defined above

        elif command == 'add':
            name = args.pop(0)
            number = args.pop(0)
            phonebook_name = args.pop(0)
            add_entry(name, number, phonebook_name)     # add_entry function should be defined above

        # define similar elif statements for update, lookup,
        # reverse-lookup, and delete commands

If you're not sure how the `pop` method works, google it!

There are some potential issues with this code. Try to figure out what they are. Try to improve the code.

## *3.3 Level up your argument parser

The argument parser we wrote in section 3.2 wasn't really that great. There's lots of duplicate logic, and it wouldn't be too easy to add or remove a command from our program. Let's try making it better with some more advanced techniques.

#### *3.3.1 Unpack the arguments

Use tuple unpacking to bind variable names to the arguments in one line of code rather than in many lines of code. For example, we can turn this:

    :::python
    name = args.pop(0)
    number = args.pop(0)

into this:

    :::python
    name, number = args

This works even though `args` is a list and not a tuple!

#### *3.3.2 Mapping commands to functions

This section is a bit more advanced than the others. If you've found the previous sections difficult, you might want to skip this one and come back to it later.

Having an `if`/`elif` statement for each command is kind of ugly. Instead, try creating a dictionary mapping the commands to their corresponding functions, like this:

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

# 4. Raising Exceptions

What happens when a user passes an incorrect number of arguments? Try giving your program too few arguments. Now try with too many arguments.

Our users might find it useful for us to `print` descriptive error messages if the number of arguments is incorrect. How could we add this to our progam?

## 4.1 Invalid number of arguments

We could do something like this:

    :::python
    if command == 'create':
        if args:
            phonebook_name = args.pop(0)
            create_phonebook(phonebook_name)
        else:
            print "Not enough arguments!"

Using `print` statements to indicate that an invalid number of arguments were passed is sufficient for now, but will make writing tests difficult.

For example, let's say we wanted to test that running our program with the command

    :::console
    $ python phonebook.py create

(which is missing an argument for the phonebook name) caused an error. How would we do that? Well, we could manually type in the command and observe the results. But would we want to do that with every command variation? And for too many arguments as well as too few? That quickly becomes too many things to remember to test manually.

Thankfully, testing frameworks like Python's `unittest` provide methods that test whether code `raise`s a specific exception. We'll cover more on testing and using `unittest` in the next chapter.

To make writing tests easier, we can define a custom exception that we'll call `ArgumentError`. To do this we just need to subclass it from the built-in `Exception` class:

    :::python
    class ArgumentError(Exception): pass

Subclassing isn't particularly important to understand for this exercise, but is definitely important to understand in other contexts. I won't cover it here.

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

# 5. Writing Tests

# 6. Data Persistence

# 7. Partial String Matching

# 8. Further Reading

# Appendix

## Subclasses (possible)

## Further Reading

* The `argparse` module