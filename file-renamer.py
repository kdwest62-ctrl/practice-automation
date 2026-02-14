import os

dir_path = input("Directory path: ")
if os.path.exists(dir_path):
    files = os.listdir(dir_path)
    num = 1
    renamed = 0
    for file in files:
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            if file.endswith('png'):
                os.rename(file_path, os.path.join(dir_path, f'DES{num}.png'))
                num += 1
                renamed += 1
    print(f"{renamed} files renamed")
else:
    print("Path not found")
