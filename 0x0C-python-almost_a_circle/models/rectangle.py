#!/usr/bin/python3
"""module to print a Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle

        def __init__
        def width @property/@width.setter
        def height @property/@height.setter
        def x @property/@x.setter
        def y @property/@y.setter
        def area
        def display
        def __str__
        def update
        def to_dictionary
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """function __init__

            Args:
                width(int): width square
                height(int): height square
                x(int): offset of the square right/left
                y(int): offset of the square top/bottom
                id(int): the id of the square

            Return:
                no return
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """function width(property)

            Args:
                number(int): width value

            Return:
                width value
        """
        return(self.__width)

    @width.setter
    def width(self, number):
        """function width(width.setter)

            Args:
                number(int): width value

            Return:
                no return
        """
        if type(number) is not int:
            raise TypeError("width must be an integer")
        if number <= 0:
            raise ValueError("width must be > 0")
        self.__width = number

    @property
    def height(self):
        """function height(property)

            Args:
                number(int): height value

            Return:
                height value
        """
        return(self.__height)

    @height.setter
    def height(self, number):
        """function height(height.setter)

            Args:
                number(int): height value

            Return:
                no return
        """
        if type(number) is not int:
            raise TypeError("height must be an integer")
        if number <= 0:
            raise ValueError("height must be > 0")
        self.__height = number

    @property
    def x(self):
        """function x(property)

            Args:
                number(int): x value

            Return:
                x value
        """
        return(self.__x)

    @x.setter
    def x(self, number):
        """function x(x.setter)

            Args:
                number(int): x value

            Return:
                no return
        """
        if type(number) is not int:
            raise TypeError("x must be an integer")
        if number < 0:
            raise ValueError("x must be >= 0")
        self.__x = number

    @property
    def y(self):
        """function y(property)

            Args:
                number(int): y value

            Return:
                y value
        """
        return(self.__y)

    @y.setter
    def y(self, number):
        """function y(y.setter)

            Args:
                number(int): y value

            Return:
                no return
        """
        if type(number) is not int:
            raise TypeError("y must be an integer")
        if number < 0:
            raise ValueError("y must be >= 0")
        self.__y = number

    def area(self):
        """function area

            Args:
                no args

            Return:
                the area of the square
        """
        return(self.width * self.height)

    def display(self):
        """function display

            Args:
                no args

            Return:
                no return

            Print:
                the rectangle
        """
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """function __str__

            Args:
                no args

            Return:
                return rectangle all value
        """
        return("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height))

    def update(self, *args, **kwargs):
        """function update

            Args:
                args(list): list of the value of the rectangle
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
                        self.__init__(self.width, self.height, self.x, self.y)
                elif i == 1:
                    self.width = arguments
                elif i == 2:
                    self.height = arguments
                elif i == 3:
                    self.x = arguments
                elif i == 4:
                    self.y = arguments
                i += 1

        elif kwargs != 0 and len(kwargs) != 0:
            for key, number in kwargs.items():
                if key == "width":
                    self.width = number
                elif key == "height":
                    self.height = number
                elif key == "x":
                    self.x = number
                elif key == "y":
                    self.y = number
                elif key == "id":
                    if number is not None:
                        self.id = number
                    else:
                        self.__init__(self.width, self.height, self.x, self.y)

    def to_dictionary(self):
        """function to_dictionary

            Args:
                no args

            Return:
                dict of the rectangle
        """
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
