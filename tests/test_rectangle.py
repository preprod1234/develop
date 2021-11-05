from src.rectangle import Rectangle
from src.triangle import Triangle


rectangle = Rectangle(5, 10)


def test_rectangle_name():
    assert rectangle.name == "Rectangle"


def test_rectangle_area():
    assert rectangle.area == 50


def test_rectangle_perimeter():
    assert rectangle.perimeter == 30


def test_rectangle_add():
    triangle = Triangle(13, 14, 15)
    assert rectangle.add_area(triangle) == 134


def test_rectangle_add_no_figure():
    no_figure = "не фигура"
    assert rectangle.add_area(no_figure) == "Incorrect Class"