# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# Rakshit, 2024-12-11, Created Script
# ------------------------------------------------------------------------------------------------- #
from data_classes import Employee

class IO:
    """
    A class for handling input and output operations with the user.

    Methods:
    output_error_messages: Displays error messages to the user.
    output_menu: Displays the menu to the user.
    input_menu_choice: Accepts a menu choice from the user.
    output_employee_data: Displays employee data to the user.
    input_employee_data: Accepts new employee data from the user.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays an error message to the user.

        :param message: The error message to display.
        :param error: An optional exception object that provides more details.
        """
        print(message, end="\n\n")
        if error:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        Displays the menu to the user.

        :param menu: The string containing the menu options.
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        Prompts the user to select a menu option.

        :return: The menu choice entered by the user.
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Invalid choice! Please choose between 1 and 4.")
        except Exception as e:
            IO.output_error_messages(str(e))
        return choice

    @staticmethod
    def output_employee_data(employee_data: list):
        """
        Displays the list of employee data to the user.

        :param employee_data: The list of employee objects to display.
        """
        print()
        print("-" * 50)
        for employee in employee_data:
            print(f'{employee.first_name} {employee.last_name} is rated as {employee.review_rating}')
        print("-" * 50)

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: Employee):
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param employee_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            # Input the data
            employee_object = employee_type()
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data