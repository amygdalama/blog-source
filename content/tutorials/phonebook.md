Title: Phonebook Tutorial
Date: 2014-07-14
Author: Amy Hanlon
Slug: phonebook
Status: hidden

Let's make a command line tool for managing phonebook entries!

## What it should do

We'll make a [CRUD](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete) application that should support creating, retrieving, updating, and deleting phonebook entries consisting of a name and a phone number.

The application will have a command line interface. The program should support the following commands:

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


## Things we'll (maybe) learn about

There are many different approaches to solving this problem. Depending on the approach you choose and your experience level, you'll have the opportunity to learn about:

* argument parsing
* data structures that allow fast lookup
* looking through strings for matches
* writing tests
* using a database

## How to read this tutorial



## Argument parsing

If you don't know how to parse arguments passed to the Python interpreter from the command line, see if you can figure out how to do it by googling. Maybe google "python command line arguments" as a start.

#### Intro to argument parsing

Arguments passed to python scripts from the command line are accessible using the sys module. Here's a simple example script that prints out the arguments passed to the Python interpreter:

    :::python
    # ex.py
    import sys

    print "The arguments given to the script are: "
    print sys.argv

What happens when you execute the script giving it some arguments?

    :::console
    $ python ex.py red flowers hi
    The arguments given to the script are:
    ['ex.py', 'red', 'flowers', 'hi']

So `sys.argv` is a list, containing the name of the python script (`'ex.py'`), and then the three arguments we passed, all represented as strings.

#### Rolling your own argument parser

For your phonebook application, you might choose to manually parse your arguments. This would look something like this:

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

If you're not sure how the `pop` method works or why I have the `if __name__ == '__main__'` statement, google it! A huge part of becoming a better programmer is learning how to google things you don't understand.

There are some potential issues with this code. Try to figure out what they are. Try to improve the code.

Things you could try:

* unpack the arguments
    * `name, number = args`
* error handling
    * `raise` or `print` error messages if the number of arguments is incorrect
    * if you don't know how to `raise` exceptions and you want to learn, now is a great time! google it!
* map the commands to their

#### Using the `argparse` module