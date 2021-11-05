from src.triangle import Triangle
from src.square import Square


square = Square(10)


def test_square_name():
    assert square.name == "Square"


def test_square_area():
    assert square.area == 100


def test_square_perimeter():
    assert square.perimeter == 40


def test_square_add():
    triangle = Triangle(13, 14, 15)
    assert square.add_area(triangle) == 184


def test_square_add_no_figure():
    no_figure = "не фигура"
    assert square.add_area(no_figure) == "Incorrect Class"

