#!/usr/bin/python3
"""Create a Class  Student"""


class Student:
    """ class to create a dict obj """

    def __init__(self, first_name, last_name, age):
        """ initialization for Student object """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self):
        """ retrieves a dictionary representation """
        return self.__dict__
