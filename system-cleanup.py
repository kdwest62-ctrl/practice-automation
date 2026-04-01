from pathlib import Path

path = Path(input("Path: "))
if path.exists():
    files = []
    dirs = []
    for item in path.rglob('*'):
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            dirs.append(item)

    file_to_remove = []
    for file in files:
        size = file.stat().st_size
        if (size / (1024**2)) >= 10:
            file_to_remove.append(file)

    dir_to_remove = []
    for item in dirs:
        count = []
        for element in item.iterdir():
            count.append(element)
        if len(count) == 0:
            dir_to_remove.append(item)

    print("Files (>= 10 mb):")
    for file in file_to_remove:
        print(file)
    print('-' * 8)
    print("Empty directories:")
    for item in dir_to_remove:
        print(item)

else:
    print("Path not found")
