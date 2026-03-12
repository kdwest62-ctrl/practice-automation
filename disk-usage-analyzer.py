import os
import shutil

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
    free = converter(usage.free)
    used = converter(usage.used)
    percent_free = percentage(free, total)
    percent_used = percentage(used, total)

    items = os.listdir(path)
    files = []
    for item in items:
        files.append(os.path.join(path, item))
    sizes = []
    for file in files:
        size = os.path.getsize(file)
        sizes.append(converter(size))
    dir_size = sum(sizes)
    percent_dir = percentage(dir_size, used)

    print(f"Total space: {total} GB")
    print(f"Used space: {used} GB")
    print(f"Used space %: {percent_used}")
    print(f"% used by directory: {percent_dir}")
    print(f"Free space: {free} GB")
    print(f"Free space %: {percent_free}")

else:
    print("Path not found")
