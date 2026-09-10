import json

# --- FILE HANDLING FUNCTIONS ---

def load_inventory():
    try:
        with open("inventory_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_inventory(inventory):
    with open("inventory_data.json", "w") as file:
        json.dump(inventory, file)


# --- CORE LOGIC FUNCTIONS ---

def add_item(inventory):
    item_name = input("Enter the item name: ").title().strip()
    try:
        item_quantity = int(input("Enter the quantity: ")) 
        if item_name in inventory:
            inventory[item_name] += item_quantity
            print(f"Updated! Added {item_quantity} to '{item_name}'. New total: {inventory[item_name]}")
        else:
            inventory[item_name] = item_quantity
            print(f"Success! {item_quantity} '{item_name}' added to stock.")
        
        save_inventory(inventory)
    except ValueError:
        print("Error: Please enter a valid whole number for the quantity.")

def view_inventory(inventory):
    if len(inventory) == 0:
        print("Your inventory is currently empty.")
    else:
        print("\n--- Current Stock ---")
        print(f"{'Item Name':<25} | {'Quantity':>8}")
        print("-" * 36)
        for item, quantity in inventory.items():
            print(f"{item:<25} | {quantity:>8}")
        print("-" * 36)

def sell_item(inventory):
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
                
                if inventory[item_name] == 0:
                    del inventory[item_name]
                    print(f"Sale recorded! '{item_name}' is now completely out of stock and removed.")
                else:
                    print(f"Sale recorded! Remaining '{item_name}': {inventory[item_name]}")
                
                save_inventory(inventory)
        except ValueError:
            print("Error: Please enter a valid whole number.")
    else:
        print(f"Error: '{item_name}' was not found in your inventory.")

# NEW FUNCTION
def calculate_total(inventory):
    if len(inventory) == 0:
        print("Your inventory is currently empty.")
    else:
        # sum() adds up all the numbers, inventory.values() gets just the quantities
        total_items = sum(inventory.values())
        print(f"\nTotal Stock Volume: You have {total_items} items currently in stock.")


# --- MAIN MENU ---

def main():
    print("Welcome to the Inventory Manager!")
    inventory = load_inventory()
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add or restock an item")
        print("2. View all items")
        print("3. Sell an item")
        print("4. Calculate total stock volume") # NEW MENU ITEM
        print("5. Exit") # MOVED TO 5
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            view_inventory(inventory)
        elif choice == '3':
            sell_item(inventory)
        elif choice == '4':
            calculate_total(inventory) # NEW FUNCTION CALL
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()