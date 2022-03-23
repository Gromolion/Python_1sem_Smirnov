from math import pi

__all__ = ['circle_perimeter', 'circle_area']
default_radius = 5


def circle_perimeter(r=default_radius):
    return 2*pi*r


def circle_area(r=default_radius):
    return pi*r**2
