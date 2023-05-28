import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from DataUtils import DataUtils
from FunctionUtils import FunctionUtils
from tkinter import filedialog
from sympy import symbols, lambdify, sympify
import numpy as np

class MainUI:
    """
    A class used to represent the Main User Interface 
    ...

    Attributes
    ----------
    data_object : object
        an instance of a Data class, used to hold and manage data for the application
    function_object : object
        an instance of a Function class, used to encapsulate function-related operations
    main_window : Tk object
        the main window for the user interface
    data_window : Tk object
        a window to handle data-related operations, initialized as None
    predict_window : Tk object
        a window to handle prediction operations, initialized as None
    optimize_window : Tk object
        a window to handle optimization operations, initialized as None
    menu_bar : Menu object
        the main menu bar for the application
    file_menu : Menu object
        a menu for file-related operations
    graph_figure : Figure object
        a matplotlib figure object for displaying a graph
    graph : Subplot object
        a subplot to be added to the matplotlib figure
    graph_canvas : Canvas object
        a canvas on which the matplotlib figure is drawn

    Methods
    -------
    update_graph():
        Updates the graph based on the current data and function object
    draw_data_window():
        Initiates or recreates the data window
    draw_predict_window():
        To be implemented - supposed to initiate or recreate the prediction window
    draw_optimize_window():
        To be implemented - supposed to initiate or recreate the optimization window
    """
    def __init__(self,data_object,function_object):

        self.data_object = data_object
        self.function_object = function_object

        self.main_window = tk.Tk()
        self.main_window.title("Machine Learning Thing")
        self.main_window.geometry("500x500")
 

        self.data_window = None
        self.predict_window = None
        self.optimze_window = None

        self.menu_bar = tk.Menu(self.main_window)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.file_menu.add_command(label="Data", command=self.draw_data_window)
        self.file_menu.add_command(label="Predict", command=self.draw_predict_window)
        self.file_menu.add_command(label="Optimize", command=self.draw_optimize_window)
        
        self.menu_bar.add_cascade(label="Menu", menu=self.file_menu)
        self.main_window.config(menu=self.menu_bar)


        self.graph_figure = Figure(figsize = (5, 5), dpi = 100)
        
        self.graph = self.graph_figure.add_subplot(111) #creates subplotgraph
        self.graph_canvas = FigureCanvasTkAgg(self.graph_figure, master = self.main_window) 
        self.graph_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.main_window.mainloop()
    
    def update_graph(self,x_values,y_values):
        
        function = self.function_object.function
        x_data = x_values
        y_data = y_values
        #predicted_y_data = FunctionUtils.compute_array_of_xvalues_multi_threaded(function,x_data)
        
        self.graph.clear() # resets the graph
        self.graph.scatter(x_data, y_data)
        #self.graph.scatter(x_data, predicted_y_data)
        self.graph_canvas.draw()
        
    def draw_data_window(self):
        """
        Initiates and creates the data window. 
        If a data window already exists, it is destroyed and set to None.
        """
        if self.data_window is None or not self.data_window.winfo_exists():
            self.data_window = DataWindow(self)
        else:
            self.data_window.destroy()
            self.data_window = None
    

    def draw_predict_window(self):
        """
        Placeholder for a method that initiates or recreates the prediction window.
        Currently, it does nothing.
        """
        pass
    
    def draw_optimize_window(self):
        """
        Placeholder for a method that initiates or recreates the optimization window.
        Currently, it does nothing.
        """
        pass
    



class DataWindow():
    """
    Class to create a data window with various controls and options.

    Attributes
    ----------
    data_window : tk.Toplevel
        A top-level window generated from the main window reference.
    drop_down_window : tk.StringVar
        A string variable for the Tkinter window, which holds the current state of the dropdown menu.
    drop_down_window_menu : tk.OptionMenu
        A dropdown menu with two options to choose from: 'pull from csv file' or 'gaussian noise'.
    file_button : tk.Button
        A button that opens a file dialog to choose a CSV file.
    function, range_min, range_max, randomness_ammount : tk.StringVar, tk.DoubleVar, tk.DoubleVar, tk.DoubleVar
        Variables that hold user input
    chose_function_frame: tk.Frame
        A frame that binds the function__text_box and function_text_label into one thing so it fits only one grid space
    function_text_label, function__text_box : tk.Frame, tk.Label, tk.Text
        UI elements related to function choice: a frame, a label and a textbox.
    generated_values_range_frame : tk.Frame
        A frame thats used for showing the range of generated values.
    randomness_ammount_slider : tk.Scale
        A slider to adjust the amount of randomness for the guassian noise
    generated_values_range_frame, range_min_text_box, range_or_text, range_max_text_box : tk.Frame, tk.Text, tk.Label, tk.Text
        tkinter stuff that holds the range selection area
    generate_data_button : tk.Button
        button that when clicked, will call a function called generate_data()
    Methods
    -------
    data_collection_option_changed(*args):
        Changes the GUI based on the selected option in the dropdown menu. Shows different widgets for different options.

    open_file():
        Opens a file dialog to choose a CSV file and prints the chosen file's name.
    """
    def __init__(self,main_ui_reference):
        self.main_ui_reference = main_ui_reference
        self.data_window = tk.Toplevel(main_ui_reference.main_window)
        self.data_window.title('Data')
        self.data_window.geometry("750x500")

        for i in range(5): # Assuming a 5x5 grid
            self.data_window.columnconfigure(i, weight=1, uniform='a')
            self.data_window.rowconfigure(i, weight=1, uniform='a')


        self.drop_down_window = tk.StringVar(self.data_window)
        self.drop_down_window.set('Choose option')
        self.drop_down_window.trace('w', self.data_collection_option_changed)
        self.drop_down_window_menu = tk.OptionMenu(self.data_window, self.drop_down_window, 'pull from csv file', 'guassian noise')
        self.drop_down_window_menu.grid(row=0,column=2) 

        self.chose_csv_file_frame = tk.Frame(self.data_window)
        

        self.file_button = tk.Button(self.data_window, text='Choose CSV file', command=self.open_file)

        self.function = tk.StringVar()
        self.range_min = tk.IntVar()
        self.range_max = tk.IntVar()
        self.num_data_points = tk.IntVar()
        self.randomness_ammount = tk.DoubleVar()

        #chose function stuff
        self.chose_function_frame = tk.Frame(self.data_window)
        self.function_text_label = tk.Label(self.chose_function_frame,text="Function")
        self.function_text_label.pack()
        self.function__text_box_entry = tk.Entry(self.chose_function_frame, width=25,text='Function') #varianle that gets stored in
        self.function__text_box_entry.pack()

        #generated values stuff
        self.generated_values_range_frame = tk.Frame(self.data_window)
        self.range_min_text_box_entry = tk.Entry(self.generated_values_range_frame,width=5)
        self.range_min_text_box_entry.pack(side='left')
        self.range_or_text = tk.Label(self.generated_values_range_frame,text="to")
        self.range_or_text.pack(side='left')
        self.range_max_text_box_entry = tk.Entry(self.generated_values_range_frame,width=5)
        self.range_max_text_box_entry.pack(side='left')

        #number of data points stuff
        self.num_data_points_frame = tk.Frame(self.data_window)
        self.num_data_points_label = tk.Label(self.num_data_points_frame,text='# of data points')
        self.num_data_points_label.pack()
        self.num_data_points_text_box_entry = tk.Entry(self.num_data_points_frame,width=8)
        self.num_data_points_text_box_entry.pack()
        

        self.randomness_ammount_slider = tk.Scale(self.data_window, variable=self.randomness_ammount, from_=0, to=10000, label='Randomness', resolution=0.2, orient='horizontal',length=150)
        
        self.generate_data_button = tk.Button(self.data_window,text='Generate Data',command=self.generate_data)
        
    def data_collection_option_changed(self,*args):
        """
        This function is called when the selection of the dropdown menu changes.
        It updates the GUI to show different controls based on the selected option.

        Parameters
        ----------
        *args :
            Variable length argument list. It is not used in this method, but is a common practice in event handlers.
        """
        if self.drop_down_window.get() == 'pull from csv file':
            #----place corresponding widets in code-----
            self.file_button.grid(row=2,column=2)
            self.generate_data_button.grid_forget()
            self.generate_data_button.grid(row=3,column=2)

            self.chose_function_frame.grid_forget()
            self.generated_values_range_frame.grid_forget()
            self.randomness_ammount_slider.grid_forget()
            self.num_data_points_frame.grid_forget()
            #----------------------------------------
        elif self.drop_down_window.get() == 'guassian noise':
            #----place corresponding widets in code-----
            self.chose_function_frame.grid(row=1,column=2)
            self.generated_values_range_frame.grid(row=2,column=1)
            self.randomness_ammount_slider.grid(row=2,column=3)
            self.generate_data_button.grid_forget()
            self.generate_data_button.grid(row=3,column=2)
            self.num_data_points_frame.grid(row=2,column=2)

            self.file_button.grid_forget()
            #----------------------------------------

    def open_file(self):
        """
        This function opens a file dialog to choose a CSV file and prints the chosen file's name.
        """
        filename = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
        print(f"Selected file: {filename}")
    
    def generate_data(self):
        x = symbols('x')
        func_str = self.function__text_box_entry.get()
        func_sympy = sympify(func_str)
        func = lambdify(x, func_sympy, 'numpy')
        
        min = int(self.range_min_text_box_entry.get())
        max = int(self.range_max_text_box_entry.get())

        num_data_points = int(self.num_data_points_text_box_entry.get())
        randomness_ammount = int(self.randomness_ammount.get())

        x_values = np.linspace(min, max, num_data_points)
        y_values = func(x_values) + np.random.normal(0, randomness_ammount, num_data_points)

        self.main_ui_reference.update_graph(x_values,y_values)
        pass
       

    def are_all_options_filled_out(self):
        if self.function.get() == '' or self.range_min.get() == '' or self.range_max.get() == "":
            pass




