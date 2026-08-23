import posixpath
root = {
    "home": {
        "user": {}
    },
    "bin": {},
    "tmp": {}
}

current_directory = "/"


def ls():
    directory = get_directory(current_directory)
    for item in directory.keys():
        print(item)
        
def get_directory(path):
    
    if path == "/":
        return root
    parts = path.split("/")[1:]
    
    current = root
    
    for part in parts:
        current = current[part]
        
    return current

def change_directory(path):
    global current_directory

    if not path.startswith("/"):
        path = posixpath.join(current_directory, path)

    try:
        directory = get_directory(path)
        current_directory = path
    except KeyError:
        print("Directory not found")