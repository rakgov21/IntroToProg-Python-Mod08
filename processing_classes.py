# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# Rakshit, 2024-12-11, Created Script
# ------------------------------------------------------------------------------------------------- #

import json
from data_classes import Employee

class FileProcessor:
    """
    A class for handling file reading and writing operations related to employee data.

    Methods:
    read_employee_data_from_file: Reads employee data from a JSON file.
    write_employee_data_to_file: Writes employee data to a JSON file.
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee):
        """
        Reads employee data from a JSON file and loads it into a list of Employee objects.

        :param file_name: The name of the file to read the data from.
        :param employee_data: A list to hold the employee objects that are read from the file.
        :param employee_type: The type of employee objects to create (Employee class).
        :return: A list of Employee objects.
        :raises FileNotFoundError: If the specified file is not found.
        :raises Exception: If any other error occurs during the reading process.
        """
        try:
            with open(file_name, "r") as file:
                list_of_dict_data = json.load(file)
                for employee in list_of_dict_data:
                    employee_obj = employee_type()
                    employee_obj.first_name = employee["FirstName"]
                    employee_obj.last_name = employee["LastName"]
                    employee_obj.review_date = employee["ReviewDate"]
                    employee_obj.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_obj)
        except FileNotFoundError:
            raise FileNotFoundError("File not found!")
        except Exception as e:
            raise Exception(f"Error while reading file: {e}")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        Writes employee data to a JSON file.

        :param file_name: The name of the file to write the data to.
        :param employee_data: A list of employee objects to be written to the file.
        :raises Exception: If an error occurs while writing the data to the file.
        """
        try:
            list_of_dict_data = []
            for employee in employee_data:
                employee_json = {
                    "FirstName": employee.first_name,
                    "LastName": employee.last_name,
                    "ReviewDate": employee.review_date,
                    "ReviewRating": employee.review_rating
                }
                list_of_dict_data.append(employee_json)
            with open(file_name, "w") as file:
                json.dump(list_of_dict_data, file, indent=4)
        except Exception as e:
            raise Exception(f"Error while writing to file: {e}")