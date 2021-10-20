from figure import Figure
from math import sqrt


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, a, b, c):
        self.perimeter = a + b + c
        p = (a + b + c) / 2
        self.area = sqrt(p*(p - a)*(p - b)*(p - c))

