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

[Back to top](#top)

## 2.1 The `__name__` Variable

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
2. What happens to `sys.argv` if we `pop` elements off `args`?
3. What happens to `sys.argv` if we set `args` equal to `sys.argv` rather than `sys.argv[:]`?

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

What happens if your program is given arguments that aren't supported? For example, try typing:

    :::console
    $ python phonebook.py cats

What about if you try `add`ing a phone number, but you only give it a name, and not a number?

    :::console
    $ python phonebook.py add 'Jane Doe'

What about if you give it a name, number, and an extra nonsensical argument?

    :::console
    $ python phonebook.py add 'Jane Doe' '765-344-3421' 'cats'

It would be helpful to print out an error message for situations like this.

[Back to top](#top)

## *3.5 Mapping commands to functions

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

[Back to top](#top)

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

We should also `raise` an exception if the phone number passed as an argument isn't valid, but we'll do that later when we talk about partial string matching.

[Back to top](#top)

# 5. Writing Tests

## 5.1 A Basic Test

## 5.2 A `tests.py` Script

## *5.3 Testing with the `unittest` Module

# 6. Data Storage

# 7. Partial String Matching

## 7.1 `string` Methods

#### 7.1.1 Matching Partial Names

#### 7.1.2 Validating Phone Numbers

## *7.2 Regular Expressions

#### *7.2.1 Matching Partial Names

#### *7.2.2 Validating Phone Numbers

# 8. Further Reading

# Appendix

## Subclasses (possible)

## Further Reading

* The `argparse` module