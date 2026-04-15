import os
import shutil

try:
    path = input("Directory path: ")
    if os.path.exists(path):
        def convert(num):
            return num / (1024 ** 2)

        items = os.listdir(path)
        if len(items) > 0:
            files = []
            sizes = []
            for item in items:
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
                    if max_size > min_size:
                        for size, file in files_with_sizes.items():
                            if min_size <= size <= max_size:
                                shutil.move(file, dir_path)
                                print(f"{file} moved to {name}")
                        count += 1
                    else:
                        print("Minimum cannot be greater than maximum")
        else:
            print("No files in path")
    else:
        print("Path not found")
except FileExistsError:
    print("Directory already exists")
except ValueError:
    print("Invalid input")
