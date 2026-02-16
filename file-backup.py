import os
import shutil
from pathlib import Path

try:
    src_path = input("Source path: ")
    if os.path.exists(src_path):

        file_extensions = []
        items = os.listdir(src_path)
        for item in items:
            file_path = os.path.join(src_path, item)
            if os.path.isfile(file_path):
                x = Path(file_path)
                file_extensions.append(x.suffix)
        print(set(file_extensions))

        extensions_list = []
        total_ext = int(input("Number of file extensions to backup: "))
        if total_ext != 0:
            ext_count = 1
            while ext_count <= total_ext:
                extension = input(f"File extension {ext_count} name: ")
                if extension not in file_extensions:
                    print("File extension not found. Try again")
                else:
                    extensions_list.append(extension)
                    ext_count += 1

        dst_path = input("Destination path: ")

        dirs_list = []
        total_dirs = int(input("Number of directories to create: "))
        if total_dirs != 0:
            dir_count = 1
            while dir_count <= total_dirs:
                dir_name= input(f"Directory {dir_count} name: ")
                os.mkdir(os.path.join(dst_path, dir_name))
                dirs_list.append(dir_name)
                dir_count += 1

            destinations_list = []
            print(dirs_list)
            for item in extensions_list:
                destination = input(f"Directory for {item}: ")
                if destination not in dirs_list:
                    print("Directory not available")
                else:
                    destinations_list.append(destination)
            organizer = dict(zip(extensions_list, destinations_list))

            if len(organizer.values()) != 0:
                items = os.listdir(src_path)
                for item in items:
                    file_path = os.path.join(src_path, item)
                    if os.path.isfile(file_path):
                        a = Path(file_path)
                        if a.suffix in organizer.keys():
                            shutil.copy2(file_path, os.path.join(dst_path, organizer[a.suffix]))

                dirs_files = []
                for item in dirs_list:
                    length = len(os.listdir(os.path.join(dst_path, item)))
                    dirs_files.append(length)
                files_count = dict(zip(dirs_list, dirs_files))
                for key, value in files_count.items():
                    print(f"Files copied to {key}: {value}")

                compress = input("Compress directory? (y/n): ")
                if compress == 'y':
                    print(dirs_list)
                    name = input("Directory name: ")
                    if name in dirs_list:
                        archive_name = input("Archive name: ")
                        archive = os.path.join(dst_path, archive_name)
                        shutil.make_archive(archive, 'zip', os.path.join(dst_path, name))
                        print(f"Success! Directory {name} compressed")
                    else:
                        print("Directory not found")
    else:
        print("Path not found")
except FileExistsError:
    print("Directory already exists")
except FileNotFoundError:
    print("Path not found")
except ValueError:
    print("Please input a number")
