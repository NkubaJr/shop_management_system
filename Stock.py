#!/usr/bin/bash python3
class Shop:
    def main(self):
        """Display the menu and handle user choices."""
        while True:
            print("\nShop Management System")
            print("1. Add item")
            print("2. View items")
            print("3. Delete an item")
            print("4. Update an item")
            print("5. Search for an item")
            print("6. Exit")
#User to enter choice of action to run

	    choice = input("Choose an option: ")

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.view_items()
            elif choice == "3":
                self.delete_item()
            elif choice == "4":
                self.update_item()
            elif choice == "5":
                self.search_item()
            elif choice == "6":
                print("Exiting the system...")
                self.conn.close()
                break
            else:
                print("Invalid choice. Please try again.")
    def view_items(self):
        """Retrieves and displays all items in the database."""
        self.cursor.execute("SELECT * FROM items")
        items = self.cursor.fetchall()

        if not items:
            print("No items available.")
        else:
            print("\nItems in the shop:")
            for item in items:
                print(f"ID: {item[0]}, Name: {item[1]}, Price: ${item[2]}, Quantity: {item[3]}")

#run the program 
shop = Shop()
shop.main()
