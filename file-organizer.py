import shutil
from pathlib import Path

try:
    path = Path(input("Path: "))
    if path.exists():
        dirs_list = []
        total_dirs = int(input("Number of directories to create: "))
        if total_dirs != 0:
            dir_count = 1
            while dir_count <= total_dirs:
                dir_name= input(f"Directory {dir_count} name: ")
                new_dir_path = path / dir_name
                new_dir_path.mkdir()
                dirs_list.append(dir_name)
                dir_count += 1

            file_extensions = []
            items = path.iterdir()
            for item in items:
                if item.is_file():
                    file_extensions.append(item.suffix)
            print(set(file_extensions))

            extensions_list = []
            total_ext = int(input("Number of file extensions to organize: "))
            if total_ext != 0:
                ext_count = 1
                while ext_count <= total_ext:
                    extension = input(f"File extension {ext_count} name: ")
                    if extension in file_extensions:
                        extensions_list.append(extension)
                        ext_count += 1
                    else:
                        print("File extension not found. Try again")

                destinations_list = []
                print(dirs_list)
                for item in extensions_list:
                    destination = input(f"Directory for {item}: ")
                    if destination in dirs_list:
                        destinations_list.append(destination)
                    else:
                        print("Directory not found")
                ext_with_dst = dict(zip(extensions_list, destinations_list))
                print(ext_with_dst)

                if len(ext_with_dst.values()) != 0:
                    items = path.iterdir()
                    for item in items:
                        if item.is_file():
                            if item.suffix in extensions_list:
                                src = str(item)
                                dst = str(path / ext_with_dst[item.suffix])
                                shutil.move(src, dst)

                    dirs_files = []
                    c = []
                    for item in dirs_list:
                        new_path = path / item
                        files = new_path.iterdir()
                        for b in files:
                            c.append(b)
                        length = len(c)
                        dirs_files.append(length)
                    files_count = dict(zip(dirs_list, dirs_files))
                    for key, value in files_count.items():
                        print(f"Files moved to {key}: {value}")

                    compress = input("Compress directory? (y/n): ")
                    if compress == 'y':
                        print(dirs_list)
                        name = input("Directory name: ")
                        if name in dirs_list:
                            archive_name = input("Archive name: ")
                            archive = path / archive_name
                            compress_path = path / name
                            shutil.make_archive(archive, 'zip', compress_path)
                            print(f"Success! Directory {name} compressed")
                        else:
                            print("Directory not found")
    else:
        print("Path not found")
except FileExistsError:
    print("Directory already exists")
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Please input a number")
