import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

from UI.DataWindow import DataWindow
from UI.PredictWindow import PredictWindow

class MainWindow:
    """
    Main application window for the Machine Learning Thing.

    This class hold the graph plot as well as holds the drop down menu where other windows can be opened
    """
    def __init__(self,data_object,function_object):
        """
        Initialize MainWindow with given data and function objects.

        Args:
        data_object : object
            An object of the data.py class initalized in the main class
        function_object : object
            An object of the function.py initalized in the main class
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
        self.main_window = tk.Tk() #creates the tkinter window
        self.main_window.title("Machine Learning Thing") #sets the title 
        self.main_window.geometry("500x500") # sets the size
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
        self.menu_bar = tk.Menu(self.main_window)# creates the menu bar
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0) # creates the drop down menu when self.menu_bar is clicked

        # menu bar options 
        self.file_menu.add_command(label="Data", command=self.draw_data_window) 
        self.file_menu.add_command(label="Predict", command=self.draw_predict_window)
        self.file_menu.add_command(label="Optimize", command=self.draw_optimize_window)

        self.menu_bar.add_cascade(label="Menu", menu=self.file_menu) #creates the clickable menu option 
        self.main_window.config(menu=self.menu_bar) #adds a menu to the window
        pass

    def create_graph(self):
        """
        Create a graph within the main application window.
        The graph is created using Matplotlib and embedded in Tkinter using the FigureCanvasTkAgg class.
        """
        self.graph_figure = Figure(figsize = (5, 5), dpi = 100) # tkinter object (kinda like a frame) that allows for plots to be displayed
        self.graph = self.graph_figure.add_subplot(111)#creates subplotgraph (the plot that will be displayed)
        self.graph_canvas = FigureCanvasTkAgg(self.graph_figure, master = self.main_window) #API bridge that allows tkinter and matplotlib to talk to eachother
        self.graph_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True) #packs the subplot to the figure/window
        pass

    def update_graph(self):
        """
        Update the graph with the data from the data_object and the function from the function_object. Will clear the current graph first, then add the updated 
        graph
        """
        self.graph.clear() # resets the graph
        self.graph.scatter(self.data_object.x_values, self.data_object.y_values) #grabs the x_values and y_values from the data_object and  adds them to the subplot
        self.graph_canvas.draw() # updates the figure object
        pass

    def graph_prediction(self,x_values,y_values):
        """
        Adds another scatter plot graph on top of the current one. Useful for showing 2 types of data on the same scatter plot graph

        Note:
            This function is very simular to update_graph(). The only diffrence is that this graph doesnt call .clear() on the original graph before adding a new one onto it
        """ 
        self.graph.scatter(x_values, y_values) #grabs the x_values and y_values from the data_object and  adds them to the subplot
        self.graph_canvas.draw() # updates the figure object)
        pass
        

    def draw_data_window(self):
        """
        Draws the data window. 
        """
        # if data window is not initalized or isnt drawn on screen
        if self.data_window is None or not self.data_window.winfo_exists():
            self.data_window = DataWindow(self) #create dataWindow
        else:
            self.data_window.destroy() #clears the variable
            self.data_window = None #sets its insides to nothing
        pass

    def draw_predict_window(self):
        """
        Draws the predict window.
        """
        # if predict window is not initalized or isnt drawn on screen
        if self.predict_window is None or not self.predict_window.winfo_exists():
            self.data_window = PredictWindow(self)
        else:
            self.predict_window.destroy()#clears the variable
            self.predict_window = None #sets its insides to nothing
        pass
        pass
    
    def draw_optimize_window(self):
        """
        (To be implemented)
        Draw the optimize window.
        """
        pass
    






