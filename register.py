import getpass
import os
import mysql.connector


class Users:
    def __init__(self):
        self.name = None
        self.age = None
        self.login = None
        self.password = None
        self.options = ['1', '2', '3']
        self.list_login = []
        self.get_login()

    def entrance_system(self):
        self.clear_screen()
        self.print_first_message()
        input_choice = input(">>>: ").strip()
        while self.is_string_empty(input_choice) or input_choice not in self.options[:2]:
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
        while self.is_string_empty(input_login) or not input_login.isalnum() or input_login in self.list_login:
            self.clear_screen()
            input_login = input("Login: ").strip().lower()

        input_password = getpass.getpass("Password: ").strip()
        check_password = getpass.getpass("Confirm: ").strip()
        while self.is_string_empty(input_password) or input_password != check_password:
            self.clear_screen()
            input_password = getpass.getpass("Password: ").strip()
            check_password = getpass.getpass("Confirm: ").strip()

        self.name = input_name
        self.age = input_age
        self.login = input_login
        self.password = input_password
        self.write_to_database()
        self.entrance_system()

    def log_in(self):
        self.clear_screen()

        input_login = input("Login: ").strip().lower()
        while self.is_string_empty(input_login) or input_login not in self.list_login:
            self.clear_screen()
            input_login = input("Login: ").strip().lower()

        self.login = input_login

        input_password = input("Password: ").strip()
        while self.is_string_empty(input_password) or self.password_true_of_login(input_password):
            self.clear_screen()
            input_password = input("Password: ").strip()

        self.clear_screen()
        self.print_second_message()
        input_choice = input(">>>: ").strip()
        while self.is_string_empty(input_choice) or input_choice not in self.options:
            self.clear_screen()
            self.print_second_message()
            input_choice = input(">>>: ").strip()

        if input_choice == self.options[0]:
            self.update_login_and_password()
        elif input_choice == self.options[1]:
            self.delete_account()
        else:
            self.log_out()


    def update_login_and_password(self):
        pass

    def delete_account(self):
        pass

    def log_out(self):
        self.clear_screen()
        print("\n\n\t\tHave a good day!")

    # __________Messages_____________

    @staticmethod
    def print_first_message():
        print("""
        Register [1]
        Login    [2]
        """)

    @staticmethod
    def print_second_message():
        print("""
        Update Login and Password [1]
        Delete Account            [2]
        Log Out                   [3]
        """)

    # __________Functions______________

    @staticmethod
    def clear_screen():
        os.system("clear")

    @staticmethod
    def is_string_empty(str_):
        return not bool(str_)

    @staticmethod
    def entrance_database():
        return mysql.connector.connect(
            host="localhost",
            user="Fayzullo",
            password="77777777",
            database='Register'
        )

    def write_to_database(self):
        my_db = self.entrance_database()
        my_cursor = my_db.cursor()
        my_cursor.execute(f"insert into users (Name, Age, Login, Password) values ('{self.name}', {self.age}, '{self.login}', '{self.password}')")
        my_db.commit()

    def get_login(self):
        my_db = self.entrance_database()
        my_cursor = my_db.cursor()
        my_cursor.execute("select Login from users")
        all_login = my_cursor.fetchall()
        for a in all_login:
            self.list_login.append(a[0])

    def password_true_of_login(self, password):
        my_db = self.entrance_database()
        my_cursor = my_db.cursor()
        my_cursor.execute(f"select password from users where Login='{self.login}'")
        password1 = my_cursor.fetchall()
        if password1[0][0] == password:
            return False
        else:
            return True


users = Users()
users.entrance_system()

