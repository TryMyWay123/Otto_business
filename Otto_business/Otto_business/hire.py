class Hire:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, full_name, age, telephone, email, address, position):
        """
        Add a new employee to the hiring system.

        Args:
            employee_id (int): The unique identifier for the employee.
            full_name (str): The full name of the employee.
            age (int): The age of the employee.
            telephone (str): The telephone number of the employee.
            email (str): The email address of the employee.
            address (str): The address of the employee.
            position (str): The position of the employee.

        Returns:
            str: Confirmation message.
        """
        if employee_id in self.employees:
            return f"Employee with ID {employee_id} already exists."
        self.employees[employee_id] = {
            'full_name': full_name,
            'age': age,
            'telephone': telephone,
            'email': email,
            'address': address,
            'position': position
        }
        return f"Employee {full_name} hired successfully with ID {employee_id}."

    def get_employee_info(self, employee_id):
        """
        Retrieve information about an employee.

        Args:
            employee_id (int): The unique identifier for the employee.

        Returns:
            dict: Information about the employee if found, None otherwise.
        """
        return self.employees.get(employee_id)

    def remove_employee(self, employee_id):
        """
        Remove an employee from the hiring system.

        Args:
            employee_id (int): The unique identifier for the employee.

        Returns:
            str: Confirmation message.
        """
        if employee_id not in self.employees:
            return f"Employee with ID {employee_id} not found."
        del self.employees[employee_id]
        return f"Employee with ID {employee_id} removed successfully."
