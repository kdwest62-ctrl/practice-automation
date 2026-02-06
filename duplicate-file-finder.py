import os

source = input("Path: ")

files = []
list2 = []
duplicates = []

for _, dirs, filename in os.walk(source):
    for item in dirs:
        if os.path.isfile(item):
            files.append(item)
    for item in filename:
        files.append(item)

for item in files:
    if item not in list2:
        list2.append(item)
    else:
        duplicates.append(item)

if len(duplicates) == 0:
    print("No duplicates")
else:
    for item in duplicates:
        print(item)

    remove = input("Remove duplicates? (y/n): ")
    if remove == 'y':
        total = int(input("Number of duplicates to remove: "))
        if total <= 0 or total > len(duplicates):
            print(f"There are {len(duplicates)} duplicates")
        else:
            count = 1
            while count <= total:
                filename = input(f"Filename {count}: ")
                if filename in duplicates:
                    os.remove(os.path.join(source, filename))
                    count += 1
                else:
                    print("File not a duplicate")
            print(f"Success! {total} duplicates removed")
