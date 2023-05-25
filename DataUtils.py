import csv
class DataUtils:
    def pull_data_from_csv_file(file_name):
        x_data = []
        y_data = []
        try:
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                
                x_data = next(reader, None)
                y_data = next(reader, None)

                #convert data to floating point
                x_data = [float(x) for x in x_data]
                y_data = [float(x) for x in y_data]
        
                return x_data,y_data

        except FileNotFoundError:
            print("Error: data.csv file not found.")
        except Exception as e:
            print(f"Error: {e}")
        pass