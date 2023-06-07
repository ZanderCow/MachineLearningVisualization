import csv
class Data:
    """
    Class used to store the data that will be used

    Attributes:
        self.data : np.array (bfloat16)
            -Represents the input data (the values that determine the output). 
            -Uses bfloat16 to save on memory resources.
    """
    def __init__(self, data):
       """
       initalizes class object

       Param:
            data : np.array (bfloat16)
                -input data (cleaned up through csv file)
       """
       self.data = data
    pass
        

        