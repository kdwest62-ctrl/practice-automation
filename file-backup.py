import shutil
from pathlib import Path

try:
    src_path = Path(input("Source path: "))
    if src_path.exists():
        file_extensions = []
        src_path_items = src_path.iterdir()
        for item in src_path_items:
            if item.is_file():
                file_extensions.append(item.suffix)
        print(set(file_extensions))

        extensions = []
        total_ext = int(input("Number of file extensions to backup: "))
        if total_ext != 0:
            ext_count = 1
            while ext_count <= total_ext:
                extension = input(f"File extension {ext_count} name: ")
                if extension in file_extensions:
                    extensions.append(extension)
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

                destinations = []
                print(dirs_list)
                for item in extensions:
                    destination = input(f"Directory for {item}: ")
                    if destination in dirs_list:
                        destinations.append(destination)
                    else:
                        print("Directory not available")
                ext_with_dst = dict(zip(extensions, destinations))

                if len(ext_with_dst.values()) != 0:
                    src_path_items = src_path.iterdir()
                    for item in src_path_items:
                        if item.is_file():
                            if item.suffix in ext_with_dst.keys():
                                shutil.copy2(str(item), str(dst_path / ext_with_dst[item.suffix]))

                    dirs_files = []
                    dirs_path_list = []
                    for item in dirs_list:
                        dir_path = dst_path / item
                        for file in dir_path.iterdir():
                            dirs_path_list.append(file)
                        count = len(dirs_path_list)
                        dirs_files.append(count)
                    files_count = dict(zip(dirs_list, dirs_files))
                    for key, value in files_count.items():
                        print(f"Files copied to {key}: {value}")

                    compress = input("Compress directory? (y/n): ")
                    if compress == 'y':
                        print(dirs_list)
                        name = input("Directory name: ")
                        if name in dirs_list:
                            archive_name = input("Archive name: ")
                            archive_dst = dst_path / archive_name
                            archive_src = dst_path / name
                            shutil.make_archive(archive_dst, 'zip', archive_src)
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
