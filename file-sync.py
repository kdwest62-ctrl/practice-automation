import os
import shutil

dir1_path = input("Original directory path: ")
if os.path.exists(dir1_path):
    dir1 = os.listdir(dir1_path)
    dir2_path = input("Sync directory path: ")
    if os.path.exists(dir2_path):
        dir2 = os.listdir(dir2_path)
        if dir1 == dir2:
            print("Files synced")
        else:
            print("Files not synced")
            sync = input("Sync? (y/n): ")
            if sync == 'y':
                files_to_sync = []
                for file in dir1:
                    if file not in dir2:
                        files_to_sync.append(file)
                added = 0
                for file in files_to_sync:
                    src = os.path.join(dir1_path, file)
                    shutil.copy2(src, dir2_path)
                    added += 1
                print(f"Files added to sync directory: {added}")
    else:
        print("Path not found")
else:
    print("Path not found")
