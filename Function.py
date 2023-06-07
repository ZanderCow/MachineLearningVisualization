from numpy import array, float16

class Function:
    """
    this class represents our Hypothesis (a function). 

    Attributes:
        coefficients : np.array (float16)
            -Array of coefficent values that are stored.
            -Uses float16 to save on memory resources.
            NOTE: see FunctionUtils for how its computed 
        powers: np.array (int)
            - Array of power values that are stored
            NOTE: see FunctionUtils for how its computed 
    """

    def __init__(self, coefficents, powers):
        """
        Initalizes a function object. passes in coefficent and powers, and sets them to be the instance variables 
        inside the class

        Parameters: 
            coefficents, powers : list
            -Array/list of coefficent, and power values that are stored.
        """
        self.coefficients = array(coefficents,dtype=float16)
        self.powers = array(powers,dtype=float16)

    pass