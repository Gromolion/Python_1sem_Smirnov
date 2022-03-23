from math import sqrt

__all__ = ['triangle_perimeter', 'triangle_area']
a = 7
b = 2
c = 8


def triangle_perimeter(first, second, third):
    return first + second + third


def triangle_area(first, second, third):
    p = (first + second + third)
    return sqrt(p * (p - first) * (p - second) * (p - third))
