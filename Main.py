from Data import Data
from Function import Function
from DataUtils import DataUtils
from FunctionUtils import FunctionUtils


data = Data()
function = Function()

data.x_values, data.y_values = DataUtils.pull_data_from_csv_file('Data.csv')

y_values = FunctionUtils.compute_array_of_values(function.coefficents ,function.powers, data.x_values)
print(y_values)
    



