import os


class Users:
    def __init__(self):
        self.name = None
        self.age = None
        self.login = None
        self.password = None
        self.options = ['1', '2']

    def entrance_system(self):
        self.clear_screen()
        self.print_first_message()
        input_choice = input(">>>: ").strip()
        while self.is_string_empty(input_choice) or input_choice not in self.options:
            self.clear_screen()
            self.print_first_message()
            input_choice = input(">>>: ").strip()

        if input_choice == self.options[0]:
            self.register()
        else:
            self.log_in()

    def register(self):
        self.clear_screen()

        input_name = input("Name: ").strip().capitalize()
        while self.is_string_empty(input_name) or not input_name.isalpha():
            self.clear_screen()
            input_name = input("Name: ").strip().capitalize()

        input_age = input("Age: ").strip()
        while self.is_string_empty(input_age) or not input_age.isnumeric():
            self.clear_screen()
            input_age = input("Age: ").strip()

        input_login = input("Login: ").strip().lower()
        while self.is_string_empty(input_login) or not input_login.isalnum():
            self.clear_screen()
            input_login = input("Login: ").strip().lower()

        input_password = input("Password: ").strip()
        check_password = input("Confirm: ").strip()
        while self.is_string_empty(input_password) or input_password != check_password:
            self.clear_screen()
            input_password = input("Password: ").strip()
            check_password = input("Confirm: ").strip()



    def log_in(self):
        pass

    def update_login_and_password(self):
        pass

    def delete_account(self):
        pass

    def log_out(self):
        pass

    # __________Messages_____________

    @staticmethod
    def print_first_message():
        print("""
        Register [1]
        Login    [2]
        """)

    # __________Functions______________

    @staticmethod
    def clear_screen():
        os.system("clear")

    @staticmethod
    def is_string_empty(str_):
        return not bool(str_)



users = Users()
users.entrance_system()

