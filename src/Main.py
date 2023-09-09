from function.Function import Function
from function.FunctionUtils import FunctionUtils
from data.Data import Data
from data.DataUtils import DataUtils
from ui.UI import UI
function = "x^2" #your hypothesis function that you chose 
data_file_location = "Data.csv" #the pathfile where your data is located 

























temp_coefficents = FunctionUtils.convert_string_polynomial_to_numpy_array_form(function)
temp_coefficents = temp_coefficents[::-1]
temp_powers = FunctionUtils.get_powers(temp_coefficents)


function = Function(temp_coefficents,temp_powers)

del temp_coefficents, temp_powers

data = Data(DataUtils.pull_from_csv_file(data_file_location))

ui = UI(data,function)