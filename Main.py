from Data import Data
from Function import Function
from DataUtils import DataUtils
from FunctionUtils import FunctionUtils
from UI import *

data = Data()
function = Function()
data.x_values, data.y_values = DataUtils.pull_data_from_csv_file('Data.csv')
ui = MainUI(data,function)

