from inventory import *
import datetime as dt 
import qrcode as qr 


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.purchaseDate = dt.datetime.now()
       
class POS:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def print_receipt(self):
        print("Receipt:")
        for product in self.products:
            print(f"{product.name}: ${product.price:.2f}\n")
        print(f"Total: ${self.calculate_total():.2f}\n")

    def process_payment(self, amount_paid):
        total = self.calculate_total()
        if amount_paid < total:
            print("Insufficient payment.")
            return False
        else:
            change = amount_paid - total
            print(f"Payment successful. Change: ${change:.2f}")
            self.products = []
            return True

def mainPOS():
    pos = POS()
    while True:
        print("\nOptions:")
        print("1. Add Product")
        print("2. Calculate Total")
        print("3. Print Receipt")
        print("4. Process Payment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            product = Product(name, price)
            pos.add_product(product)
            print("Product added.")
        elif choice == '2':
            total = pos.calculate_total()
            print(f"Total: ${total:.2f}")
        elif choice == '3':
            pos.print_receipt()
        elif choice == '4':
            amount_paid = float(input("Enter amount paid: "))
            pos.process_payment(amount_paid)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

