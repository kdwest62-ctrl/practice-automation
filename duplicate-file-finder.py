import os

try:
    path1 = input("Path 1: ")
    path1_items = os.listdir(path1)
    path2 = input("Path 2: ")
    path2_items = os.listdir(path2)

    duplicates = []
    for item in path1_items:
        if item in path2_items:
            duplicates.append(item)
    for item in path2_items:
        if item in path1_items:
            duplicates.append(item)

    if len(duplicates) == 0:
        print("No duplicate files")
    else:
        print(f"Duplicate files: {set(duplicates)}")
        choice = input("Delete duplicates? (y/n): ")
        if choice == 'y':
            path = input("Select path: ")
            if path == '1':
                filename = input("Filename: ")
                os.remove(os.path.join(path1, filename))
                print("Success! Duplicates deleted")
            elif path == '2':
                filename = input("Filename: ")
                os.remove(os.path.join(path2, filename))
                print("Success! Duplicates deleted")
            else:
                print("Path doesn't exist")
except FileNotFoundError:
    print("Filename not found")
