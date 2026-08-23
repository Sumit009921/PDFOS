# PDFOS — Development Documentation

## 1. Project Overview

PDFOS is a research project exploring the development of a virtual operating environment associated with a PDF.

The project is being developed in Python.

The current implementation is not a real operating-system kernel. It is a user-space virtual environment that currently provides:

- Command-line interaction
- Virtual filesystem
- Directory navigation
- Absolute and relative paths
- Basic command handling
- Filesystem state

The project will be developed in layers. Each layer will be implemented, tested, understood, and then used as the foundation for the next layer.

Current development path:

    CLI
     ↓
    Virtual Filesystem
     ↓
    File and Directory Operations
     ↓
    Command Parser
     ↓
    Persistence
     ↓
    Runtime
     ↓
    PDF Integration

---

# 2. Current Version

Version: v0.1

v0.1 establishes the first working PDFOS environment.

Current files:

    PDFOS/
    ├── README.md
    ├── main.py
    ├── filesystem.py
    └── read.md

---

# 3. Running the Project

Python 3 is required.

No external Python packages are required for the current version.

From the project directory:

    py main.py

The program starts with:

    PDFOS v0.1
    PDFOS:/>

The shell then waits for commands.

---

# 4. Current Commands

The current shell supports:

    hello
    help
    ls
    cd
    exit

---

# 5. main.py

`main.py` is the entry point of PDFOS.

Its responsibilities are:

- Starting the shell
- Displaying the PDFOS version
- Receiving user input
- Recognizing commands
- Passing filesystem operations to `filesystem.py`
- Displaying command output
- Maintaining the shell loop

The shell currently uses an `if / elif` command-dispatch structure.

The current architecture is:

    User
      ↓
    main.py
      ↓
    Command
      ↓
    filesystem.py
      ↓
    Virtual Filesystem

The shell does not directly manipulate the internal filesystem tree.

---

# 6. hello Command

The `hello` command is implemented as:

    def hello():
        print("Hello from PDFOS!")

It is mainly a basic command used to verify that the command loop and function execution are working.

---

# 7. help Command

The `help` command displays the currently available commands.

Current output:

    Available commands:
    hello
    help
    ls
    cd
    exit

Whenever a new permanent shell command is added, the help system should eventually be updated.

---

# 8. ls Command

`ls` lists the contents of the current virtual directory.

Example:

    PDFOS:/> ls

Current output:

    home
    bin
    tmp

`main.py` receives the command and calls:

    filesystem.ls()

The filesystem module is responsible for determining what exists in the current directory.

The flow is:

    ls
     ↓
    filesystem.ls()
     ↓
    get_directory(current_directory)
     ↓
    list directory entries

---

# 9. cd Command

`cd` changes the current virtual directory.

Examples:

    cd /home

    cd home

    cd user

The first example is an absolute path.

The second and third examples are relative paths.

The command is parsed using:

    command.split()

For:

    cd /home

the result is:

    ["cd", "/home"]

Therefore:

    parts[0] = "cd"
    parts[1] = "/home"

The path is then passed to:

    filesystem.change_directory(parts[1])

---

# 10. Virtual Filesystem

The initial virtual filesystem is represented using a nested Python dictionary.

Current structure:

    root = {
        "home": {
            "user": {}
        },
        "bin": {},
        "tmp": {}
    }

This represents:

    /
    ├── home
    │   └── user
    ├── bin
    └── tmp

The filesystem exists inside Python memory.

It is not the actual filesystem of the computer running PDFOS.

---

# 11. Why a Dictionary Was Used

The dictionary was chosen because a filesystem is naturally hierarchical.

A dictionary provides a simple:

    name → object

relationship.

For example:

    {
        "home": {...},
        "bin": {},
        "tmp": {}
    }

The keys represent filesystem entry names.

Nested dictionaries represent children.

Therefore:

    root
     ├── home
     │    └── user
     ├── bin
     └── tmp

can be represented directly using nested dictionaries.

The main reason
