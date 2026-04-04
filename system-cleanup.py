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
    criteria = 10
    for file in files:
        size = file.stat().st_size
        converted = round((size / 1024**2), 2)
        if converted >= criteria:
            sizes.append(converted)
            files_to_remove.append(file)

    for file in files_to_remove:
        file_path = Path(file)
        file_names.append(file_path.name)
        locations.append(file_path.parent)

    dir_to_remove = []
    dir_loc = []
    dir_names = []
    for item in dirs:
        count = []
        for element in item.iterdir():
            count.append(element)
        if len(count) == 0:
            dir_to_remove.append(item)

    for item in dir_to_remove:
        dir_path = Path(item)
        dir_names.append(dir_path.name)
        dir_loc.append(dir_path.parent)

    print(f"Files (>= {criteria} mb)")
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
