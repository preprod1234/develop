from src.circle import Circle
from src.triangle import Triangle


circle = Circle(10)


def test_circle_name():
    assert circle.name == "Circle"


def test_circle_area():
    assert circle.area == 314


def test_circle_perimeter():
    assert circle.perimeter == 62


def test_circle_add():
    triangle = Triangle(13, 14, 15)
    assert circle.add_area(triangle) == 398


def test_circle_add_no_figure():
    no_figure = "не фигура"
    assert circle.add_area(no_figure) == "Incorrect Class"