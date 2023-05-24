import csv
class DataUtils:
    def pull_data_from_csv_file(file_name):
        x_data = []
        y_data = []
        try:
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                
                xdata = next(reader, None)
                ydata = next(reader, None)

                #convert data to floating point
                xdata = [float(x) for x in xdata]
                ydata = [float(x) for x in ydata]
                return x_data,y_data

        except FileNotFoundError:
            print("Error: data.csv file not found.")
        except Exception as e:
            print(f"Error: {e}")
        pass