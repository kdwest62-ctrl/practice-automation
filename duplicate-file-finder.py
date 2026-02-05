import os
from pathlib import Path

source = input("Path: ")
path = Path(source)

files = []
list2 = []
duplicates = []

for _, dirs, filename in os.walk(path):
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
