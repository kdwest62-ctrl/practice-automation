import os
import shutil

dir1_path = input("Directory 1 path: ")
if os.path.exists(dir1_path):

    def get_files(dir_path):
        files = []
        items = os.listdir(dir_path)
        for a in items:
            file_path = os.path.join(dir_path, a)
            files.append(file_path)
        return tuple(files)

    def sync(dir1, dir_path, dir_files):
        for b in dir1:
            if b not in dir_files:
                shutil.copy2(b, dir_path)

    dir1_files = get_files(dir1_path)

    paths = []
    total = int(input("Number of directories to sync with original directory: "))
    if total > 0:
        count = 0
        while count < total:
            path = input(f"Directory path: ")
            if os.path.exists(path):
                paths.append(path)
                count += 1
            else:
                print("Path not found")

        paths_files = []
        for item in paths:
            path_files = get_files(item)
            paths_files.append(path_files)

        dict1 = dict(zip(paths, paths_files))

        for key, value in dict1.items():
            if value != dir1_files:
                sync(dir1_files, key, value)

        print("Success! Directories synced")

else:
    print("Path not found")
