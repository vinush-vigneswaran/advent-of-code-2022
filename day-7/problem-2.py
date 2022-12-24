class Directory:
    def __init__(self, parent):
        self.parent_directory = parent
        self.child_directories = {}
        self.file_size = 0

    def update_child_file_size(self):
        total_child_file_size = 0

        if len(self.child_directories) < 1:
            return self.file_size

        for k, child_directory in self.child_directories.items():
            child_dir_file_size = child_directory.update_child_file_size()
            total_child_file_size += child_dir_file_size

        return self.file_size + total_child_file_size

    def add_child(self, name, child_directory):
        self.child_directories[name] = child_directory

def list_to_string(lst):
    return '/'.join(lst)


file = "data.txt"
read_file = open(file, 'r')

lines = read_file.readlines()
all_dirs = {}
root_directory = Directory(None)
history = []
listed = False

for line in lines:
    line = line.rstrip('\n')
    line = line.split()

    if (line[0] == "$") and (line[1] == "cd") and (line[2] == "/"):
        listed = False
        current_directory = root_directory
        history.append(line[2])
        all_dirs[list_to_string(history)] = current_directory

    elif (line[0] == "$") and (line[1] == "cd") and (line[2] != ".."):
        listed = False
        _dir = history + [line[2]]
        path = list_to_string(_dir)

        current_directory = current_directory.child_directories[path]
        history.append(line[2])
        all_dirs[list_to_string(history)] = current_directory

    elif (line[0] == "$") and (line[1] == "cd") and (line[2] == ".."):
        listed = False
        current_directory = current_directory.parent_directory
        history.pop()

    elif (line[1] == "ls"):
        listed = True

    elif (line[0] == "dir") and listed:
        _dir = history + [line[1]]
        path = list_to_string(_dir)

        if (path not in current_directory.child_directories.keys()):
            #create child and add to dir dict
            child_directory = Directory(current_directory)
            current_directory.add_child(path, child_directory)
            all_dirs[path] = child_directory

    elif (line[0].isdigit()) and listed:
        current_directory.file_size += int(line[0])

# update file sizes
for k,directory in all_dirs.items():
    directory.file_size = directory.update_child_file_size()

# results
disk_size = 70000000
required_size = 30000000
used_size = all_dirs['/'].file_size
unused_size = disk_size - used_size
space_to_clear = required_size - unused_size

print("disk size= ", disk_size)
print("used= ", used_size)
print("unused= ", unused_size)

print("space needed to clear= ", space_to_clear)

filtered = {k: v.file_size for k, v in all_dirs.items() if v.file_size >= space_to_clear}
filtered = min(filtered.values())

print("remove file with size= ", filtered)