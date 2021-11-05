from src.triangle import Triangle
from src.square import Square


triangle = Triangle(13, 14, 15)


def test_triangle_name():
    assert triangle.name == "Triangle"


def test_triangle_area():
    assert triangle.area == 84


def test_triangle_perimeter():
    assert triangle.perimeter == 42


def test_triangle_add():
    square = Square(10)
    assert triangle.add_area(square) == 184


def test_triangle_add_no_figure():
    no_figure = "не фигура"
    assert triangle.add_area(no_figure) == "Incorrect Class"



