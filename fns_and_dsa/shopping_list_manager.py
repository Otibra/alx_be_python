def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display list")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item}")
        
        elif choice == "2":
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item}")
            else:
                print(f"{item}")
        
        elif choice == "3":
            if shopping_list:
                print("Your shopping list:")
                for item in shopping_list:
                    print(f"{item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

main()