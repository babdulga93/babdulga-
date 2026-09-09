def main():
    print("Welcome to the Inventory Manager!")
    
    # Our empty dictionary to hold the stock
    inventory = {}
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new item")
        print("2. View all items")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            item_name = input("Enter the item name: ")
            # We use int() to convert the user's text input into a number
            item_quantity = int(input("Enter the quantity: ")) 
            
            # This line stores the key-value pair in the dictionary
            inventory[item_name] = item_quantity
            print(f"Success! {item_quantity} '{item_name}' added to stock.")
            
        elif choice == '2':
            # Check if the dictionary is empty first
            if len(inventory) == 0:
                print("Your inventory is currently empty.")
            else:
                print("\n--- Current Stock ---")
                # Loop through the dictionary and print each key and value
                for item, quantity in inventory.items():
                    print(f"{item}: {quantity}")
                    
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()