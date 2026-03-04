import os
import shutil

dir1_path = input("Directory path 1: ")
if os.path.exists(dir1_path):
    dir1 = os.listdir(dir1_path)
    dir2_path = input("Directory path 2: ")
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
                synced = 0
                for file in files_to_sync:
                    src = os.path.join(dir1_path, file)
                    shutil.copy2(src, dir2_path)
                    synced += 1
                print(f"Files synced: {synced}")
    else:
        print("Path not found")
else:
    print("Path not found")
