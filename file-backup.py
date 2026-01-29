import os
import shutil

destination = input("Destination path: ")
os.chdir(destination)
if not os.path.isdir('Backup'):
    os.mkdir('Backup')

source = input("Source path: ")
os.chdir(source)
extension = input("File extension: ")
count = 0
items = os.listdir(os.getcwd())
for item in items:
    if os.path.isfile(item):
        if item.endswith(extension):
            shutil.copy(item, '')
            count += 1
print(f"{count} files copied")
