import sys
import os
from math import pi

class Circle:
    def __init__(self, radius, fill='red', stroke='black'):
        self._radius = radius
        self._fill= fill
        self._stroke= stroke

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

def main():
    circle= Circle(5.0, fill='orange', stroke='red')
    print(f"area= {circle.calculate_area()}")
    print(f"circumference is {len(circle)}")
    print(circle())
    return os.EX_OK

if __name__ == "__main__":
    sys.exit(main())