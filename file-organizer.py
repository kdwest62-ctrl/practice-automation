import os
import shutil

path = input("Path: ")
os.chdir(path)

folder1 = input("Folder 1: ")
if not os.path.isdir(folder1):
    os.mkdir(folder1)
folder2 = input("Folder 2: ")
if not os.path.isdir(folder2):
    os.mkdir(folder2)

exe_count = 0
jpg_count = 0
downloads = os.listdir(os.getcwd())
for item in downloads:
    if os.path.isfile(item):
        if item.lower().endswith('.exe'):
            shutil.move(item, os.path.join(os.getcwd(), folder1))
            exe_count += 1
        elif item.lower().endswith('.jpg'):
            shutil.move(item, os.path.join(os.getcwd(), folder2))
            jpg_count += 1
        else:
            continue
print(f"Success! {folder1}: {exe_count} files, {folder2}: {jpg_count} files")
