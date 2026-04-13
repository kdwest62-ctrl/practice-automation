import shutil
from pathlib import Path

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
        options = dict(zip(numbers, dir_names))
        for num, dir_name in options.items():
            print(num, dir_name)

        total = int(input("Number of directories to archive: "))
        if total > 0:
            dir_nums = []
            count = 0
            while count < total:
                dir_num = int(input("Directory to archive (number): "))
                if dir_num in options.keys():
                    dir_nums.append(dir_num)
                    count += 1
                else:
                    print("Directory not found")

            archive_names = []
            for item in dir_nums:
                archive_name = input(f"Archive name for {options[item]}: ")
                archive_names.append(archive_name)

            to_archive = dict(zip(dir_nums, archive_names))
            reference = dict(zip(numbers, dir_paths))

            dst_path = Path(input("Destination path: "))
            if dst_path.exists():
                for num, name in to_archive.items():
                    src = str(reference[num])
                    dst = dst_path / name
                    shutil.make_archive(dst, 'zip', src)
                    print(f"{options[num]} archived as {name}")
            else:
                print("Destination path not found")
    else:
        print("No directories in path")
else:
    print("Path not found")
