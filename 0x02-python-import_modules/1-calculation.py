#!/usr/bin/python3
# Import the required functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Assign values to variables a and b
a = 10
b = 5

# Call each function with a and b as arguments and store the results in variables
add_result = add(a, b)
sub_result = sub(a, b)
mul_result = mul(a, b)
div_result = div(a, b)

# Print the results
print("{} + {} = {}".format(a, b, add_result))
print("{} - {} = {}".format(a, b, sub_result))
print("{} * {} = {}".format(a, b, mul_result))
print("{} / {} = {}".format(a, b, div_result))
