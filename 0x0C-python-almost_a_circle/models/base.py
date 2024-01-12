#!/usr/bin/python3
"""module to have the base"""
import json
import csv
from os.path import exists



class Base:
    """class Base

        def __init__
        def to_json_string(staticmethod)
        def save_to_file(classmethod)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """function __init__

            Args:
                id(int): the id of the base

            Return:
                no return
        """
        self.__id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function to_json_string

            Args:
                list_dictionaries(list): list of the dict

            Return:
                dict of the base
        """
        if list_dictionaries == [] or list_dictionaries is None:
            return("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """function save_to_file

            Args:
                list_objs(list): list of the object

            Return:
                object of the base
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                count = len(list_objs) - 1
                f.write('[')
                for i in list_objs:
                    dict = i.to_dictionary()
                    f.write(Base.to_json_string(dict))
                    if count > 0:
                        f.write(", ")
                        count -= 1
                f.write(']')

    @staticmethod
    def from_json_string(json_string):
        """function from_json_string

            Args:
                json_string(str): json string

            Return:
                json loads
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function create

            Args:
                dictionary(str): dictionary

            Return:
                dictionary add
        """
        name = cls.__name__
        if (dictionary != {} and dictionary):
            if name == "Rectangle":
                add = cls(1, 1)
            else:
                add = cls(1)
            add.update(**dictionary)
            return(add)

    @classmethod
    def load_from_file(cls):
        """function load_from_file

            Args:
                no args

            Return:
                load file
        """
        name = cls.__name__ + ".json"
        try:
            with open(name, "r") as f:
                dict = Base.from_json_string(f.read())
                return [cls.create(**i) for i in dict]
        except IOError:
            return([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """function save_to_file_csv

            Args:
                list_objs(list): object list

            Return:
                no return
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs == [] or list_objs is None:
                f.write("")
            else:
                if cls.__name__ == "Rectangle":
                    paramters = ["id", "width", "height", "x", "y"]
                else:
                    paramters = ["id", "size", "x", "y"]
                w = csv.DictWriter(f, fieldnames=paramters)
                for obj in list_objs:
                    w.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """function load_from_file_csv

            Args:
                no args

            Return:
                dict and file load
        """
        filename = cls.__name__ + ".csv"
        listOfObjs = []
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                for elem in reader:
                    if cls.__name__ == "Rectangle":
                        newObj = {
                            "id": int(elem[0]),
                            "width": int(elem[1]),
                            "height": int(elem[2]),
                            "x": int(elem[3]),
                            "y": int(elem[4]),
                        }
                    else:
                        newObj = {
                            "id": int(elem[0]),
                            "size": int(elem[1]),
                            "x": int(elem[2]),
                            "y": int(elem[3]),
                        }
                    newObj = cls.create(**newObj)
                    listOfObjs.append(newObj)
            return listOfObjs
        except FileExistsError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """function draw

            Args:
                list_rectangles
                list_squares

            Return:
                xxx
        """
        return(0)
