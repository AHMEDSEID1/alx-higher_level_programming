#!/usr/bin/python3
a = 10
b = 5
import calculator_1

result_add = calculator_1.add(a, b)
result_sub = calculator_1.sub(a, b)
result_mul = calculator_1.mul(a, b)
result_div = calculator_1.div(a, b)

print("Addition: {} + {} = {}".format(a, b, result_add))
print("Subtraction: {} - {} = {}".format(a, b, result_sub))
print("Multiplication: {} * {} = {}".format(a, b, result_mul))
print("Division: {} / {} = {}".format(a, b, result_div))
