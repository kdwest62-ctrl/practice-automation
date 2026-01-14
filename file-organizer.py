import os

os.chdir('') # directory
os.mkdir('Setups')
os.mkdir('Images')

downloads = os.listdir(os.getcwd())
for item in downloads:
    if os.path.isfile(item):
        extension = "".join([item[-3], item[-2], item[-1]])
        if extension == 'exe':
            os.rename(item, '' + '\\' + item) # new directory
        elif extension == 'jpg':
            os.rename(item, '' + '\\' + item) # new directory
        else:
            continue
print("File organization successful")
