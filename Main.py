import csv
from Data import Data
from UI import UI
from Function import Function
class Main:
    def __init__(self):
        data = Data()
        function = Function()
        UI(data,function)
    pass
    




if __name__ == '__main__':
    main = Main()
