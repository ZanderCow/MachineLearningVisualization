import matplotlib.pyplot as plt
import tkinter as tk
from DataUtils import DataUtils
from FunctionUtils import FunctionUtils
from tkinter import filedialog
import numpy as np

class DataWindow:
    """
    Class for generating a UI window for data manipulation. This window can either pull data from a CSV file
    or generate random data based on a function with Gaussian noise.
    """
    def __init__(self,parent):
        """
        Initializes the DataWindow object and calls methods to create the window and its components.

        Args:
            parent: The parent UI element that this DataWindow will be attached to. (the mainwindow)
        """
        self.parent = parent
        self.create_window(self.parent)
        self.create_drop_down_window()
        self.create_csv_file_button()
        self.create_chose_function_objects()
        self.create_range_objects()
        self.create_data_points_objects()
        self.create_randomness_objects()
        self.create_generate_data_objects()
        self.run()
        pass


    def create_window(self,main_ui_reference):
        """
        Creates the main window for the DataWindow, sets up the layout, and assigns it to the parent UI element.

        Args:
            main_ui_reference: The main user interface that will be used as the parent for this window.
        """
        self.main_ui_reference = main_ui_reference #creates a main UI refrences that allows for things in this class to call a function from a object of the MainWindow class)
        self.data_window = tk.Toplevel(main_ui_reference.main_window) #creates a seperate window that is connected to the main_window object in the MainWindow class
        self.data_window.title('Data') 
        self.data_window.geometry("750x500")

        # turns self.data_window into a 5x5 grid. This allows for widgets to be placed nicely 
        for i in range(5): 
            self.data_window.columnconfigure(i, weight=1, uniform='a')
            self.data_window.rowconfigure(i, weight=1, uniform='a')
        pass


    def create_drop_down_window(self):
        """
        Creates a drop-down menu within the DataWindow. The options in the drop-down menu allow for choosing
        the data collection method.
        """
        self.drop_down_window = tk.StringVar(self.data_window) # creates a string var that holds a text
        self.drop_down_window.set('Choose option') # sets string var option to "chose option"
        self.drop_down_window.trace('w', self.data_collection_option_changed) #sets up the ability for the drop_down_window menu to call data_collection_option_changed() when its option is changed 
        self.drop_down_window_menu = tk.OptionMenu(self.data_window, self.drop_down_window, 'pull from csv file', 'guassian noise') #creates the drop down menu
        self.drop_down_window_menu.grid(row=0,column=2) #adds the drop down menu to the frame
        pass
    
    def create_csv_file_button(self):
        """
        Creates a button in the DataWindow for selecting a CSV file for data import.
        """
        self.file_button = tk.Button(self.data_window, text='Choose CSV file', command=self.open_file)
        pass
    
    def create_chose_function_objects(self):
        """
        Creates a button in the DataWindow for selecting a CSV file for data import.
        """
        self.chose_function_frame = tk.Frame(self.data_window) #holds the tktiner objects below in the function (makes it nicer to look at)
        self.function_text_label = tk.Label(self.chose_function_frame,text="Function")
        self.function_text_label.pack()
        self.function__text_box_entry = tk.Entry(self.chose_function_frame, width=25,text='Function') #varianle that gets stored in
        self.function__text_box_entry.pack()
        pass
    
    def create_range_objects(self):
        """
        Creates UI components for specifying the range of values to be generated. This includes two text box entries
        for minimum and maximum values.
        """
        self.generated_values_range_frame = tk.Frame(self.data_window) #holds the tktiner objects below in the function (makes it nicer to look at)
        self.range_min_text_box_entry = tk.Entry(self.generated_values_range_frame,width=5)
        self.range_min_text_box_entry.pack(side='left')
        self.range_or_text = tk.Label(self.generated_values_range_frame,text="to")
        self.range_or_text.pack(side='left')
        self.range_max_text_box_entry = tk.Entry(self.generated_values_range_frame,width=5)
        self.range_max_text_box_entry.pack(side='left')
        pass

    def create_data_points_objects(self):
        """
        Creates UI components for specifying the number of data points. This includes a text label and a text box for input.
        """
        self.num_data_points_frame = tk.Frame(self.data_window) #holds the tktiner objects below in the function (makes it nicer to look at)
        self.num_data_points_label = tk.Label(self.num_data_points_frame,text='# of data points')
        self.num_data_points_label.pack()
        self.num_data_points_text_box_entry = tk.Entry(self.num_data_points_frame,width=8)
        self.num_data_points_text_box_entry.pack()
        pass

    def create_randomness_objects(self):
        """
        Creates UI components for specifying the amount of randomness in the generated data. This includes a text label 
        and a text box for input.
        """
        self.randomness_ammount_frame = tk.Frame(self.data_window) #holds the tktiner objects below in the function (makes it nicer to look at)
        self.randomness_ammount_label = tk.Label(self.randomness_ammount_frame,text='randomness')
        self.randomness_ammount_label.pack()
        self.randomness_ammount_text_box_entry = tk.Entry(self.randomness_ammount_frame,width=8)
        self.randomness_ammount_text_box_entry.pack()
        pass

    def create_generate_data_objects(self):
        """
        Creates a button in the DataWindow to initiate data generation based on the provided parameters.
        """
        self.generate_data_button = tk.Button(self.data_window,text='Generate Data',command=self.generate_data)
        pass

    def run(self):
        """
        Starts the main event loop for the DataWindow.
        """
        self.data_window.mainloop()
        pass
    
    def update_window_for_pull_from_csv_file_option(self):
        """
        Updates the DataWindow UI to the configuration suitable for the 'Pull from CSV file' option.
        """
        self.file_button.grid(row=2,column=2)
        self.generate_data_button.grid_forget()
        self.generate_data_button.grid(row=3,column=2)

        # gets rid the widgets that were displayed when "guassian noise option was selected"
        self.chose_function_frame.grid_forget()
        self.generated_values_range_frame.grid_forget()
        self.randomness_ammount_frame.grid_forget()
        self.num_data_points_frame.grid_forget()
        pass
    
    def update_window_for_guassian_noise_option(self):
        """
        Updates the DataWindow UI to the configuration suitable for the 'Gaussian noise' option.
        """
        self.chose_function_frame.grid(row=1,column=2)
        self.generated_values_range_frame.grid(row=2,column=1)
        self.randomness_ammount_frame.grid(row=2,column=3)
        self.generate_data_button.grid_forget()
        self.generate_data_button.grid(row=3,column=2)
        self.num_data_points_frame.grid(row=2,column=2)
        
        # gets rid the widgets that were displayed when "chose from csv file option were selected"
        self.file_button.grid_forget()
        pass


        
    def data_collection_option_changed(self,*args):
        """
        Event handler for changes to the data collection option in the drop-down menu. Updates the UI configuration
        based on the selected option.

        Args:
            *args: Variable length argument list.
        """
        if self.drop_down_window.get() == 'pull from csv file':
            self.update_window_for_pull_from_csv_file_option()
        elif self.drop_down_window.get() == 'guassian noise':
            self.update_window_for_guassian_noise_option()
    

    def open_file(self):
        """
        Opens a file dialog to allow the user to select a CSV file for data import. Prints the selected file name.
        """
        self.file_that_user_chosed = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
    
    def generate_data(self):
        """
        Generates data based on the selected parameters: a function, range, number of data points, and randomness.
        The generated data is then passed to the parent UI element for display.
        """
        if self.are_all_options_filled_out() == False:
            print("all options are not filled out")
        else:
            function = FunctionUtils.convert_string_polynomial_to_numpy_array_form(self.function__text_box_entry.get())
            function = np.poly1d(function) # turns into a polynomial object
            min = int(self.range_min_text_box_entry.get())
            max = int(self.range_max_text_box_entry.get())
            num_data_points = int(self.num_data_points_text_box_entry.get())
            randomness_ammount = int(self.randomness_ammount_text_box_entry.get())

            # this code refrences the x and y values from a Data class object created in the main class
            self.parent.data_object.x_values = np.linspace(min, max, num_data_points)
            self.parent.data_object.y_values = FunctionUtils.compute_array_of_xvalues_multi_threaded(function,self.parent.data_object.x_values) + np.random.normal(0, randomness_ammount, num_data_points)

            self.parent.update_graph()
        pass
       

    def are_all_options_filled_out(self):
        """
        Checks if all the required fields for data generation are filled out: function, range minimum, and range maximum.

        Returns:
            False (boolean): if any of the required fields are not filled out
            True (boolean): if all of the required fields are filled out
        """
        if not (self.function__text_box_entry.get() == '' or self.range_min_text_box_entry.get() == '' or self.range_max_text_box_entry.get() == "" or self.num_data_points_text_box_entry == '' or self.randomness_ammount_text_box_entry == ''):
            return True
        else: return False
