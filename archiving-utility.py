import shutil
from pathlib import Path

try:
    path = Path(input("Path: "))
    if path.exists():
        dir_paths = []
        dir_names = []
        for item in path.iterdir():
            if item.is_dir():
                dir_paths.append(item)
                dir_names.append(Path(item).name)

        if len(dir_paths) > 0:
            numbers = [item for item in range(len(dir_paths))]
            dirs = dict(zip(numbers, dir_names))
            for num, dir_name in dirs.items():
                print(num, dir_name)

            total = int(input("Number of directories to archive: "))
            if total > 0:
                dir_nums = []
                count = 0
                while count < total:
                    dir_num = int(input("Directory to archive (number): "))
                    if dir_num in dirs.keys():
                        dir_nums.append(dir_num)
                        count += 1
                    else:
                        print("Directory not found")

                archive_names = []
                for item in dir_nums:
                    archive_name = input(f"Archive name for {dirs[item]}: ")
                    if archive_name not in archive_names:
                        archive_names.append(archive_name)
                    else:
                        print(f"{archive_name} already taken")

                to_archive = dict(zip(dir_nums, archive_names))
                reference = dict(zip(numbers, dir_paths))

                for num, name in to_archive.items():
                    dst_path = Path(input(f"Destination path for {name}: "))
                    if dst_path.exists():
                        src = str(reference[num])
                        dst = dst_path / name
                        shutil.make_archive(dst, 'zip', src)
                        print(f"{dirs[num]} archived as {name}")
                    else:
                        print("Destination path not found")
        else:
            print("No directories in path")
    else:
        print("Path not found")
except ValueError:
    print("Invalid input")
