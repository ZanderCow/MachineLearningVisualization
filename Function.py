import re
class Function:
    def __init__(self,function):
        self.string_version = function
        self.coefficent_terms = []
        self.power_terms = []
        self.coefficent_terms,self.power_terms = self.parse_polynomial(function)

    

    def parse_polynomial(self,function_string):
        """
        Parse a polynomial function string into a list of coefficients and powers.

        This function takes a polynomial function represented as a string, finds all the terms in the 
        string, and extracts the coefficients and powers of each term. It assumes the function string 
        is provided in the standard polynomial format, e.g., '2x^2 + 3x - 4'. 

        Arguments:
        function_string -- A string representing a polynomial function. Terms must be separated by '+' 
                        or '-' symbols, and the power of x in each term must be indicated with '^'.
                        For example, '2x^2 + 3x - 4' is a valid input.

        Returns:
        A tuple of two lists: the first list contains the coefficients of each term (in the same order 
        as they appear in the input string), and the second list contains the powers of x for each term 
        (again, in the same order).

        Example:
        >>> parse_polynomial('2x^2 + 3x - 4')
        ([2.0, 3.0, -4.0], [2, 1, 0])
        """
        terms = re.findall(r'([+-]?\s*\d*\.?\d*\s*x\^\d+|[+-]?\s*\d*\.?\d*\s*x|[+-]?\s*\d+\.?\d*)', function_string)
        coefficients = []
        powers = []
        for term in terms:
            term = term.replace(' ', '')
            if 'x' in term:
                if '^' in term:
                    coef, power = term.split('x^')
                    coef = '1' if coef in ['', '+'] else '-1' if coef == '-' else coef
                    coefficients.append(float(coef))
                    powers.append(int(power))
                else:
                    coef = term.split('x')[0]
                    coef = '1' if coef in ['', '+'] else '-1' if coef == '-' else coef
                    coefficients.append(float(coef))
                    powers.append(1)
            else:
                coefficients.append(float(term))
                powers.append(0)

        return coefficients, powers





    

   

    def make_predictions(self,input):
        """
        ake predictions based on the input data using the defined function.

        Parameters:
        - self: The instance of the class.
        - input: List of input data points.

        Returns:
        - predictedValues: List of predicted values.

        """
        predictedValues = []
        for dataPoint in input:
            y = 0
           #computes the function in parts. for example in [3,3,3] (3x^2+ 3x +3), it would compute 3x^2 first, 3x and then 3. 
            for coefficent,power in zip(self.coefficent_terms,self.power_terms):
                y += (coefficent * ((dataPoint)** power))
            predictedValues.append(y)
        return predictedValues
    

    def compute_cost(self,data_object):
        """
        Compute the cost using the predicted and actual values.
        
        Parameters:
        - self: The instance of the class.
        - dataObject: An object containing xdata and ydata attributes.
        
        Returns:
        - cost: The computed cost.
        """
        cost = 0
        predictedValues = self.make_predictions(data_object.xdata)
        actualValues = data_object.ydata
        n = len(predictedValues)
        for xi,yi in zip(predictedValues,actualValues):
            cost += ((xi - yi)**2)
        cost = (1/(n)) * cost
        return cost
    
    def compute_gradient_vectors():

        return None