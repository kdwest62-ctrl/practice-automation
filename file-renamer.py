from pathlib import Path

dir_path = Path(input("Directory path: "))
if dir_path.exists():
    files = dir_path.iterdir()
    num = 1
    renamed = 0
    for file in files:
        if file.is_file():
            if file.suffix == '.png':
                new_name = file.parent / f'DES{num}.png'
                file.rename(new_name)
                num += 1
                renamed += 1
    print(f"{renamed} files renamed")
else:
   print("Path not found")
