elif command.lower().startswith("cat"):
         parts = command.split()
         filesystem.cat(parts[2]) 