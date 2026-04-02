import shutil
from pathlib import Path

path = Path(input("Path: "))
if path.exists():
    dirs = []
    for item in path.iterdir():
        if item.is_dir():
            dirs.append(item)

    if len(dirs) > 0:
        for item in dirs:
            print(item.name)
        dir_to_archive = input("Directory to archive: ")
        archive_name = input("Archive name: ")
        dst_path = Path(input("Destination path: "))
        if dst_path.exists():
            src = path / dir_to_archive
            dst = dst_path / archive_name
            shutil.make_archive(dst, 'zip', src)
            print(f"{dir_to_archive} archived as {archive_name}")
        else:
            print("Path not found")
    else:
        print("No directories in path")
else:
    print("Path not found")
