import sys
import os
from math import pi
import yaml

class Circle:

    def __init__(self, radius, fill='red', stroke='black', at=(0,0)):
        self._radius = radius
        self._fill = fill
        self._stroke = stroke
        self._at = at

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

    def __str__(self):
        string = yaml.dump({
            'circle' : {
                'radius': self._radius,
                'fill': self._fill,
                'stroke': self._stroke,
                'at': self._at
            }
        })
        return string

    @classmethod
    def from_yaml(cls, string):
        """Creatr a circle from YAML instance"""
        circle_dict = yaml.load(string, Loader=yaml.Loader)['circle']
        print(circle_dict)
        obj = cls(circle_dict['radius'], fill=circle_dict['fill'], stroke=circle_dict['stroke'], at=circle_dict['at'])
        return obj





class Quadrilateral:

    def __init__(self, width, height, fill="red", stroke="black"):
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

    my_dict = {
        'key':{
            'inside_dict':[5,6,7,8]
        }
    }
    my_yaml= yaml.dump(my_dict)
    print(my_yaml)
    print(circle)

    yaml_circle = """\
circle:
  at: !!python/tuple
  - 0
  - 0
  fill: orange
  radius: 5.0
  stroke: red """
    my_circle = Circle.from_yaml(yaml_circle)

    return os.EX_OK





if __name__ == "__main__":
    sys.exit(main())