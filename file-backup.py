import os
import shutil

os.chdir('C:\\Users\\KEAR\\Documents')
os.mkdir('Backup')

os.chdir('C:\\Users\\KEAR\\Downloads')
items = os.listdir(os.getcwd())
for item in items:
    if os.path.isfile(item):
        extension = "".join([item[-3], item[-2], item[-1]])
        if extension == 'exe':
            shutil.copy2(item, 'C:\\Users\\KEAR\\Documents\\Backup')
print("File backup successful")
