import os

path1_files = []
path1 = input("Path 1: ")
os.chdir(path1)
path1_items = os.listdir(os.getcwd())
for item in path1_items:
    if os.path.isfile(item):
        path1_files.append(item)
path2_files = []
path2 = input("Path 2: ")
os.chdir(path2)
path2_items = os.listdir(os.getcwd())
for item in path2_items:
    if os.path.isfile(item):
        path2_files.append(item)

duplicates = []
for item in path1_files:
    if item in path2_files:
        duplicates.append(item)
for item in path2_files:
    if item in path1_files:
        duplicates.append(item)

if len(duplicates) == 0:
    print("No duplicate files")
else:
    print(f"Duplicate files: {set(duplicates)}")
    choice = input("Delete duplicates? (y/n): ")
    if choice == 'y':
        path = input("Select path: ")
        if path == '1':
            filename = input("Filename: ")
            os.remove(os.path.join(path1, filename))
            print("Success! Duplicates deleted")
        elif path == '2':
            filename = input("Filename: ")
            os.remove(os.path.join(path2, filename))
            print("Success! Duplicates deleted")
        else:
            print("Path doesn't exist")
