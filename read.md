Project: PDFOS
Stage: Initial CLI + Virtual Filesystem Research

What I worked on:

Started the PDFOS project in VS Code.
Created the initial main.py.
Created a basic CLI using Python.
Learned how print() displays information.
Learned how input() receives and stores user input.
Implemented if, elif, and else for command handling.
Used while to keep the CLI running.
Used break to terminate the CLI with the exit command.
Used .lower() to make commands case-insensitive.
Created functions for individual commands such as hello() and help_command().
Started designing the PDFOS virtual filesystem.
Learned how Python dictionaries can represent directories and nested directories.
Created filesystem_test.py to experiment with the virtual filesystem separately from the main program.
Learned how .keys() can be used to retrieve the contents of a directory represented by a dictionary.

Current working CLI:

PDFOS v0.1


PDFOS v0.1> hello
Hello from PDFOS!


PDFOS v0.1> help
Available commands:
hello
help
exit


PDFOS v0.1> exit
goodbye!!

Current virtual filesystem concept:

/
├── home
│   └── user
├── bin
└── tmp

Important concepts learned:

Variables
Strings
input()
print()
Conditions
Loops
Functions
Dictionaries
Nested dictionaries
Directory hierarchy
Virtual filesystem concept

Current understanding:

PDFOS currently has a basic command-line shell. The filesystem is still only a Python data structure and is not yet connected to the main PDFOS CLI. The next objective is to develop the ls command and connect it to the virtual filesystem.
