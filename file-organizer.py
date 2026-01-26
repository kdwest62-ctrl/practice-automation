import os
import shutil

def file_extension(filename):
    filename_split = filename.split('.')
    return filename_split[-1]

# input desired path
path = input("Path: ")
os.chdir(path)

# input number of directories to create + their names
dirs_list = []
total_dirs = int(input("Number of directories to create: "))
dir_count = 1
while dir_count <= total_dirs:
    dir_name= input(f"Directory {dir_count} name: ")
    os.mkdir(dir_name)
    dirs_list.append(dir_name)
    dir_count += 1

# program prints file extension/s located in path
draft_list = []
items = os.listdir(os.getcwd())
for item in items:
    if os.path.isfile(item):
        draft_list.append(file_extension(item))
file_extensions = set(draft_list)
print(file_extensions)

# user chooses the file extension/s to organize
extensions_list = []
print(f"File extensions inside the path: {len(file_extensions)}")
total_ext = int(input("Number of file extensions to organize: "))
ext_count = 1
while ext_count <= total_ext:
    extension = input(f"File extension {ext_count} name: ")
    if extension not in file_extensions:
        print("File extension not found. Try again")
    else:
        extensions_list.append(extension)
        ext_count += 1

# user chooses which directories the file extension/s go
destinations_list = []
print(f"Directories: {dirs_list}")
for item in extensions_list:
    destination = input(f"Directory for {item}: ")
    if destination not in dirs_list:
        print("Directory not available")
    else:
        destinations_list.append(destination)
blueprint = dict(zip(extensions_list, destinations_list))

# main process
if len(blueprint.values()) != 0:
    items = os.listdir(os.getcwd())
    for item in items:
        if os.path.isfile(item):
            if file_extension(item) in blueprint.keys():
                shutil.move(item, os.path.join(os.getcwd(), blueprint[file_extension(item)]))

# feedback
    print("File organization successful")
