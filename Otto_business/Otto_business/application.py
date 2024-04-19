

class Application:
    def __init__(self):
        self.applications = {}

    def submit_application(self, application_id, name, position):
        """
        Submit a job application.

        Args:
            application_id (int): The unique identifier for the application.
            name (str): The name of the applicant.
            position (str): The position applied for.

        Returns:
            str: Confirmation message.
        """
        if application_id in self.applications:
            return f"Application with ID {application_id} already exists."
        self.applications[application_id] = {'name': name, 'position': position}
        return f"Application submitted successfully with ID {application_id}."

    def get_application_info(self, application_id):
        """
        Retrieve information about a job application.

        Args:
            application_id (int): The unique identifier for the application.

        Returns:
            dict: Information about the application if found, None otherwise.
        """
        return self.applications.get(application_id)

    def remove_application(self, application_id):
        """
        Remove a job application.

        Args:
            application_id (int): The unique identifier for the application.

        Returns:
            str: Confirmation message.
        """
        if application_id not in self.applications:
            return f"Application with ID {application_id} not found."
        del self.applications[application_id]
        return f"Application with ID {application_id} removed successfully."
    
