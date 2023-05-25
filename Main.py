from Data import Data
from Function import Function
from DataUtils import DataUtils
from FunctionUtils import FunctionUtils


data = Data()
function = Function()

data.x_values, data.y_values = DataUtils.pull_data_from_csv_file('Data.csv')

y_values = FunctionUtils.compute_array_of_xvalues_multi_threaded(function.function, data.x_values)
print(y_values)





