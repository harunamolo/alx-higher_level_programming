#!/usr/bin/python3
"""square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """size needs to be an int
        """

        self.width = value
        self.height = value

    def __str__(self):
        """Returns formatted information display
        """

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """Returns a dict representation
        """

        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
