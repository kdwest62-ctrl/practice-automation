from pathlib import Path
import pandas as pd

file_name = input("File name: ")
path = input("Search for duplicates (input path): ")
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

        if len(paths) > 1:
            names = []
            location = []
            sizes = []
            nums = []
            num = 0
            for item in paths:
                names.append(Path(item).name)
                location.append(Path(item).parent)
                sizes.append(Path(item).stat().st_size / 1024)
                nums.append(num)
                num += 1

            data = {'Number': [i for i in nums],
                    'Location': [i for i in location],
                    'Size (kb)': [i for i in sizes]}
            df = pd.DataFrame(data, index=[i for i in names])
            print(df.to_string())

        else:
            print("No duplicates found")
    else:
        print("No files in path")
else:
    print("Path does not exist")
