#!/usr/bin/python3
# Import the calculator_1 module
import calculator_1 as calc

# Define the variables a and b
a = 10
b = 5

# Call the functions from the calculator_1 module using the module alias as a prefix
add_result = calc.add(a, b)
sub_result = calc.sub(a, b)
mul_result = calc.mul(a, b)
div_result = calc.div(a, b)

# Print the results using the required format
print("{} + {} = {}".format(a, b, add_result))
print("{} - {} = {}".format(a, b, sub_result))
print("{} * {} = {}".format(a, b, mul_result))
print("{} / {} = {}".format(a, b, div_result))
