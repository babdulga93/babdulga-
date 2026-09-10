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
                for item, quantity in inventory.items():
                    print(f"{item}: {quantity}")
                    
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
                        inventory[item_name] -= sell_qty
                        print(f"Sale recorded! Remaining '{item_name}': {inventory[item_name]}")
                        
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