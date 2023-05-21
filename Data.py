import csv
class Data:
    def __init__(self):
        #default values
        self.xdata = None
        self.ydata = None
        #Pulls data from csv file 
        try:
            with open('data.csv', 'r') as file:
                reader = csv.reader(file)
                self.xdata = next(reader, None)
                self.ydata = next(reader, None)

                #convert data to int
                self.xdata = [float(x) for x in self.xdata]
                self.ydata = [float(x) for x in self.ydata]
        except FileNotFoundError:
            print("Error: data.csv file not found.")
        except Exception as e:
            print(f"Error: {e}")

        

        