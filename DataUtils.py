import csv
from numpy import array, float16
from pandas import read_csv

class DataUtils:
    """
    Holds all of the functionality to the Data class. Designed to adhere to data oriented design prinsiples
    """

    def pull_from_csv_file(file_name):
        """
        This method pulls the data from a csv file and returns it.  
        """
        try:
            data = read_csv(file_name,header=None)
            data = data.to_numpy(dtype=float16)
        except ValueError:
            data = read_csv(file_name)

        return data