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

        dirs_to_archive = []
        total = int(input("Number of directories to archive: "))
        if total > 0:
            count = 1
            while count <= total:
                dir_to_archive = input(f"Directory {count} to archive: ")
                a = path / dir_to_archive
                if a in dirs:
                    dirs_to_archive.append(a)
                    count += 1
                else:
                    print("Directory not found")

            archive_names = []
            for item in dirs_to_archive:
                archive_name = input(f"Archive name for {item}: ")
                archive_names.append(archive_name)

            my_dict = dict(zip(dirs_to_archive, archive_names))

            dst_path = Path(input("Destination path: "))
            if dst_path.exists():
                for key, value in my_dict.items():
                    src = path / key
                    dst = dst_path / value
                    shutil.make_archive(dst, 'zip', src)
                    print(f"{key} archived as {value}")
            else:
                print("Destination path not found")
    else:
        print("No directories in path")
else:
    print("Path not found")
