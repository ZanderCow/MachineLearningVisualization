
import numpy as np
import concurrent.futures
import re


class FunctionUtils:

    def compute_single_value(coefficents, powers, x):
        
        

        result = numpy_function_reference(x)
        return result
    
    
    def compute_function(numpy_function, x_values):
        results = np.zeros(len(x_values)) #initalizes array
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(lambda x: numpy_function(x), x_values))
        return results
    
    
    def convert_string_polynomial_to_numpy_array_form(function):
        """
        Function that converts polynomial string to numpy array

        Args:
            function : string 
                a string representation of a polynomial function (ex 2x^3 -5)

        Examples:
            >>> convert_string_polynomial_to_numpy_array_form(x^2 -5)
            [1,-5]
            >>> convert_string_polynomial_to_numpy_array_form(3x^3 + 10)
            [3,0,0,10]

        Note: 
            if any function where the highest degree is n. Any terms that are less than n and not specfifed in the string 
            are interpeted as 0 (ex: 2x^3 -5) would be [2,0,0,-5] 
        """  

        function = function.replace(" ", "") # Remove spaces in function string
        terms = re.findall('[+-]?[^+-]+', function) # Split function string into separate terms with regular expressions        
        degree = max(int(re.findall(r'\^(\d+)', term)[0]) if '^' in term else 1 if 'x' in term else 0 for term in terms) # Find the highest degree in the polynomial        
        coefficients = [0] * (degree + 1) # Initialize coefficients list with zeros based on degree

        # Loop through each term of the polynomial
        for term in terms:
            coeff = re.findall(r'([+-]?\d*)x', term) # Find coefficient of x in each term
            deg = re.findall(r'\^(\d+)', term) # Find degree of x in each term
            # If both coefficient and degree are found in a term
            if coeff and deg: # If both coefficient and degree are found in a term
                coefficients[degree - int(deg[0])] = int(coeff[0]) if coeff[0] not in ['-', ''] else -1 if coeff[0] == '-' else 1 # Assign coefficient value at correct index in coefficients list
            # If only coefficient is found (degree is implicitly 1)
            elif coeff:
                coefficients[degree - 1] = int(coeff[0]) if coeff[0] not in ['-', ''] else -1 if coeff[0] == '-' else 1 # Assign coefficient value at correct index in coefficients list
            # If only constant term is found (degree is implicitly 0)
            else:
                coefficients[degree] = int(term) # Assign constant value at the last index in coefficients list

        coefficients = np.array(coefficients) # Convert coefficients list to numpy array for efficient manipulation

        return coefficients


   