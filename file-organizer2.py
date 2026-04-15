import os
import shutil

try:
    path = input("Directory path: ")
    if os.path.exists(path):
        def convert(num):
            result = num / (1024 ** 2)
            return round(result, 2)

        files = []
        sizes = []
        for item in os.listdir(path):
            file = os.path.join(path, item)
            if os.path.isfile(file):
                files.append(file)
                sizes.append(convert(os.path.getsize(file)))
        files_with_sizes = dict(zip(sizes, files))

        total = int(input("Number of directories to create: "))
        if total > 0:
            count = 1
            while count <= total:
                name = input(f"Directory {count} name: ")
                dir_path = os.path.join(path, name)
                os.mkdir(dir_path)
                min_size = float(input("Min file size (mb): "))
                max_size = float(input("Max file size (mb): "))
                for size, file in files_with_sizes.items():
                    if min_size <= size <= max_size:
                        shutil.move(file, dir_path)
                        print(f"{file} moved to {name}")
                count += 1
    else:
        print("Path not found")
except FileExistsError:
    print("Directory already exists")
