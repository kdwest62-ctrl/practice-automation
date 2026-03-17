import os
import shutil
import pandas as pd

path = input("Directory path: ")
if os.path.exists(path):
    def converter(num):
        result = num / (1024**3)
        return round(result, 2)
    def percentage(part, whole):
        result = (part / whole) * 100
        return round(result, 2)

    usage = shutil.disk_usage(path)
    total = converter(usage.total)
    used = converter(usage.used)
    free = converter(usage.free)
    percent_used = percentage(used, total)
    percent_free = percentage(free, total)

    items = os.listdir(path)
    files = []
    for item in items:
        files.append(os.path.join(path, item))
    sizes = []
    for file in files:
        size = os.path.getsize(file)
        sizes.append(converter(size))
    dir_size = sum(sizes)
    percent_dir = percentage(dir_size, total)

    print(f"Total space: {total} gb")
    data = {'Data (gb)': [used, dir_size, free],
            '% used in total space': [percent_used, percent_dir, percent_free]}
    df = pd.DataFrame(data, index=['Used space', 'Directory size', 'Free space'])
    print(df)
else:
    print("Path not found")
