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

        items = path.iterdir()
        files = []
        for item in items:
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

            sizes = []
            for file in files:
                size = file.stat().st_size
                sizes.append(convert(size, unit))
            dir_size = sum(sizes)
            percent_dir = percent(dir_size, total)

            print(f"Total space: {total} {unit}")
            data = {f'Data ({unit})': [used, dir_size, free],
                    '% used in total space': [percent_used, percent_dir, percent_free]}
            df = pd.DataFrame(data, index=['Used space', 'Directory size', 'Free space'])
            print(df)
        else:
            print("No items in path")
    else:
        print("Path not found")
except TypeError:
    print("Unit not found")
