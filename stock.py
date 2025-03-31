#!/usr/bin/env python3
import mysql.connector

class Shop:
    def __init__(self):
        """Initialize the MySQL database connection."""
        print("=" * 50)
        print("🎉 Welcome to the Shop Management System 🎉")
        print("📦 Manage your shop with ease and efficiency!")
        print("=" * 50)
        
        self.conn = mysql.connector.connect(
            host="localhost",  # Assuming MySQL is running locally
            user="shop_user",  # The new user you created
            password="shop_password",  # The password you set for the new user
            database="shop_db"  # The database name
        )
        self.cursor = self.conn.cursor()

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

    def add_item(self):
        """Adds an item to the database."""
        name = input("Enter the item name: ")
        try:
            price = float(input("Enter the item price: "))  # Ensure it's a float
            quantity = int(input("Enter the quantity: "))  # Ensure it's an integer

            # Insert the item into the database
            self.cursor.execute(
                "INSERT INTO items (name, price, quantity) VALUES (%s, %s, %s)", 
                (name, price, quantity)
            )
            self.conn.commit()
            print(f"Item '{name}' added successfully!")
        except ValueError:
            print("Invalid input for price or quantity. Please enter valid numbers.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def view_items(self):
        """Retrieves and displays all items in the database."""
        self.cursor.execute("SELECT * FROM items")
        items = self.cursor.fetchall()

        if not items:
            print("No items available.")
        else:
            print("\nItems in the shop:")
            for item in items:
                print(f"ID: {item[0]}, Name: {item[1]}, Price: ${item[2]:.2f}, Quantity: {item[3]}")

    def delete_item(self):
        """Deletes an item from the database by name."""
        name = input("Enter the name of the item to delete: ")
        self.cursor.execute("DELETE FROM items WHERE name = %s", (name,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Item '{name}' deleted successfully!")
        else:
            print("Item not found.")

    def update_item(self):
        """Updates the price and quantity of an item in the database."""
        name = input("Enter the name of the item to update: ")
        try:
            new_price = float(input("Enter the new price: "))  # Ensure it's a float
            new_quantity = int(input("Enter the new quantity: "))  # Ensure it's an integer

            # Update the item in the database
            self.cursor.execute(
                "UPDATE items SET price = %s, quantity = %s WHERE name = %s",
                (new_price, new_quantity, name)
            )
            if self.cursor.rowcount > 0:
                self.conn.commit()
                print(f"Item '{name}' updated successfully!")
            else:
                print("Item not found.")
        except ValueError:
            print("Invalid input for price or quantity. Please enter valid numbers.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def search_item(self):
        """Searches for an item in the database by name."""
        name = input("Enter the name of the item to search for: ")
        self.cursor.execute("SELECT * FROM items WHERE name = %s", (name,))
        item = self.cursor.fetchone()

        if item:
            print(f"Found item: ID: {item[0]}, Name: {item[1]}, Price: ${item[2]:.2f}, Quantity: {item[3]}")
        else:
            print("Item not found.")


# Run the program
if __name__ == "__main__":
    shop = Shop()
    shop.main()

