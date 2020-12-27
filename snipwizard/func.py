from functools import reduce
from typing import Callable, List


def compose(*functions: Callable) -> Callable:
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def rot(matrix: List[List]) -> List[List]:
    """Rotate a python matrix (list of list) clockwise by 90 degree without numpy
    https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-matrix-in-python
    """
    return list(map(list, zip(*matrix[::-1])))


def flip_h(matrix: List[List]) -> List[List]:
    """Flip a matrix (list of list) horizontally
    """
    return [arr[::-1] for arr in matrix]


def flip_v(matrix: List[List]) -> List[List]:
    """Flip a matrix (list of list) vertically 
    """
    return matrix[::-1]
