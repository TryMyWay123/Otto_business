import pandas as pd

class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self):
        name = input("Enter the item name to add to inventory: \n")
        quantity = int(input("Enter the quantity: \n"))
        price = float(input("Enter the price: \n"))
        item = InventoryItem(name, quantity, price)
        self.items.append(item)
        
    def remove_item(self):
        name = input("Enter the item name to remove from inventory: \n")
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"{name} removed from inventory.\n")
                return
        print(f"{name} not found in inventory.\n")

    def display_inventory(self):
        print("Inventory:\n")
        if not self.items:
            print("Inventory is empty.")
            return
        else:
            inventory_data = {'Name': [], 'Quantity': [], 'Price': []}
            for item in self.items:
                inventory_data['Name'].append(item.name)
                inventory_data['Quantity'].append(item.quantity)
                inventory_data['Price'].append(item.price)
            df = pd.DataFrame(inventory_data)
            print(df)

def stock():
    inventory = Inventory()
    while True:
        print("\n1. Add Item\n2. Remove Item\n3. Display Inventory\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): \n")
        if choice == '1':
            inventory.add_item()
        elif choice == '2':
            inventory.remove_item()
        elif choice == '3':
            inventory.display_inventory()
        elif choice == '4':
            print("Exiting program. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")

