import csv
class Data:
    """
    Class used to store the data that will be used

    Attributes:
        input : np.array (bfloat16)
            -Represents the input data (the values that determine the output). 
            -Uses bfloat16 to save on memory resources.
            -****ONLY 1D ROW ARRAYS CAN BE USED. THIS ALLOWS IT TO BE VISUALIZED 
            - 
        
    """
    def __init__(self,x_data,y_data):
        """
        Initalizes the class
        """
        self.x_values = []
        self.y_values = []
    pass
        

        