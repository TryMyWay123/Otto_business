
class Register:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose a different username.\n")
            return False
        else:
            self.users[username] = password
            print("User registered successfully!\n")
            return True

    def get_user_password(self, username):
        return self.users.get(username)
    
           
class FileHandler:
    @staticmethod
    def save_user_info(username, password, filename):
        with open(filename, "a") as f:
            f.write(f"{username},{password}\n")

    @staticmethod
    def read_user_info(filename):
        user_info = {}
        try:
            with open(filename, "r") as f:
                for line in f:
                    username, password = line.strip().split(',')
                    user_info[username] = password
        except FileNotFoundError:
            print("File not found.")
        return user_info


def register():
    registration_system = Register()
    user_file = "users.txt"
    # Load existing user information from file
    #registration_system.users = FileHandler.read_user_info(user_file) modify parameter
    new_username = input("Enter a username: \n")
    new_password = input("Enter a password: \n")
    if registration_system.register_user(new_username, new_password):
        # Save new user information to file
        FileHandler.save_user_info(new_username, new_password, user_file) #modify parameter user_file
    else:
        # Handle the case where the username is already taken.
        username_to_check = input("Enter the username to retrieve the password: ")
        retrieved_password = registration_system.get_user_password(username_to_check)
        if retrieved_password is not None:
            print(f"The password for {username_to_check} is: {retrieved_password}")
        else:
            print(f"No user found with the username {username_to_check}.")

class Login:
    def __init__(self, stored_username, stored_password):
        self.username = stored_username
        self.password = stored_password
        self.is_authenticated = False
        
    def login():
        user_input_username = input("Enter your username: \n")
        user_input_password = input("Enter your password: \n")
        login_attempt = Login(user_input_username, user_input_password)
        if login_attempt.authenticate(user_input_username, user_input_password):
            print("Login successful!")
        # Proceed with user-specific tasks
        # For example: access to certain features or data
            login_attempt.logout()
        else:
            print("Invalid username or password. Please try again.")
        
    def authenticate(self, stored_username, stored_password):
        with open("users.txt", "r") as f: #modify code for customer, emp, and man files 
            lines = ''
            for l in lines:
                l = f.readlines()
                return l
        if self.username == stored_username and self.password == stored_password:
            self.is_authenticated = True
            return True
        else:
            return False

    def logout(self):
        self.is_authenticated = False
        print("Logged out successfully.")


        

        
        