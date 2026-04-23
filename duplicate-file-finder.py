from pathlib import Path
import pandas as pd

file_name = input("File name: ")
if len(file_name) >= 3:
    path = input("Search for file (input directory path): ")
    if Path(path).exists():
        files = []
        for item in Path(path).rglob('*'):
            if Path(item).is_file():
                files.append(str(item))

        if len(files) > 0:
            paths = []
            for file_path in files:
                if file_name in file_path:
                    paths.append(file_path)

            if len(paths) > 0:
                names = []
                location = []
                sizes = []
                nums = []
                num = 0
                for item in paths:
                    names.append(Path(item).name)
                    location.append(Path(item).parent)
                    size = Path(item).stat().st_size / (1024**2)
                    sizes.append(round(size, 2))
                    nums.append(num)
                    num += 1

                data = {'Number': [i for i in nums],
                        'Location': [i for i in location],
                        'Size (mb)': [i for i in sizes]}
                df = pd.DataFrame(data, index=[i for i in names])
                print(df.to_string())

                remove = input("Remove duplicates? (y/n): ")
                if remove == 'y':
                    reference = dict(zip(nums, paths))
                    decide = input("Remove all or selection? (a/s): ")
                    if decide == 'a':
                        count = 0
                        while count < 1:
                            protect = int(input("Select file to protect (number only): "))
                            if protect in reference.keys():
                                del reference[protect]
                                for path in reference.values():
                                    Path(path).unlink()
                                print("All unprotected files removed")
                                count += 1
                            else:
                                print("Number not in list")
                    elif decide == 's':
                        total = int(input("How many files to remove? "))
                        if 0 < total < len(paths):
                            count = 0
                            while count < total:
                                number = int(input("Select file to remove (number only): "))
                                if number in reference.keys():
                                    Path(reference[number]).unlink()
                                    print(f"{Path(reference[number]).name} removed")
                                    count += 1
                                else:
                                    print("Number not in list")
                        else:
                            print("Invalid input")
            else:
                print("No files found")
        else:
            print("No files in path")
    else:
        print("Path does not exist")
else:
    print("Name must be 3 letters or more")
