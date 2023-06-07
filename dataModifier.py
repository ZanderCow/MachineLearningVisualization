import numpy as np
from FunctionUtils import FunctionUtils
import csv

file_name = "data.csv" 
function = "x^2"
min = -10
max = 10
number_of_data_points = 100
randomness = 30

















coefficents = FunctionUtils.convert_string_polynomial_to_numpy_array_form(function)
coefficents = coefficents[::-1]
powers = FunctionUtils.get_powers(coefficents)

function = FunctionUtils.convert_string_polynomial_to_numpy_array_form(function)
function = np.poly1d(function) # turns into a polynomial object

x_values = np.linspace(min, max, number_of_data_points)
y_values = FunctionUtils.compute_values_multithreaded(coefficents,powers, x_values) + np.random.normal(0, randomness, number_of_data_points)

with open(file_name, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(x_values)
    writer.writerow(y_values)





