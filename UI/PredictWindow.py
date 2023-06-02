import matplotlib.pyplot as plt
import tkinter as tk
from DataUtils import DataUtils
from FunctionUtils import FunctionUtils
import numpy as np

class PredictWindow:
    def __init__(self,parent):
        self.parent = parent

        self.create_window()
        self.create_function_objects()
        self.create_predict_data_objects()

        self.predict_window.mainloop()

        
        pass

    def create_window(self):
        self.predict_window = tk.Toplevel(self.parent.predict_window) 
        self.predict_window.title('Predict')
        self.predict_window.geometry("750x500")
        for i in range(5): # Assuming a 5x5 grid
            self.predict_window.columnconfigure(i, weight=1, uniform='a')
            self.predict_window.rowconfigure(i, weight=1, uniform='a')
        pass

    def create_function_objects(self):
        self.function_frame = tk.Frame(self.predict_window)
        self.function_label = tk.Label(self.function_frame,text='Function:')
        self.function_label.pack()
        self.function_text_box = tk.Entry(self.function_frame,width=25)
        self.function_text_box.pack()
        self.function_frame.grid(row=1,column=2)
        pass
    
    def create_predict_data_objects(self):
        self.predict_data_button = tk.Button(self.predict_window,text="Predict Data",command=self.predict_data) #TODO: add command 
        self.predict_data_button.grid(row=3,column=2)
        pass
    
    def predict_data(self):
        """
        predicts the data
        """
        function_pulled_from_text_box = self.function_text_box.get() #grabs function string grom text box
        FunctionUtils.convert_string_polynomial_to_numpy_array_form(function_pulled_from_text_box) #updates the function variables inside function_object to the one inside the text box 
        prediction_function = self.parent.function_object.function #refrence from the MainWindow.py object function_object object variable 
        x_values = self.parent.data_object.x_values # grabs the xvalues from the data object.x_values
        y_values = FunctionUtils.compute_array_of_xvalues_multi_threaded(prediction_function, x_values)
        self.parent.graph_prediction(x_values,y_values)
        pass