from src.square import Square
from src.triangle import Triangle


square = Square(10)
print(square.area)

triangle = Triangle(13, 14, 15)
print(triangle.area)

print(square.add_area(triangle))
