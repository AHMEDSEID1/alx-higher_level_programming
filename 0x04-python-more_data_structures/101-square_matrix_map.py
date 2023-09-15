#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """Returns a new matrix with the square of each value"""
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
