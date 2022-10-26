

with open("a_file.txt") as file:
    file.read()
    #prints: FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt' BECAUSE there is no file named a_file.txt and it cannot make a new file as default mode is READ **