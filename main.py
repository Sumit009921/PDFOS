import filesystem
import posixpath

current = "/home"
requested = "user"

new_path = posixpath.join(current, requested)

print(new_path)

print("PDFOS v0.1")


def hello():
    print("Hello from PDFOS!")


def help_command():
    print("Available commands:")
    print("hello")
    print("help")
    print("ls")
    print("cd")
    print("exit")


while True:

    command = input("PDFOS:" + filesystem.current_directory + "> ")

    if command.lower() == "hello":
        hello()

    elif command.lower() == "help":
        help_command()

    elif command.lower() == "ls":
        filesystem.ls()

    elif command.lower().startswith("cd "):
        parts = command.split()
        filesystem.change_directory(parts[1])

    elif command.lower() == "exit":
        print("goodbye!!")
        break

    else:
        print("Unknown command:", command)
        