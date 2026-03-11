import os
import shutil

path = input("Path: ")
if os.path.exists(path):
    items = os.listdir(path)
    files = []
    for item in items:
        file = os.path.join(path, item)
        files.append(file)

    for file in files:
        if os.path.isdir(file):
            print(file)

    dir_to_archive = input("Dir to archive: ")
    archive_name = input("Archive name: ")
    dst_path = input("Destination path: ")
    src = os.path.join(path, dir_to_archive)
    dst = os.path.join(dst_path, archive_name)
    shutil.make_archive(dst, 'zip', src)
    print(f"{dir_to_archive} archived as {archive_name}")

else:
    print("Path not found")
