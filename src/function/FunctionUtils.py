import numpy as np
import re
import concurrent.futures
from multiprocessing import Pool
import os



class FunctionUtils:
    """
    this class holds all of the functionality for the function.py class
    """

    def get_powers(coefficents):
        """
        gets the power values from a coefficents. 
        
        Params:
            coefficents: list
                -the coefficents of the function
                NOTE: make sure the function coefficents are in decending order with respect to power. ex: x^2 -9 ->>> [9,0,1]
        
        Returns: 
            powers: list
                -a list of power variables 
        """
        powers = []
        for i, num in enumerate(coefficents):
            powers.append(i)
        return powers

    def compute_value(coefficents, powers, x):
        """
        computes a single x value over a polynomial function given its coefficents and powers. 

        NOTE: please rearrange your input function to be from least to greatest. 
        For example the function x^2 -3x +5 would be interpreted as (powers: [0,1,2], coefficents: [5,-3,1].

        Params:
            coefficents : np.array(float16)
                -a numpy array of coefficent terms 
            powers : np.array(int)
                -a numpy array of power terns
            x : float
                -the input value
            NOTE: this function assumes that powers, and coefficents are the same length

        Returns:
            total : double 
                the computed term given
        
        """
        total = 0

        # This code computes the coefficent in parts
        for i in range(len(coefficents)):
          total += x ** powers[i] * coefficents[i]
        return total 
    


    def compute_values_multithreaded(coefficients, powers, x_values):
        """
        This code computes a whole entire numpy array into the function.

        Params:
            coefficents : np.array(float16)
                -a numpy array of coefficent terms 
            powers : np.array(int)
                -a numpy array of power terns
            x_values : np.array(float16)
                - a array of floating points as input
        
        Returns:
            results : np.array 
                the computed terms 
        
        Note:
            -Since the function "def compute_value(coefficents, powers, x):" takes in more than one parameter. A wrapper function is defined "def compute_single_value(x)".
            -This is so we can use executor.map on the operation to multithread the operation.
                    
        """
        results = np.zeros_like(x_values)  # Create an array to store the results
        
        with concurrent.futures.ThreadPoolExecutor() as executor:

            def compute_single_value(x):
                return FunctionUtils.compute_value(coefficients, powers, x)

            results = np.array(list(executor.map(compute_single_value, x_values))) # Map the computation function to each x in parallel
        
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
    

    def compute_single_partial_derivative(actual_i,predicted_i,power):
        """
        computes a single partial derivitive at ith location. Useful for parellization

        Args:
            acutal_i : float16
                - actual output value
            predicted_i : float16
                - predicted value from function/hypothesis aproximiation
            power : int
                - power variable
        
        Returns: 
            single_partial_derivative : float16
                - partiall computed partial derivitve

        Note: 
            - the computation preformed isnt the full partial dertivitve. Its the part where its compputed at ith value.
        """
        single_partial_derivative = (actual_i - predicted_i) * (predicted_i ** power)
        return np.array(single_partial_derivative)
        

    def compute_gradient(actual,predicted,powers):
        """
        Computes the partial derivatives for each coefficent term

        Params:
            powers : np.array
                -the power values
            acutal: np.array
                -the actual output of the data 
            predicted : np.array
                -the predict output of the data that was predicted by the function/hypothesis

        Returns: 
            graident : np.array()
                - a graident of the partial derivatives computed 
        
                    
        """
        gradient = []
        M = len(actual)

        for power in powers:
            partial_derivative = 0
            for i in range(len(actual)):
                partial_derivative += FunctionUtils.compute_single_partial_derivative(actual[i],predicted[i],power)
            partial_derivative = (-1/M) * partial_derivative
            gradient.append(partial_derivative)
        return np.array(gradient)


    

    def update_coefficents(coefficents,computed_gradient,learning_rate):
        """
        updates the existing coefficents with regression

        Params:
            coefficents : np.array
                - a array of coefficents from the function/hypothesis
            computed_gradient : np.array
                - computed partial derivatives 
            learning_rate : int
                - size in witch the function should change

        Returns:
            updated_coefficents : np.array
                - the updated coefficent values 
        """
        updated_coefficents = [] # blank list set to size of coefficent array

        for current_coefficent,partial_derivative in zip(coefficents,computed_gradient):
            updated_coefficent = current_coefficent - learning_rate * partial_derivative
            updated_coefficents.append(updated_coefficent)

        return np.array(updated_coefficents)



    def compute_cost(actual,predicted):
        """
        computes the cost

        Param:
            acutal : np.array
                - the acutal values of the data
            predicted : np.array
                - the predicted values of the data computed by the function
        
        Returns: 
            cost : float
                - the cost of the function
        """
        sum = 0
        N = len(actual)
        for i,j in zip(actual,predicted):
            sum += (i - j) ** 2
        cost = (1/2*N) * sum
        return cost


    
   