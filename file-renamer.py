import os

dir_path = input("Directory path: ")
os.chdir(dir_path)

files = os.listdir(os.getcwd())
num = 1
for file in files:
    if os.path.isfile(file):
        if file.endswith('png'):
            os.rename(file, f'DES{num}.png')
            num += 1
print("Files successfully renamed")
