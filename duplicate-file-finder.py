from pathlib import Path
import os

try:
    path = Path(input("Path: "))
    if path.exists():
        files = []
        single_names = []
        duplicate_names = []
        duplicate_paths = []
        for item in path.rglob('*'):
            if item.is_file():
                files.append(item)
        for file in files:
            if file.name in single_names:
                duplicate_names.append(file.name)
            else:
                single_names.append(file.name)

        if len(duplicate_names) == 0:
            print("No duplicate files")
        else:
            index = 0
            while index < len(set(duplicate_names)):
                for file in files:
                    if file.name == duplicate_names[index]:
                        duplicate_paths.append(file)
                index += 1

            nums = []
            num = 1
            while num <= len(duplicate_paths):
                nums.append(num)
                num += 1

            duplicates_with_nums = dict(zip(nums, duplicate_paths))
            for key, value in duplicates_with_nums.items():
                print(key, value)

            show_size = input("Show file sizes? (y/n): ")
            if show_size == 'y':
                file_sizes = []
                for item in duplicate_paths:
                    size = os.path.getsize(str(item))
                    file_sizes.append(size / 1000)
                dict1 = dict(zip(nums, file_sizes))

                for key, value in dict1.items():
                    print(f"{key} ({value} KB)")

            remove = input("Remove files? (y/n): ")
            if remove == 'y':
                total = int(input("Number of files to remove: "))
                if total <= len(duplicate_paths) and total != 0:
                    files_to_remove = []
                    count = 0
                    while count != total:
                        file_num = int(input("Remove file (input number): "))
                        if file_num in nums:
                            files_to_remove.append(file_num)
                            count += 1
                        else:
                            print("Number not in list")
                    files_removed = 0
                    for item in files_to_remove:
                        duplicates_with_nums[item].unlink()
                        files_removed += 1
                    print(f"{files_removed} files removed")
                else:
                    print(f"There are only {len(duplicates_with_nums.values())} files")
    else:
        print("Path not found")
except ValueError:
    print("Please input a whole number")
