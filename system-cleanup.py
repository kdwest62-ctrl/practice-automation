from pathlib import Path
import pandas as pd

try:
    path = Path(input("Path: "))
    if path.exists():
        def convert(num, unit_choice):
            if unit_choice == 'kb':
                result = num / 1024
                return round(result, 2)
            elif unit_choice == 'mb':
                result = num / (1024 ** 2)
                return round(result, 2)
            elif unit_choice == 'gb':
                result = num / (1024 ** 3)
                return round(result, 2)

        files = []
        dirs = []
        for item in path.rglob('*'):
            if item.is_file():
                files.append(item)
            elif item.is_dir():
                dirs.append(item)

        files_match = []
        file_names = []
        locations = []
        sizes = []
        unit = input("Select unit (kb, mb, gb): ")
        file_size = float(input(f"File size ({unit}): "))
        for file in files:
            size = file.stat().st_size
            converted = convert(size, unit)
            if converted >= file_size:
                sizes.append(converted)
                files_match.append(file)
        for file in files_match:
            file_path = Path(file)
            file_names.append(file_path.name)
            locations.append(file_path.parent)

        num_files = [item for item in range(len(files_match))]
        my_dict1 = dict(zip(num_files, files_match))

        dirs_match = []
        dir_loc = []
        dir_names = []
        for item in dirs:
            count = []
            for element in item.iterdir():
                count.append(element)
            if len(count) == 0:
                dirs_match.append(item)
        for item in dirs_match:
            dir_path = Path(item)
            dir_names.append(dir_path.name)
            dir_loc.append(dir_path.parent)

        num_dirs = [item for item in range(len(dirs_match))]
        my_dict2 = dict(zip(num_dirs, dirs_match))

        if len(files_match) == 0 and len(dirs_match) == 0:
            print("No files and directories matched the criteria")
        elif len(files_match) > 0 and len(dirs_match) == 0:
            print(f"Files (>= {file_size} {unit})")
            data = {'Number': [item for item in range(len(files_match))],
                    'Location': [item for item in locations],
                    f'Size ({unit})': [item for item in sizes]}
            df = pd.DataFrame(data, index=[item for item in file_names])
            print(df.to_string())
            print('-' * 8)
            print("No empty directories")
            print('-' * 8)
            remove_files = input("Remove files? (y/n): ")
            if remove_files == 'y':
                choice = input("Remove all or selection? (a/s): ")
                if choice == 'a':
                    for value in my_dict1.values():
                        f = Path(value)
                        f.unlink()
                    print("Files removed successfully")
                elif choice == 's':
                    remove_items = []
                    total = int(input("How many to remove: "))
                    if total <= len(files_match):
                        count = 0
                        while count < total:
                            remove = int(input("File number: "))
                            remove_items.append(remove)
                            count += 1
                        confirm = input("Confirm to remove selected files (y/n): ")
                        if confirm == 'y':
                            for key, value in my_dict1.items():
                                if key in remove_items:
                                    f = Path(value)
                                    f.unlink()
                            print("Files removed successfully")
        elif len(files_match) == 0 and len(dirs_match) > 0:
            print(f"No files >= {file_size} {unit}")
            print('-' * 8)
            print("Empty directories")
            data = {'Number': [item for item in range(len(dirs_match))],
                    'Location': [item for item in dir_loc]}
            df = pd.DataFrame(data, index=[item for item in dir_names])
            print(df.to_string())
            print('-' * 8)
            remove_dirs = input("Remove empty directories? (y/n): ")
            if remove_dirs == 'y':
                choice = input("Remove all or selection? (a/s): ")
                if choice == 'a':
                    for value in my_dict2.values():
                        d = Path(value)
                        d.rmdir()
                    print("Empty directories removed successfully")
                elif choice == 's':
                    remove_items = []
                    total = int(input("How many to remove: "))
                    if total <= len(dirs_match):
                        count = 0
                        while count < total:
                            remove = int(input("Directory number: "))
                            remove_items.append(remove)
                            count += 1
                        confirm = input("Confirm to remove selected directories (y/n): ")
                        if confirm == 'y':
                            for key, value in my_dict2.items():
                                if key in remove_items:
                                    d = Path(value)
                                    d.rmdir()
                            print("Empty directories removed successfully")
        else:
            print(f"Files (>= {file_size} {unit})")
            data = {'Number': [item for item in range(len(files_match))],
                    'Location': [item for item in locations],
                    f'Size ({unit})': [item for item in sizes]}
            df = pd.DataFrame(data, index=[item for item in file_names])
            print(df.to_string())
            print('-' * 8)
            print("Empty directories")
            data = {'Number': [item for item in range(len(dirs_match))],
                    'Location': [item for item in dir_loc]}
            df = pd.DataFrame(data, index=[item for item in dir_names])
            print(df.to_string())
    else:
        print("Path not found")
except TypeError:
    print("Unit not available")
except ValueError:
    print("Please input a number")
except OSError:
    print("Directory contains files and/or subdirectories")
