from pathlib import Path
import pandas as pd

path = Path(input("Path: "))
if path.exists():
    files = []
    dirs = []
    for item in path.rglob('*'):
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            dirs.append(item)

    files_to_remove = []
    file_names = []
    locations = []
    sizes = []
    criterion = 10
    for file in files:
        size = file.stat().st_size
        converted = round((size / 1024**2), 2)
        if converted >= criterion:
            sizes.append(converted)
            files_to_remove.append(file)

    for file in files_to_remove:
        file_path = Path(file)
        file_names.append(file_path.name)
        locations.append(file_path.parent)

    dirs_to_remove = []
    dir_loc = []
    dir_names = []
    for item in dirs:
        count = []
        for element in item.iterdir():
            count.append(element)
        if len(count) == 0:
            dirs_to_remove.append(item)

    for item in dirs_to_remove:
        dir_path = Path(item)
        dir_names.append(dir_path.name)
        dir_loc.append(dir_path.parent)

    if len(files_to_remove) == 0 and len(dirs_to_remove) == 0:
        print("No files and directories match the criteria")
    elif len(files_to_remove) > 0 and len(dirs_to_remove) == 0:
        print(f"Files (>= {criterion} mb)")
        data = {'Location': [item for item in locations], 'Size (mb)': [item for item in sizes]}
        df = pd.DataFrame(data, index=[item for item in file_names])
        print(df.to_string())
    elif len(files_to_remove) == 0 and len(dirs_to_remove) > 0:
        print("Empty directories")
        data = {'Location': [item for item in dir_loc]}
        df = pd.DataFrame(data, index=[item for item in dir_names])
        print(df.to_string())
    else:
        print(f"Files (>= {criterion} mb)")
        data = {'Location': [item for item in locations], 'Size (mb)': [item for item in sizes]}
        df = pd.DataFrame(data, index=[item for item in file_names])
        print(df.to_string())
        print('-' * 8)
        print("Empty directories")
        data = {'Location': [item for item in dir_loc]}
        df = pd.DataFrame(data, index=[item for item in dir_names])
        print(df.to_string())
else:
    print("Path not found")
