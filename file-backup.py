import os
import shutil

os.chdir('') # destination
os.mkdir('Backup')

os.chdir('') # source
items = os.listdir(os.getcwd())
for item in items:
    if os.path.isfile(item):
        extension = "".join([item[-3], item[-2], item[-1]])
        if extension == 'exe':
            shutil.copy2(item, '' + '\\Backup')
print("File backup successful")
