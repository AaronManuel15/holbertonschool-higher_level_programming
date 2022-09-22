#!/usr/bin/python3
""" Project 0x0C. Python - Almost a circle
    Task 10
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a Square based on Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes attributes for a square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size
        """
        return self.height

    @size.setter
    def size(self, value):
        """ Setter for size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ String description of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute
        """
        if len(args) > 0:
            attribute = ['id', 'size', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, attribute[arg], args[arg])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
