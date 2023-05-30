import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from DataUtils import DataUtils
from FunctionUtils import FunctionUtils
from tkinter import filedialog
from sympy import symbols, lambdify, sympify
import numpy as np

from UI.DataWindow import DataWindow

class MainWindow:
    """
    Main application window for the Machine Learning Thing.

    This class is responsible for the creation and management of the main application window and its components,
    including other windows, menus and graphs.
    """
    def __init__(self,data_object,function_object):
        """
        Initialize MainWindow with given data and function objects.

        Args:
        data_object : object
            An object that holds the data to be visualized.
        function_object : object
            An object that encapsulates a mathematical function to be applied to the data.
        """
        self.data_object = data_object
        self.function_object = function_object
        self.create_main_window()
        self.create_other_window_refrence_variables()
        self.create_menu_bar()
        self.create_graph()
        self.main_window.mainloop()
        pass

    def create_main_window(self):
        """
        Create the main window for the application using Tkinter.
        """
        self.main_window = tk.Tk()
        self.main_window.title("Machine Learning Thing")
        self.main_window.geometry("500x500")
        pass
    
    def create_other_window_refrence_variables(self):
        """
        Initialize references to other window objects to None.
        These windows include data, predict and optimize windows.
        """
        self.data_window = None
        self.predict_window = None
        self.optimze_window = None
        pass
    
    def create_menu_bar(self):
        """
        Create a menu bar for the main application window.
        The menu bar includes three menu options: Data, Predict, and Optimize.
        """
        self.menu_bar = tk.Menu(self.main_window)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Data", command=self.draw_data_window)
        self.file_menu.add_command(label="Predict", command=self.draw_predict_window)
        self.file_menu.add_command(label="Optimize", command=self.draw_optimize_window)
        self.menu_bar.add_cascade(label="Menu", menu=self.file_menu)
        self.main_window.config(menu=self.menu_bar)
        pass

    def create_graph(self):
        """
        Create a graph within the main application window.
        The graph is created using Matplotlib and embedded in Tkinter using the FigureCanvasTkAgg class.
        """
        self.graph_figure = Figure(figsize = (5, 5), dpi = 100)
        self.graph = self.graph_figure.add_subplot(111) #creates subplotgraph
        self.graph_canvas = FigureCanvasTkAgg(self.graph_figure, master = self.main_window) 
        self.graph_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        pass

    def update_graph(self):
        """
        Update the graph with the data from the data_object and the function from the function_object. Will clear the current graph first, then add the updated 
        graph
        """
        self.graph.clear() # resets the graph
        self.graph.scatter(self.data_object.x_values, self.data_object.y_values)
        self.graph_canvas.draw()
        pass

    def add_another_graph_on_top_of_current_graph(self):
        """
        Adds another scatter plot graph on top of the current one. Useful for showing 2 types of data on the same scatter plot graph

        Note:
            This function is very simular to update_graph(). The only diffrence is that this graph doesnt call .clear() on the original graph before adding a new one onto it
        """
        function = self.function_object.function
        x_data = self.data_object.x_values
        y_data = self.data_object.y_values
        self.graph.scatter(x_data, y_data)
        self.graph_canvas.draw()
        pass



    def draw_data_window(self):
        """
        Draw the data window. 
        If the data window already exists, it is destroyed and a new one is created.
        """
        if self.data_window is None or not self.data_window.winfo_exists():
            self.data_window = DataWindow(self)
        else:
            self.data_window.destroy()
            self.data_window = None
        pass

    def draw_predict_window(self):
        """
        (To be implemented)
        Draw the predict window.
        """
        pass
    
    def draw_optimize_window(self):
        """
        (To be implemented)
        Draw the optimize window.
        """
        pass
    






