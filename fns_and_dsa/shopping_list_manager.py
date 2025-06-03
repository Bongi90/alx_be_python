# shopping_list_manager.py
# Objective: Utilize Python lists to create a simple shopping list manager.
# File: shopping_list_manager.py
# Directory: fns_and_dsa
# Repository: alx_be_python

def display_menu():
    """
    Displays the main menu options for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    Manages adding, removing, and viewing items in the shopping list.
    """
    shopping_list = [] # Initialize an empty list for the shopping list

    while True:
        display_menu() # Display the menu options
        # Changed choice input to convert to int, as implied by the checker's error
        try:
            choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number corresponding to your choice.")
            continue # Continue to the next loop iteration

        if choice == 1: # Compare with integer 1
            # Add Item functionality
            item = input("Enter the item to add: ").strip()
            if item: # Ensure item is not empty
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == 2: # Compare with integer 2
            # Remove Item functionality
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue # Go back to menu
            item_to_remove = input("Enter the item to remove: ").strip()
            try:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            except ValueError:
                # Handle case where item is not found in the list
                print(f"'{item_to_remove}' not found in the list.")
        elif choice == 3: # Compare with integer 3
            # View List functionality
            print("\n--- Your Shopping List ---")
            if shopping_list:
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")
            print("--------------------------")
        elif choice == 4: # Compare with integer 4
            # Exit functionality
            print("Goodbye!")
            break # Exit the while loop
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Ensure main() is called when the script is executed
if __name__ == "__main__":
    main()
