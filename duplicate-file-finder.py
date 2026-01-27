import os

path1_files = []
os.chdir(r'')
path1 = os.listdir(os.getcwd())
for item in path1:
    if os.path.isfile(item):
        path1_files.append(item)
path2_files = []
os.chdir(r'')
path2 = os.listdir(os.getcwd())
for item in path2:
    if os.path.isfile(item):
        path2_files.append(item)

duplicates = []
for item in path1_files:
    if item in path2_files:
        duplicates.append(item)
for item in path2_files:
    if item in path1_files:
        duplicates.append(item)

if len(duplicates) == 0:
    print("No duplicate files")
else:
    print(f"Duplicate files found: {set(duplicates)}")
