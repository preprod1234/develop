from . figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, a, b):
        self.perimeter = (a + b) * 2
        self.area = a * b

