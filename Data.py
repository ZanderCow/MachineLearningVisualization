import csv
class Data:
    """
    Class used to store the data that will be used

    Attributes:
        x, y : np.array (bfloat16)
            -Represents the input data (the values that determine the output). 
            -Uses bfloat16 to save on memory resources.
            -****ONLY 1D ROW ARRAYS CAN BE USED. THIS ALLOWS IT TO BE VISUALIZED ON THE GRAPH (WILL ADD 2D support in the future****
    """
    def __init__(self, x, y):
        """
        Initalizes the class

        Parameters:
            x,y : np.array([]) (bfloat16)

        """
        self.x = x
        self.y = y


    pass
        

        