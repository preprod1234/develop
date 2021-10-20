from figure import Figure


class Circle(Figure):
    name = "Square"

    def __init__(self, a):
        self.perimeter = 2 * 3.14 * a
        self.area = 3.14 * a ** 2



