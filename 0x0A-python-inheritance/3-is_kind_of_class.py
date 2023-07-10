#!/usr/bin/python3
"""same class or inherit fro"""


def is_kind_of_class(obj, a_class):
    """
    is kind of class
    Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        True if obj is instance or inherited instance of a_class,
        False otherwise.
        """
    if isinstance(obj, a_class):
        return True
    else:
        False
