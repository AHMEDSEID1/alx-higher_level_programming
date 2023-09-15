#!/bin/usr/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple (<score>, <weight>)"""
    if not my_list:
        return 0
    sum_prod = 0
    sum_weight = 0
    for score, weight in my_list:
        sum_prod += score * weight
        sum_weight += weight
    return sum_prod / sum_weight
