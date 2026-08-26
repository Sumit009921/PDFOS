import posixpath
root = {
    "name": "/",
    "type": "directory",
    "children": {
        "home": {
            "name": "home",
            "type": "directory",
            "children": {
                "user": {
                    "name": "user",
                    "type": "directory",
                    "children": {
                        "hello.txt": {
                            "name": "hello.txt",
                            "type": "file",
                            "content": ""
                        }
                    }
                }
            }
        },
        "bin": {
            "name": "bin",
            "type": "directory",
            "children": {}
        },
        "tmp": {
            "name": "tmp",
            "type": "directory",
            "children": {}
        }
    }
}


current_directory = "/"


def ls():
    directory = get_directory(current_directory)
    
    for item in directory["children"].keys():
        print(item)

def touch(filename):
    directory = get_directory(current_directory) 
    
    children = directory["children"]
    file = {
        "name": filename,
        "type": "file",
        "content": "" 
    }
    children[filename] = file
        
def get_directory(path):
    
    if path == "/":
        return root
    parts = path.split("/")[1:]
    
    current = root
    
    for part in parts:
        current = current["children"][part]
        
    return current

def change_directory(path):
    global current_directory

    if not path.startswith("/"):
        path = posixpath.join(current_directory, path)

    try:
        directory = get_directory(path)
        if(directory["type"] == "file"):
            print("cannot change the directory")
            return 
        else:
            current_directory = path
            
        current_directory = path
    except KeyError:
        print("Directory not found")