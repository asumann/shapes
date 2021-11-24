import sys
import os
from math import pi

class Circle:

    def __init__(self, radius, fill='red', stroke='black'):
        self._radius = radius
        self._fill = fill
        self._stroke = stroke

    @property
    def radius(self): #public access for ._radius; read-only
        return self._radius

    def calculate_area(self):
        """Calculates the area"""
        return pi * self._radius ** 2

    def __len__(self):
        return int(pi * self._radius * 2)

    def __call__(self):
        return "I am a circle"

    def __repr__(self):
        return f"Circle({self._radius}, fill={self._fill}, stroke={self._stroke})"

class Quadrilateral:

    def __init__(self, width, height, fill= "red", stroke="black"):
        self._width = width
        self._height = height
        self._fill = fill
        self._stroke = stroke

    def calculate_area(self):
        return self._width * self._height

class Canvas:

    def __init__(self, width, height, bg="white"):
        self._width = width
        self._height = height
        self.background = bg

class Text:
    def __init__(self, size, color="black", font="Times"):
        self._color = color
        self._size = size
        self._font = font


def main():
    circle = Circle(5.0, fill='orange', stroke='red')
    quadrilateral = Quadrilateral(5, 10547, fill='orange', stroke='red')
    print(f"area= {circle.calculate_area()}")
    print(f"circumference is {len(circle)}")
    print(circle())
    print(repr(circle))
    print(quadrilateral.calculate_area())
    return os.EX_OK





if __name__ == "__main__":
    sys.exit(main())