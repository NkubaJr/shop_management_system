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
#run the program 
shop = Shop()
shop.main()
