import shutil
import pandas as pd
from pathlib import Path

try:
    path = Path(input("Directory path: "))
    if path.exists():
        def convert(num, unit_choice):
            if unit_choice == 'kb':
                result = num / 1024
                return round(result, 2)
            elif unit_choice == 'mb':
                result = num / (1024**2)
                return round(result, 2)
            elif unit_choice == 'gb':
                result = num / (1024**3)
                return round(result, 2)
        def percent(part, whole):
            result = (part / whole) * 100
            return round(result, 2)

        files = []
        for item in path.rglob('*'):
            if item.is_file():
                files.append(item)

        if len(files) > 0:
            unit = input("Select unit (kb, mb, gb): ")
            usage = shutil.disk_usage(path)
            total = convert(usage.total, unit)
            used = convert(usage.used, unit)
            free = convert(usage.free, unit)
            percent_used = percent(used, total)
            percent_free = percent(free, total)

            file_names = []
            locations = []
            for file in files:
                x = Path(file)
                file_names.append(x.name)
                locations.append(x.parent)

            sizes = []
            for file in files:
                size = file.stat().st_size
                sizes.append(convert(size, unit))
            dir_size = sum(sizes)
            percent_dir = percent(dir_size, total)

            percentages = []
            for size in sizes:
                percentage = percent(size, dir_size)
                percentages.append(percentage)

            print(f"Total space: {total} {unit}")
            print(f"Free space: {free} {unit} ({percent_free} %)")
            data = {f'Data ({unit})': [used, dir_size],
                    'Space used in total space(%)': [percent_used, percent_dir]}
            df = pd.DataFrame(data, index=['Used space', 'Directory size'])
            print(df)
            print('-' * 8)
            data = {'Location': [item for item in locations],
                     f'Data ({unit})': [item for item in sizes],
                     'Space used in directory (%)': [item for item in percentages]}
            df = pd.DataFrame(data, index=[item for item in file_names])
            print(df.to_string())
        else:
            print("No items in path")
    else:
        print("Path not found")
except TypeError:
    print("Unit not found")
