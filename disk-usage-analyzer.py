import os
import shutil
import pandas as pd

try:
    path = input("Directory path: ")
    if os.path.exists(path):
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

        items = os.listdir(path)
        if len(items) > 0:
            unit = input("Select unit (kb, mb, gb): ")
            usage = shutil.disk_usage(path)
            total = convert(usage.total, unit)
            used = convert(usage.used, unit)
            free = convert(usage.free, unit)
            percent_used = percent(used, total)
            percent_free = percent(free, total)

            files = []
            for item in items:
                file = os.path.join(path, item)
                if os.path.isfile(file):
                    files.append(file)
            sizes = []
            for item in files:
                size = os.path.getsize(item)
                sizes.append(convert(size, unit))
            dir_size = sum(sizes)
            percent_dir = percent(dir_size, total)

            print(f"Total space: {total} {unit}")
            data = {f'Data {unit}': [used, dir_size, free],
                    '% used in total space': [percent_used, percent_dir, percent_free]}
            df = pd.DataFrame(data, index=['Used space', 'Directory size', 'Free space'])
            print(df)
        else:
            print("No items in path")
    else:
        print("Path not found")
except TypeError:
    print("Unit not found")
