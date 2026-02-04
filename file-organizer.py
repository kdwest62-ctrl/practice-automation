import os
import shutil

try:
    def file_extension(filename):
        filename_split = filename.split('.')
        return filename_split[-1]

    path = input("Source path: ")
    os.chdir(path)

    dirs_list = []
    total_dirs = int(input("Number of directories to create: "))
    if total_dirs != 0:
        dir_count = 1
        while dir_count <= total_dirs:
            dir_name= input(f"Directory {dir_count} name: ")
            os.mkdir(dir_name)
            dirs_list.append(dir_name)
            dir_count += 1

        draft_list = []
        items = os.listdir(os.getcwd())
        for item in items:
            if os.path.isfile(item):
                draft_list.append(file_extension(item))
        file_extensions = set(draft_list)
        print(file_extensions)

        extensions_list = []
        total_ext = int(input("Number of file extensions to organize: "))
        if total_ext != 0:
            ext_count = 1
            while ext_count <= total_ext:
                extension = input(f"File extension {ext_count} name: ")
                if extension not in file_extensions:
                    print("File extension not found. Try again")
                else:
                    extensions_list.append(extension)
                    ext_count += 1

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
                items = os.listdir(os.getcwd())
                for item in items:
                    if os.path.isfile(item):
                        if file_extension(item) in organizer.keys():
                            shutil.move(item, os.path.join(os.getcwd(), organizer[file_extension(item)]))
                print("File organization successful")

                compress = input("Compress directory? (y/n): ")
                if compress == 'y':
                    print(dirs_list)
                    name = input("Directory name: ")
                    if name in dirs_list:
                        archive_name = input("Archive name: ")
                        shutil.make_archive(archive_name, 'zip', os.path.join(os.getcwd(), name))
                        print(f"Success! Directory {name} compressed")
                    else:
                        print("Directory not found")
except FileExistsError:
    print("Directory already exists")
except FileNotFoundError:
    print("Path not found")
except ValueError:
    print("Please input a number")
