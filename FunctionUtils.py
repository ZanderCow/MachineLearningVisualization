
import numpy as np
import concurrent.futures
import re


class FunctionUtils:
    def compute_single_value(numpy_function_reference, x):
        """
        This function applies a given numpy function to a specified value.

        Parameters
        ----------
        numpy_function_reference : function
        A reference to a numpy function. This function should take a single argument.
        x : int, float
        The value to which the numpy function will be applied.

        Returns
        -------
        result : int, float
            The result of applying the numpy function to the input value.

        Example
        -------
        >>> import numpy as np
        >>> compute_single_value(np.poly1d([1,3,4]), 4)
        2.0
        """
        result = numpy_function_reference(x)
        return result
    
    def compute_array_of_xvalues_single_threaded(numpy_function_refrence, x_values):
        """
        This function applies a given numpy function to each value in a list of values using a single thread.

        Parameters
        ----------
        numpy_function_refrence : function
            A reference to a numpy function. This function should take a single argument.
        x_values : list of int, float
            The list of values to which the numpy function will be applied.

        Returns
        -------
        y_values : list of int, float
            The list of results from applying the numpy function to each value in the input list.

        Example
        -------
        >>> import numpy as np
        >>> compute_array_of_xvalues_single_threaded(np.sqrt, [1, 4, 9])
        [1.0, 2.0, 3.0]
        """
        y_values = []
        for x in x_values:
            y_values.append(numpy_function_refrence(x))
        return y_values 


    def compute_array_of_xvalues_multi_threaded(numpy_function, x_values):
        """
        This function uses multi-threading to apply a given numpy function to an array of x-values.

        It leverages the concurrent.futures.ThreadPoolExecutor to distribute the computation across multiple threads, which can significantly speed up processing time for large data arrays and/or complex computations.

        Args:
            numpy_function_reference (function): A reference to the numpy function that will be applied to the x_values. This should be a function that accepts a single argument.

            x_values (array-like): An array-like object (such as a list or numpy array) that contains the values that will be processed by the numpy function.

        Returns:
            list: A list of the results from applying the numpy function to each value in x_values. The ordering of the results will correspond to the ordering of the values in x_values.

        Example:
            >>> x_values = [0, 1, 2, 3, 4, 5]
            >>> compute_array_of_xvalues_multi_threaded(numpy.sin, x_values)
            [0.0, 0.8414709848078965, 0.9092974268256817, 0.1411200080598672, -0.7568024953079282, -0.9589242746631385]

        Note: 
            This function is most effective when the numpy function requires significant computation. For simple functions or small data arrays, the overhead of multi-threading can actually lead to slower execution times compared to a single-threaded approach.
        """
        results = np.zeros(len(x_values)) #initalizes array
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(lambda x: numpy_function(x), x_values))
        return results
    
    
    def convert_string_polynomial_to_numpy_array_form(function):  
        # Function that converts polynomial string to numpy array
        function = function.replace(" ", "") 
        # Remove spaces for easy string manipulation
        
        terms = re.findall('[+-]?[^+-]+', function) 
        # Split function string into separate terms with regular expressions
        
        degree = max(int(re.findall(r'\^(\d+)', term)[0]) if '^' in term else 1 if 'x' in term else 0 for term in terms)
        # Find the highest degree in the polynomial
        
        coefficients = [0] * (degree + 1)
        # Initialize coefficients list with zeros based on degree
        
        for term in terms:
            # Loop through each term of the polynomial
            coeff = re.findall(r'([+-]?\d*)x', term)
            # Find coefficient of x in each term
            
            deg = re.findall(r'\^(\d+)', term)
            # Find degree of x in each term

            if coeff and deg:
                # If both coefficient and degree are found in a term
                coefficients[degree - int(deg[0])] = int(coeff[0]) if coeff[0] not in ['-', ''] else -1 if coeff[0] == '-' else 1
                # Assign coefficient value at correct index in coefficients list

            elif coeff:
                # If only coefficient is found (degree is implicitly 1)
                coefficients[degree - 1] = int(coeff[0]) if coeff[0] not in ['-', ''] else -1 if coeff[0] == '-' else 1
                # Assign coefficient value at correct index in coefficients list

            else:
                # If only constant term is found (degree is implicitly 0)
                coefficients[degree] = int(term)
                # Assign constant value at the last index in coefficients list

        coefficients = np.array(coefficients)
        # Convert coefficients list to numpy array for efficient manipulation

        return coefficients
        # Return the numpy array of coefficients