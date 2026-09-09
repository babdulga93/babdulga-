import json

def main():
    print("Welcome to the Inventory Manager!")
    
    # Our empty dictionary to hold the stock
    inventory = {}
    # Try to load existing data when the program starts
    try:
        with open ("inventory_data.json", "r") as file:
            inventory = json.load(file)
    except FileNotFoundError:
        pass # If the file doesn't exist yet, we just continue with an empty dictionary

    
    while True:
        print("\n--- Main Menu ---")
        print("2. View all items")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            item_name = input("Enter the item name: ")
            # We use int() to convert the user's text input into a number
            try:
                # We TRY to convert the user's input into a number
                item_quantity = int(input("Enter the quantity: ")) 
                # Check if the item already exist in the dictionary
                if item_name in inventory:
                    # Add the new quantity to existing total
                    inventory[item_name] += item_quantity
                    print(f"Updated! Added {item_quantity} to '{item_name}'.New total: {inventory[item_name]}")
                else:
                    # Creat a brand new entry
                    
                # If successful, it moves to these lones
                # This line stores the key-value pair in the dictionary
                   inventory[item_name] = item_quantity
                   print(f"Success! {item_quantity} '{item_name}' added to stock.")
                   # save the updated dictionary to the file
                   with open("inventory_data.json","w") as file:
                       json.dump(inventory, file)
            except ValueError:
                    # If they typed letters(like "twenty") instead of a number,it jumps here
                    print("Error: Please enter a valid whole number for quantity")
            
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