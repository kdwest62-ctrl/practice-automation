import os

os.chdir('')

if not os.path.isdir('Setups'):
    os.mkdir('Setups')
if not os.path.isdir('Images'):
    os.mkdir('Images')

downloads = os.listdir(os.getcwd())
for item in downloads:
    if os.path.isfile(item):
        if item.lower().endswith('.exe'):
            os.rename(item, '' + '\\' + item)
        elif item.lower().endswith('.jpg'):
            os.rename(item, '' + '\\' + item)
        else:
            continue
print("File organization successful")
