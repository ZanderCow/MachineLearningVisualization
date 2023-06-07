import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from FunctionUtils import FunctionUtils



class UI:
    """
    UI class for the program.

    Attributes:
        self.data : Data() object
            -a reference to the data object from the main class. 
        self.function : Function() object
            -a reference to the function object in the main class. 
        self.window : tk.Tk() 
            -a tktiner window object. 
            -is a container for all the widgets (such as buttons, labels, text boxes, etc.).
            -provides basic framework for building graphical user interface.
        self.graph_figure : tk.Figure()
            -Creates a new Figure object for plotting.
        self.graph : tk.subplot()
            - creates a subplot
            - adds the subplot to self.graph_figure
            - this is the actual graph. When you want to plot or add data to be displayed, this is where
            you want to be refrencing from.
        self.graph_canvas : FigureCanvasTkAgg()
            -tkinter backend for displaying self.graph_figure within a tkinter application window
        self.cost_function_label : tk.label()
            - label that stores the value of the cost function
            - gets updated everytime the "predict data" button is pressed
        self.learning_rate_text_box : tk.Entry()
            - Textbox that stores the user input for the learning rate
        self.predict_data_button : tk.Button()
            - button that when pressed, preforms 1 iteration of graident descent to the data with the function
            self.predict_data()
        self.number_of_iterations : tk.Entry()
            - Entry for number of iterations
        self.learning_rate_label : tk.Label()
            - label for the text box entry
        self.number_of_iterations_label : tk.Label()
            - label for the # of iterations
    """
    def __init__(self,data_object,function_object):
        """ 
        Initialize MainWindow with given data and function objects.

        Args:
        data : Data() object from Data.py class
            -An object of the data.py class initalized in the main class
        function : Function() object from Function.py class
            -An object of the function.py initalized in the main class
        """

        self.data = data_object
        self.function = function_object

        self.main_window = tk.Tk() 
        self.main_window.title("Machine Learning Thing")
        self.main_window.geometry("500x700") 

        self.graph_figure = Figure(figsize = (5, 5), dpi = 100) 
        self.graph = self.graph_figure.add_subplot(111)
        self.graph_canvas = FigureCanvasTkAgg(self.graph_figure, master = self.main_window) 
        self.graph_canvas.get_tk_widget().pack() #packs the subplot to the figure/window

        self.cost_function_label = tk.Label(self.main_window,text='Cost:')
        self.cost_function_label.pack()
        self.learning_rate_label = tk.Label(self.main_window,text="Learning Rate:")
        self.learning_rate_label.pack()
        self.learning_rate_text_box = tk.Entry(self.main_window,width=10)
        self.learning_rate_text_box.pack()
        self.number_of_iterations_label = tk.Label(self.main_window,text="# of iterations")
        self.number_of_iterations_label.pack()
        self.number_of_iterations = tk.Entry(self.main_window,width=10)
        self.number_of_iterations.pack()

        self.predict_data_button = tk.Button(text="predict data",command=self.optimize_data)
        self.predict_data_button.pack()

        self.update_graph_with_data()
        self.main_window.mainloop()
        pass

   
    def update_graph_with_data(self):
        """
        Updates the graph with the data from the data_object
        """
        self.graph.clear() # resets the graph

        data = self.data.data
        predicted_y = FunctionUtils.compute_values_multithreaded(self.function.coefficients, self.function.powers, self.data.data[0])
        self.graph.scatter(data[0], data[1]) #grabs the x_values and y_values from the data_object and  adds them to the subplot
        self.graph.scatter(data[0],predicted_y) #grabs the x_values and y_values from the data_object and  adds them to the subplot
        
        cost = FunctionUtils.compute_cost(data[1],predicted_y)
        self.cost_function_label.config(text='Cost: ' + str(cost))

        self.graph_canvas.draw() # updates the figure object
        pass



    def optimize_data(self):
        """
        preforms 1 iteration of graident descent 
        """
        num_iterations = int(self.number_of_iterations.get())
        learning_rate = float(self.learning_rate_text_box.get())

        for i in range(num_iterations):
            predicted_y = FunctionUtils.compute_values_multithreaded(self.function.coefficients, self.function.powers, self.data.data[0])
            gradient = FunctionUtils.compute_gradient(self.data.data[1],predicted_y,self.function.powers)
            self.function.coefficients = FunctionUtils.update_coefficents(self.function.coefficients,gradient,learning_rate)
        self.update_graph_with_data()

    






