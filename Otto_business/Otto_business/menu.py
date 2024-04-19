import sys 
import random

# Define menu items
appetizers = ['Curly Fries', 'Crinkle Fries', 'Mozerella Sticks', 'Stuffed Mushrooms', 'Calamari']
main_courses = ['Steak and Cheese', 'Cheese Burger', 'Hamburger', 'Chili Dog', 'Hamburger']
drinks = ['Pepsi', 'Coke', 'Sweet Tea', 'Can Drinks', '2-liters']

# Generate a random ordering menu
def generate_menu():
    menu = {
        'Appetizers': random.sample(appetizers, k=random.randint(1, 3)),
        'Main Courses': random.sample(main_courses, k=random.randint(1, 3)),
        'Desserts': random.sample(drinks, k=random.randint(1, 2))
    }
    return menu

# Print the menu
def print_menu(menu):
    for category, items in menu.items():
        print(category)
        for item in items:
            print("-", item)
        print()

# Generate and print the menu
random_menu = generate_menu()
#print_menu(random_menu)

    
def empMenu():
    print("Employee Menu.\n")
    print("In - Clock-In")
    print("Out - to Clock-Out.\n")
    print("Time - to view weekly schedule and work hours.\n")
    print("Off - to request time off.\n")
    print("Exit - return to main menu\n")
    
def customerMenu():
    print("Customer Menu.\n")
    print("Order - to place an order.\n")
    print("Work - to fill out application.\n")
    print("Set - to manage settings.\n")
    print("Exit - to return to main menu.\n")
     
def manMenu():
    print("Manager Menu.\n")
    print("1 - to manage employees.\n")
    print("2 - to view sales, revenue and profit reports.\n")
    print("3 - to access and manage the inventory.\n")
    print("4 - to return to main menu.\n")
    
def select():
    select = input("Choose a command from the menu.\n")
    return select 

def killApp():
    print("GoodBye! \n Have a nice day!\n")
    sys.exit()
    
    


    
    
    
    
