import os
import shutil

path = input("Directory path: ")
if os.path.exists(path):
    def convert(num):
        result = num / (1024 ** 2)
        return round(result, 2)

    small = os.path.join(path, 'Small')
    medium = os.path.join(path, 'Medium')
    large = os.path.join(path, 'Large')
    os.mkdir(small)
    os.mkdir(medium)
    os.mkdir(large)

    files = []
    items = os.listdir(path)
    for item in items:
        file = os.path.join(path, item)
        if os.path.isfile(file):
            files.append(file)

    sizes = []
    for x in files:
        a = os.path.getsize(x)
        sizes.append(convert(a))

    dict1 = dict(zip(files, sizes))
    for item in dict1.keys():
        if 0 < dict1[item] <= 2:
            shutil.move(item, small)
        elif 2 < dict1[item] <= 10:
            shutil.move(item, medium)
        else:
            shutil.move(item, large)
    print("Files organized successfully")
else:
    print("Path not found")
