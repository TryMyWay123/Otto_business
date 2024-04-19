import random as rand
import pandas as pd 

class Employee:
    TAX_RATE = 0.12

    def __init__(self, emp_id, first_name, last_name, hours, pay):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.hours = hours
        self.pay = pay
        self.gross_pay = self.calculate_gross_pay()
        self.tax = self.calculate_tax()
        self.net_pay = self.calculate_net_pay()

    def calculate_gross_pay(self):
        return self.hours * self.pay

    def calculate_tax(self):
        return self.TAX_RATE * self.gross_pay

    def calculate_net_pay(self):
        return self.gross_pay - self.tax

    @classmethod
    def from_user_input(cls):
        emp_id = rand.randint(100, 999)
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        hours = int(input("Enter employee's hours: "))
        pay = int(input("Enter the employee's hourly wage: "))
        return cls(emp_id, first_name, last_name, hours, pay)

    def manage_schedule(self, emp_id, schedule):
        # Assuming EmployeeSchedule is another class to manage schedule
        employee_schedule = EmployeeSchedule(emp_id)
        for day, start_time, end_time in schedule:
            employee_schedule.add_schedule(day, start_time, end_time)
        employee_schedule.save_schedule()

class EmployeeSchedule:
    def __init__(self, emp_id):
        self.emp_id = emp_id
        self.schedule = []

    def add_schedule(self, day, start_time, end_time):
        self.schedule.append((day, start_time, end_time))

    def save_schedule(self):
        # Some logic to save schedule, maybe to a database or file
        pass
    