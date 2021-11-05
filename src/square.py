from . figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, a):
        self.perimeter = a * 4
        self.area = a ** 2

