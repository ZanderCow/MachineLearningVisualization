import csv
from numpy import array, bfloat16

class DataUtils:
    """
    Holds all of the functionality to the Data class. Designed to adhere to data oriented design prinsiples
    """

    def pull_data_from_csv_file(file_name):
        """
        This method pulls the information from a csv file and returns it. 

        Parameters:
            file_name : string
                -A pathname to a csv file in the users file system represented as a string
        
        Returns: 
            -x_data, y_data: np.array (bfloat16)
            NOTE: data is converted to np in the function
        
        Throws: 
            FileNotFoundError: error
                -"Error: file not found."
            e : Expection
                -if any unusual errors pop up

        """
        try:
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                
                x_data = float(next(reader, None))
                y_data = float(next(reader, None))

                #convert data to bfloat16 numpy array
                x_data = array(x_data, dtype=bfloat16)
                y_data = array(y_data, dtype=bfloat16)
        
                return x_data,y_data

        except FileNotFoundError:
            print("Error: file not found.")
        except Exception as e:
            print(f"Error: {e}")
        pass