# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# Rakshit, 2024-12-11, Created Script
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee
from processing_classes import FileProcessor
from presentation_classes import IO

FILE_NAME = 'EmployeeRatings.json'
MENU = '''
---- Employee Ratings ------------------------------
 Select from the following menu:
   1. Show current employee rating data.
   2. Enter new employee rating data.
   3. Save data to a file.
   4. Exit the program.
--------------------------------------------------
'''

employees = []  # a table of employee data
menu_choice = ''

# Read data from file
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)

while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to {FILE_NAME}.")
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break
    else:
        print("Please only choose option 1, 2, 3 or 4")

print("Program Ended")