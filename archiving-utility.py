import shutil
from pathlib import Path

path = Path(input("Path: "))
if path.exists():
    items = path.iterdir()
    for item in items:
        if item.is_dir():
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
    print("Path not found")
