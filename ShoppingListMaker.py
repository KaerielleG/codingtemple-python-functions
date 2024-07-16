#task1
# Function to add items to the shopping list
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

# Function to display the current shopping list
def display_list(shopping_list):
    if shopping_list:
        print("Current Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

# Main function to run the shopping list program
def main():
    shopping_list = []

    print("Welcome to the Shopping List Program!")

    while True:
        print("\nMenu:")
        print("1. Add item to shopping list")
        print("2. View shopping list")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            display_list(shopping_list)
        elif choice == '3':
            print("Thank you for using the Shopping List Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Call the main function to start the program
if __name__ == "__main__":
    main()


#task2
# Function to add items to the shopping list
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

# Function to remove items from the shopping list
def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")

# Function to display the current shopping list
def display_list(shopping_list):
    if shopping_list:
        print("Current Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

# Main function to run the shopping list program
def main():
    shopping_list = []

    print("Welcome to the Shopping List Program!")

    while True:
        print("\nMenu:")
        print("1. Add item to shopping list")
        print("2. Remove item from shopping list")
        print("3. View shopping list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == '3':
            display_list(shopping_list)
        elif choice == '4':
            print("Thank you for using the Shopping List Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Call the main function to start the program
if __name__ == "__main__":
    main()




#task3