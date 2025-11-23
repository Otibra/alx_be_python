def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        # Display menu options to the user
        print("Shopping List Manager")
        print("1. Add item")
        print("2. Remove item")
        print("3. Display list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item}")
        
        elif choice == "2":
            # Remove item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item}")
            else:
                print(f"{item} Invalid.")
        
        elif choice == "3":
            # Display list
            if shopping_list:
                for item in shopping_list:
                    print("{item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == "4":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again")

# Run the program
main()
