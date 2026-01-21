import os
import shutil

os.chdir(r'')

if not os.path.isdir('Setups'):
    os.mkdir('Setups')
if not os.path.isdir('Images'):
    os.mkdir('Images')

exe_count = 0
jpg_count = 0
downloads = os.listdir(os.getcwd())
for item in downloads:
    if os.path.isfile(item):
        if item.lower().endswith('.exe'):
            shutil.move(item, os.path.join(os.getcwd(), 'Setups'))
            exe_count += 1
        elif item.lower().endswith('.jpg'):
            shutil.move(item, os.path.join(os.getcwd(), 'Images'))
            jpg_count += 1
        else:
            continue
print(f"Success! Setups: {exe_count} files, Images: {jpg_count} files")
