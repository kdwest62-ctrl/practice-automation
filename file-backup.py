import os
import shutil

dst = input("Destination path: ")
os.chdir(dst)
dir_name = input("Directory name: ")
dst_dir = os.path.join(dst, dir_name)
if not os.path.isdir(dst_dir):
    os.mkdir(dst_dir)

src = input("Source path: ")
os.chdir(src)
extension = input("File extension: ")
count = 0
items = os.listdir(os.getcwd())
for item in items:
    if os.path.isfile(item):
        if item.endswith(extension):
            shutil.copy(item, dst_dir)
            count += 1
print(f"{count} files copied")
