import shutil
from pathlib import Path

source = Path(input("Source directory path: "))
if source.exists():
    def get_files(dir_path):
        content = []
        for i in dir_path.iterdir():
            if i.is_file():
                content.append(str(i))
        return tuple(content)
    def get_names(dir_path):
        names = []
        for i in dir_path.iterdir():
            if i.is_file():
                names.append(str(i.name))
        return tuple(names)
    def sync(src_files, dir_path):
        for i in Path(dir_path).iterdir():
            Path(i).unlink()
        for file in src_files:
            shutil.copy2(file, dir_path)

    source_names = get_names(source)
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
            file_names = []
            for item in paths:
                files_of_paths.append(get_files(item))
                file_names.append(get_names(item))

            score = 0
            for file_name in file_names:
                if file_name != source_names:
                    score += 1
                else:
                    score += 0
            if score != 0:
                to_sync = dict(zip(paths, files_of_paths))
                for path, files in to_sync.items():
                    if files != source_files:
                        sync(source_files, path)
                print("Success! Directories synced")
            else:
                print("Directories already synced")
    else:
        print("No files in path")
else:
    print("Path not found")
