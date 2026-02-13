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
        index = 0
        while True:
            for item in list1:
                path = Path(item)
                if path.name == list3[index]:
                    list4.append(item)
            index += 1
            if index >= len(set(list3)):
                break
        keys = []
        num = 0
        while num != len(list4):
            num += 1
            keys.append(num)

        dict1 = dict(zip(keys, list4))
        for key, value in dict1.items():
            print(key, value)

        remove = input("Remove duplicates? (y/n): ")
        if remove == 'y':
            total = int(input("Number of duplicates to remove: "))
            if total <= len(list4) and total != 0:
                count = 1
                while count <= total:
                    remove_path = input(f"Remove path {count}: ")
                    if remove_path in list4:
                        os.remove(remove_path)
                        count += 1
                    else:
                        print("Path not in list")
                print("Success! Duplicates removed")
else:
    print("Path not found")
