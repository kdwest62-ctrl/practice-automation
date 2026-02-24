from pathlib import Path

dir_path = Path(input("Directory path: "))
if dir_path.exists():
    file_extensions = []
    items = dir_path.iterdir()
    for item in items:
        if item.is_file():
            file_extensions.append(item.suffix)
    print(set(file_extensions))

    file_extension = input("File extension to rename: ")
    if file_extension in file_extensions:
        num = 1
        renamed = 0
        items = dir_path.iterdir()
        for item in items:
            if item.is_file():
                if item.suffix == file_extension:
                    new_name = item.parent / f'test{num}{file_extension}'
                    item.rename(new_name)
                    num += 1
                    renamed += 1
        print(f"{renamed} files renamed")
    else:
        print("File extension not available")
else:
    print("Path not found")
