import pytest
import math


# Класс прямоугольника
class Rectangle:
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(f'Can not create Rectangle')

        self.side_a = side_a
        self.side_b = side_b
        self.name = 'Rectangle'

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def add_area(self, r2):
        return self.get_area() + r2.get_area()


# Класс квадрата
class Square:
    def __init__(self, side):
        if side <= 0:
            raise ValueError('Can not crate Square')

        self.side = side
        self.name = 'Square'

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return self.side * 4

    def add_area(self, r2):
        return self.get_area() + r2.get_area()


# Класс треугольника
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError('Can not create Triangle')

        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError('Invalid side lengths for a triangle')

        self.name = 'Triangle'
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.p = (self.side_a + self.side_b + self.side_c) / 2

    def get_area(self):
        return math.sqrt(self.p * (self.p - self.side_a) * (self.p - self.side_b) * (self.p - self.side_c))

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def add_area(self, r2):
        return self.get_area() + r2.get_area()


# Класс круга
class Circles:
    def __init__(self, R):
        if R <= 0:
            raise ValueError('Can not create Circles')
        self.name = 'Circles'
        self.R = R
        self.P = 3.14

    def get_area(self):
        return round(self.P * self.R ** 2)

    def get_perimeter(self):
        return round(self.P * self.R * 2)

    def add_area(self, r2):
        return self.get_area() + r2.get_area()


# Тесты прямоугольника
@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (4, 5, 18, 20),
                             (10, 20, 60, 200),
                             (7, 5, 24, 35),
                         ])
def test_rectangle(side_a, side_b, perimeter, area):
    r = Rectangle(side_a, side_b)
    assert r.name == 'Rectangle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (-4, 5, 2, 20),
                             (0, 20, 40, 0),
                         ])
def test_rectangle_negative(side_a, side_b, perimeter, area):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


# Тесты треугольника
@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
                         [
                             (5, 5, 8, 18, 12),
                             (5, 4, 3, 12, 6),
                             (50, 40, 30, 120, 600),
                         ])
def test_triangle(side_a, side_b, side_c, perimeter, area):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == 'Triangle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
                         [
                             (5, 5, 8, 18, 12),
                             (5, 4, 3, 12, 6),
                             (50, 40, 30, 120, 600),
                         ])
def test_triangle_negative(side_a, side_b, side_c, perimeter, area):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


# Тесты квадрата
@pytest.mark.parametrize('side, perimeter, area',
                         [
                             (5, 20, 25),
                             (10, 40, 100),
                             (50, 200, 2500),
                         ])
def test_square(side, perimeter, area):
    r = Square(side)
    assert r.name == 'Square'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side, perimeter, area',
                         [
                             (0, 21, 250),
                             (0, 45, 10),
                             (0, 300, 250),
                         ])
def test_square_negative(side, perimeter, area):
    with pytest.raises(ValueError):
        Square(side)


# Тесты круга
@pytest.mark.parametrize('R, perimeter, area',
                         [
                             (5, 31, 78),
                             (6, 38, 113),
                             (50, 314, 7850),
                         ])
def test_circles(R, perimeter, area):
    r = Circles(R)
    assert r.name == 'Circles'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('R, perimeter, area',
                         [
                             (0, 21, 250),
                             (0, 45, 10),
                             (0, 300, 250),
                         ])
def test_circles_negative(R, perimeter, area):
    with pytest.raises(ValueError):
        Circles(R)


# Тесты функции add_area
def test_add_area():
    r1 = Rectangle(30, 50)
    r2 = Circles(10)
    assert round(r1.add_area(r2)) == 1814


def test_add_area_negative():
    r1 = Rectangle(30, 50)
    r2 = Circles(10)
    assert round(r1.add_area(r2)) != -100
