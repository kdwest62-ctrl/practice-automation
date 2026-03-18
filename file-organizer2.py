import os
import shutil

try:
    path = input("Directory path: ")
    if os.path.exists(path):
        def convert(num):
            result = num / (1024 ** 2)
            return round(result, 2)

        small_min = int(input("Small min (mb): "))
        small_max = int(input("Small max (mb): "))
        medium_min = int(input("Medium min (mb): "))
        medium_max = int(input("Medium max (mb): "))
        large_min = int(input("Large min (mb): "))
        large_max = int(input("Large max (mb): "))

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
            if small_min < dict1[item] <= small_max:
                shutil.move(item, small)
            elif medium_min < dict1[item] <= medium_max:
                shutil.move(item, medium)
            elif large_min < dict1[item] <= large_max:
                shutil.move(item, large)
        print("Files organized successfully")
    else:
        print("Path not found")
except FileExistsError:
    print("Directory already exists")
