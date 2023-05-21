import numpy as np
import csv
from sympy import symbols, lambdify, sympify

# Define the x symbol for sympy
x = symbols('x')

# Input your function as a string
func_str = "x**3 + 4*x**2 + 3*x + 3"

# Convert the string to a sympy function
func_sympy = sympify(func_str)

# Convert the sympy function to a lambda function for numerical calculations
func = lambdify(x, func_sympy, 'numpy')

# Generate x values
x_values = np.linspace(-10, 10, 100)

# Generate y values with Gaussian noise
y_values = func(x_values) + np.random.normal(0, 100, 100)

# Write x and y values to a CSV file
with open('Data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(x_values)
    writer.writerow(y_values)