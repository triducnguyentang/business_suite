from .task_manager import TaskManager

def run_tasks_cli():
    """Main function to run the Task Manager command-line interface."""
    filename = "tasks.json"
    manager = TaskManager(filename)

    print("\n--- Welcome to your Task Manager! ---")

    while True:
        print("\nTask Menu:")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Return to Main Menu")
        print("-------------------------")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # TODO: Get task details from the user.
            print("TODO: Add task functionality to be implemented.")

        elif choice == '2':
            # TODO: Display tasks to the user.
            print("TODO: View tasks functionality to be implemented.")

        elif choice == '3':
            # TODO: Mark a task as complete.
            print("TODO: Mark task complete functionality to be implemented.")

        elif choice == '4':
            # TODO: Delete a task.
            print("TODO: Delete task functionality to be implemented.")

        elif choice == '5':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")