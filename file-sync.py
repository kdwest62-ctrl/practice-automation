import shutil
from pathlib import Path

source = Path(input("Source directory path: "))
if source.exists():
    def get_files(dir_path):
        return tuple(dir_path.iterdir())
    def sync(src_files, dir_path, dir_files):
        for file in src_files:
            if file not in dir_files:
                shutil.copy2(file, dir_path)
    def check(src_files, dir_files):
        if dir_files == src_files:
            return 0
        else:
            return 1

    source_files = get_files(source)
    if len(source_files) > 0:
        total = int(input("Number of directories to sync with source: "))
        if total > 0:
            paths = []
            count = 1
            while count <= total:
                path = Path(input(f"Directory {count} path: "))
                if path.exists():
                    paths.append(path)
                    count += 1
                else:
                    print("Path not found")

            files_of_paths = []
            for item in paths:
                files_of_paths.append(get_files(item))
            scores = []
            for item in files_of_paths:
                scores.append(check(source_files, item))

            if sum(scores) != 0:
                to_sync = dict(zip(paths, files_of_paths))
                for path, files in to_sync.items():
                    if files != source_files:
                        sync(source_files, path, files)
                print("Success! Directories synced")
            else:
                print("Directories already synced")
    else:
        print("No files in path")
else:
    print("Path not found")
