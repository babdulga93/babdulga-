def main():
    print("Welcome to the Inventory Manager!")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new item")
        print("2. View all items")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            print("Adding an item... (logic coming soon!)")
        elif choice == '2':
            print("Viewing items... (logic coming soon!)")
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()