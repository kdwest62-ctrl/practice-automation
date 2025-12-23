incomplete = []
complete = []
print("1. View Tasks\n2. Add a Task\n3. Complete a Task\n4. Remove a Task\n5. Exit")
while True:
    user_choice = input("Choose option: ")
    if user_choice == '1':
        print(f"Incomplete: {incomplete}")
        print(f"Complete: {complete}")
    elif user_choice == '2':
        new = input("Enter new task: ")
        if new in incomplete:
            print("Task already exists")
            decide = input("Continue? (y/n): ")
            if decide == 'y':
                incomplete.append(new)
                print("Task added to incomplete")
        else:
            incomplete.append(new)
            print("Task added to incomplete")
    elif user_choice == '3':
        print(f"{incomplete}")
        completed = input("Completed task: ")
        if completed in incomplete:
            for item in incomplete:
                if item == completed:
                    complete.append(item)
                    incomplete.remove(item)
                else:
                    continue
            print("Task added to complete")
        else:
            print("Task not found")
    elif user_choice == '4':
        print("1. Incomplete, 2. Complete")
        choice = input("Choose list: ")
        if choice == "1":
            if len(incomplete) == 0:
                print("List empty")
            else:
                print(f"{incomplete}")
                remove_task = input("Remove task: ")
                if remove_task in incomplete:
                    for item in incomplete:
                        if item == remove_task:
                            incomplete.remove(item)
                            print("Task removed")
                        else:
                            continue
                else:
                    print("Task not found")
        elif choice == "2":
            if len(complete) == 0:
                print("List empty")
            else:
                print(f"{complete}")
                remove_task = input("Remove task: ")
                if remove_task in complete:
                    for item in complete:
                        if item == remove_task:
                            complete.remove(item)
                            print("Task removed")
                        else:
                            continue
                else:
                    print("Task not found")
        else:
            print("Invalid choice")
    elif user_choice == '5':
        print("Program closed")
        break
    else:
        print("Invalid choice")
