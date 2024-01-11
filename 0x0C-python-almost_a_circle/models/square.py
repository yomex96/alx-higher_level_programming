#!/usr/bin/python3
"""module to print a Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square

        def __init__
        def size @property/@size.setter
        def __str__
        def update
        def to_dictionary
    """
    def __init__(self, size, x=0, y=0, id=None):
        """function __init__

            Args:
                size(int): size square
                x(int): offset of the square right/left
                y(int): offset of the square top/bottom
                id(int): the id of the square

            Return:
                no return
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """function size(property)

            Args:
                number(int): size value

            Return:
                size value
        """
        return(self.width)

    @size.setter
    def size(self, number):
        """function size(size.setter)

            Args:
                number(int): size value

            Return:
                no return
        """
        self.width = number
        self.height = number

    def __str__(self):
        """function __str__

            Args:
                no args

            Return:
                return square all value
        """
        return("[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width))

    def update(self, *args, **kwargs):
        """function update

            Args:
                args(list): list of the value of the square
                kwargs(list of list): list of the value with the name

            Return:
                no return
        """
        if args != 0 and len(args) != 0:
            i = 0
            for arguments in args:
                if i == 0:
                    if arguments is not None:
                        self.id = arguments
                    else:
                        self.__init__(self.size, self.x, self.y)
                elif i == 1:
                    self.size = arguments
                elif i == 2:
                    self.x = arguments
                elif i == 3:
                    self.y = arguments
                i += 1

        elif kwargs != 0 and len(kwargs) != 0:
            for key, number in kwargs.items():
                if key == "size":
                    self.size = number
                elif key == "x":
                    self.x = number
                elif key == "y":
                    self.y = number
                elif key == "id":
                    if number is not None:
                        self.id = number
                    else:
                        self.__init__(self.size, self.x, self.y)

    def to_dictionary(self):
        """function to_dictionary

            Args:
                no args

            Return:
                dict of the square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
