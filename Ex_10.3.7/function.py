"""Этот модуль считает площади фигур"""
import math
from math import pi

def circle_square(r: float) -> float:
    return math.pi * r ** 2

def rect_square(a: float, b: float) -> float:
    return a * b