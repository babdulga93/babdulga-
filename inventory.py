import json

def main():
    print("Welcome to the Inventory Manager!")
    
    inventory = {}
    
    try:
        with open("inventory_data.json", "r") as file:
            inventory = json.load(file)
    except FileNotFoundError:
        pass
        
    while True:
        print("\n--- Main Menu ---")
        print("1. Add or restock an item")
        print("2. View all items")
        print("3. Sell an item")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            # NEW: Automatically title-case and trim spaces from the input
            item_name = input("Enter the item name: ").title().strip()
            
            try:
                item_quantity = int(input("Enter the quantity: ")) 
                if item_name in inventory:
                    inventory[item_name] += item_quantity
                    print(f"Updated! Added {item_quantity} to '{item_name}'. New total: {inventory[item_name]}")
                else:
                    inventory[item_name] = item_quantity
                    print(f"Success! {item_quantity} '{item_name}' added to stock.")
                
                with open("inventory_data.json", "w") as file:
                    json.dump(inventory, file)
                    
            except ValueError:
                print("Error: Please enter a valid whole number for the quantity.")
                
        elif choice == '2':
            if len(inventory) == 0:
                print("Your inventory is currently empty.")
            else:
                print("\n--- Current Stock ---")
                # The table header
                print(f"{'Item Name':<25} | {'Quantity':>8}")
                # A divider line made by multiplying a hyphen
                print("-" * 36)
                
                # The table rows
                for item, quantity in inventory.items():
                    print(f"{item:<25} | {quantity:>8}")
                    
                # A bottom divider line
                print("-" * 36)
                    
        elif choice == '3':
            # NEW: Automatically title-case and trim spaces from the input
            item_name = input("Enter the item name you sold: ").title().strip()
            
            if item_name in inventory:
                try:
                    sell_qty = int(input(f"How many '{item_name}' did you sell? "))
                    
                    if sell_qty > inventory[item_name]:
                        print(f"Error: You only have {inventory[item_name]} in stock!")
                    elif sell_qty <= 0:
                        print("Error: Please enter a number greater than 0.")
                    else:
                        # Subtract the quantity
                        inventory[item_name] -= sell_qty
                        
                        # NEW: Check if the stock is now zero
                        if inventory[item_name] == 0:
                            del inventory[item_name]
                            print(f"Sale recorded! '{item_name}' is now completely out of stock and removed.")
                        else:
                            print(f"Sale recorded! Remaining '{item_name}': {inventory[item_name]}")
                        
                        # Save the updated data (happens whether it was deleted or just reduced)
                        with open("inventory_data.json", "w") as file:
                            json.dump(inventory, file)
                except ValueError:
                    print("Error: Please enter a valid whole number.")
            else:
                print(f"Error: '{item_name}' was not found in your inventory.")
                
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()