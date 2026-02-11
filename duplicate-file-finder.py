import os
from pathlib import Path

source = input("Source path: ")
if os.path.exists(source):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for root, dirs, files in os.walk(source):
        for item in dirs:
            if os.path.isfile(item):
                a = os.path.join(root, item)
                list1.append(a)
        for item in files:
            a = os.path.join(root, item)
            list1.append(a)

    for item in list1:
        path = Path(item)
        if path.name in list2:
            list3.append(path.name)
        else:
            list2.append(path.name)

    if len(set(list3)) == 0:
        print("No duplicates")
    else:
        while True:
            index = 0
            for item in list1:
                path = Path(item)
                if path.name == list3[index]:
                    list4.append(item)
            index += 1
            if index >= len(set(list3)):
                break
        for item in list4:
            print(item)

else:
    print("Path not found")
