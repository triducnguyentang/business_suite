from inventory.manager import run_inventory_cli
from tasks.manager import run_tasks_cli

def main_menu():
    """Displays the main menu."""
    print("\n--- Business Suite Main Menu ---")
    print("1. Manage Inventory")
    print("2. Manage Tasks")
    print("3. Exit")
    print("--------------------------------")

def main():
    """Main function to run the application."""
    print("Welcome to the Business Suite!")

    while True:
        main_menu()
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            # This function will contain the loop for the inventory manager
            run_inventory_cli()
        elif choice == '2':
            # This function will contain the loop for the task manager
            run_tasks_cli()
        elif choice == '3':
            print("Exiting Business Suite.")
            break
        else:
            print("Invalid choice. Please select an option from the menu.")

if __name__ == "__main__":
    main()
