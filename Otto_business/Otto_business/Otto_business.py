from register import *
from emp import *
from inventory import *
from hire import *
from application import *
from reports import *
from POS import *
from menu import *
import random as rand
import time

import time

class Time:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def startTimer(self):
        self.start_time = time.time()

    def stopTimer(self):
        self.end_time = time.time()

    def totalTime(self):
        if self.start_time is None or self.end_time is None:
            return "Timer not started or stopped."
        return round(self.end_time - self.start_time, 2)

    def clearTimer(self):
        self.start_time = None
        self.end_time = None

class Customer:
    def __init__(self):
        self.register = Register()
        self.logon = Login.login()
        self.menu = customerMenu()
        self.orderMenu = random_menu = generate_menu()
        
    def displayMenu(self):
        print(self.customerMenu)
        command = select()
          
    def displayApp():
        app = Application()
        app.submit_application(1, 'Jane Doe', 'Waitress')
        app.submit_application(2, 'John Doe', 'Cook')
        return app
    
    def pointOfSale():
        mainPOS()
    
    def exit():
        log_out = Login.logout()
        sys.exit()
        
class Employee:
    def __init__(self):
        self.register = Register()
        self.empID = rand.randint(100, 999)
        self.logon = Login.login()
        self.menu = empMenu()
        
    def displayMenu(self):
        print(self.empMenu)
        command = select()
        
    def empTime():
        timer = Time()
        timer.startTimer()
        time.sleep(8 * 3600)  # 8 hours shift (8 hours * 3600 seconds per hour)
        timer.stopTimer()
        print("Total time elapsed:", timer.totalTime())
        timer.clearTimer()
        print("Timer cleared.")
    empTime()

    def exit():
        log_out = Login.logout()
        sys.exit()
            
class Manager:
    def __init__(self):
        self.register = Register()
        self.manID = rand.randint(1000, 9999)
        self.logon = Login.login()
        self.menu = manMenu()
        self.stock = stock()
        
    def manMenu(self):
        print(self.manMenu)
        command = select()
        
    def manInventroy():
        stock()
        
    def exit(self):
        log_out = Login.logout()
        sys.exit()
    
    def manInventroy():
        stock()
        
def startApp():
    access_id = input("Enter username or access SID.\n")
    if access_id == 3:
      employee = Employee()
      employee.empMenu()
    elif access_id == 4:
       manager = Manager()
       manager.manMenu()
    else:
        customer = Customer()
        customer.displayMenu()
    return customer 
        
     
if __name__ == "__main__":
    print("Hello, I am Otto. Remote Automated Business Assistant.\n")
    print("Starting Application.\n")
    start_up = startApp()
    
    
    
        
    
    
    
    
    
    
   
    
    
     

        
        
    
    
    
    
    
    
    
    
    
    
