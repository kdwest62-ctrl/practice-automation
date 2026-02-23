import shutil
from pathlib import Path

try:
    src_path = Path(input("Source path: "))
    if src_path.exists():
        file_extensions = []
        items = src_path.iterdir()
        for item in items:
            if item.is_file():
                file_extensions.append(item.suffix)
        print(set(file_extensions))

        extensions_list = []
        total_ext = int(input("Number of file extensions to backup: "))
        if total_ext != 0:
            ext_count = 1
            while ext_count <= total_ext:
                extension = input(f"File extension {ext_count} name: ")
                if extension in file_extensions:
                    extensions_list.append(extension)
                    ext_count += 1
                else:
                    print("File extension not found. Try again")

        dst_path = Path(input("Destination path: "))
        if dst_path.exists():
            dirs_list = []
            total_dirs = int(input("Number of directories to create: "))
            if total_dirs != 0:
                dir_count = 1
                while dir_count <= total_dirs:
                    dir_name= input(f"Directory {dir_count} name: ")
                    new_dir_path = dst_path / dir_name
                    new_dir_path.mkdir()
                    dirs_list.append(dir_name)
                    dir_count += 1

                destinations_list = []
                print(dirs_list)
                for item in extensions_list:
                    destination = input(f"Directory for {item}: ")
                    if destination in dirs_list:
                        destinations_list.append(destination)
                    else:
                        print("Directory not available")
                organizer = dict(zip(extensions_list, destinations_list))

                if len(organizer.values()) != 0:
                    items = src_path.iterdir()
                    for item in items:
                        if item.is_file():
                            if item.suffix in organizer.keys():
                                a = str(item)
                                b = str(dst_path / organizer[item.suffix])
                                shutil.copy2(a, b)

                    dirs_files = []
                    c = []
                    for item in dirs_list:
                        new_path = dst_path / item
                        files = new_path.iterdir()
                        for y in files:
                            c.append(y)
                        length = len(c)
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
                            archive = dst_path / archive_name
                            compress_path = dst_path / name
                            shutil.make_archive(archive, 'zip', compress_path)
                            print(f"Success! Directory {name} compressed")
                        else:
                            print("Directory not found")
        else:
            print("Path not found")
    else:
        print("Path not found")
except FileExistsError:
    print("Directory already exists")
except ValueError:
    print("Please input a number")
