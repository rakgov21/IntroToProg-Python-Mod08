# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# Rakshit, 2024-12-11, Created Script
# ------------------------------------------------------------------------------------------------- #

from datetime import date

class Person:
    """
    A class representing a person with basic attributes like first and last names.

    Attributes:
    first_name (str): The person's first name.
    last_name (str): The person's last name.
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        """
        Initialize a Person object with a first name and a last name.

        :param first_name: The first name of the person. Defaults to an empty string.
        :param last_name: The last name of the person. Defaults to an empty string.
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """
        Get the person's first name, capitalized.

        :return: The capitalized first name of the person.
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """
        Set the person's first name. Validates that it contains only alphabetic characters.

        :param value: The first name to set.
        :raises ValueError: If the first name contains non-alphabetic characters.
        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self):
        """
        Get the person's last name, capitalized.

        :return: The capitalized last name of the person.
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """
        Set the person's last name. Validates that it contains only alphabetic characters.

        :param value: The last name to set.
        :raises ValueError: If the last name contains non-alphabetic characters.
        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        """
        Returns a string representation of the person's full name.

        :return: A string containing the full name of the person.
        """
        return f"{self.first_name},{self.last_name}"


class Employee(Person):
    """
    A class representing an employee with review details, extending the Person class.

    Attributes:
    first_name (str): The employee's first name.
    last_name (str): The employee's last name.
    review_date (str): The date of the employee's review (format: YYYY-MM-DD).
    review_rating (int): The review rating of the employee (1-5).
    """

    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):
        """
        Initialize an Employee object with review information.

        :param first_name: The first name of the employee.
        :param last_name: The last name of the employee.
        :param review_date: The review date of the employee in YYYY-MM-DD format.
        :param review_rating: The review rating of the employee (1-5).
        """
        super().__init__(first_name=first_name, last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        """
        Get the employee's review date.

        :return: The review date as a string (YYYY-MM-DD).
        """
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        """
        Set the employee's review date. Validates that the date is in the correct format (YYYY-MM-DD).

        :param value: The review date in YYYY-MM-DD format.
        :raises ValueError: If the date format is invalid.
        """
        try:
            date.fromisoformat(value)  # Ensures the date is in the correct format.
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        """
        Get the employee's review rating.

        :return: The review rating (int between 1 and 5).
        """
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: int):
        """
        Set the employee's review rating. Ensures the rating is between 1 and 5.

        :param value: The review rating (int between 1 and 5).
        :raises ValueError: If the rating is not between 1 and 5.
        """
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose a rating between 1 and 5")

    def __str__(self):
        """
        Returns a string representation of the employee's full details.

        :return: A string containing the employee's full name, review date, and rating.
        """
        return f"{self.first_name},{self.last_name},{self.review_date},{self.review_rating}"
