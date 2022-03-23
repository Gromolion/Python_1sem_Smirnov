from math import sqrt

__all__ = ['triangle_perimeter', 'triangle_area']
a = 7
b = 2
c = 8


def triangle_perimeter(first=a, second=b, third=c):
    return first + second + third


def triangle_area(first=a, second=b, third=c):
    p = (first + second + third)
    return sqrt(p * (p - first) * (p - second) * (p - third))
