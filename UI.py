import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from DataUtils import DataUtils
from FunctionUtils import FunctionUtils
from tkinter import filedialog

class UI():              
    def __init__(self,data_object,function_object):

        self.data_object = data_object
        self.function_object = function_object

        self.main_window = Tk()
        self.main_window.title("Machine Learning Thing")
        self.main_window.geometry("1000x500")
 

        self.data_window = None
        self.predict_window = None
        self.optimze_window = None



        self.menu_bar = Menu(self.main_window)
        self.menu_bar.add_cascade(label="Data", command=self.draw_data_window)
        #---placeholders for later
        self.menu_bar.add_cascade(label="Predict", command=self.draw_predict_window)
        self.menu_bar.add_cascade(label="Optimize", command=self.draw_optimize_window)
        #------

        self.main_window.config(menu=self.menu_bar)


        self.graph_figure = Figure(figsize = (5, 5), dpi = 100)
        

        self.graph = self.graph_figure.add_subplot(111) #creates subplotgraph
        self.graph_canvas = FigureCanvasTkAgg(self.graph_figure, master = self.main_window) 
        self.graph_canvas.get_tk_widget().pack()
        #self.cost_function_label["text"] = "Cost: " + str(function_object.compute_cost(data_object)) #updates cost function
        self.main_window.mainloop()
    





    def draw_data_window(self):
        if self.data_window is None or not self.data_window.winfo_exists():
            #-------------------Data UI Code-------------------------------------

            def data_collection_option_changed(*args):
                if data_collection_drop_down_window.get() == 'pull from csv file':
                    file_button.pack(side=LEFT,padx=10,pady=10)
                    mean_slider.pack_forget()
                    std_slider.pack_forget()
                elif data_collection_drop_down_window.get() == 'guassian noise':
                    mean_slider.pack(side=LEFT,padx=10,pady=10)
                    std_slider.pack(side=LEFT,padx=10,pady=10)
                    file_button.pack_forget()

            def data_collection_open_file():
                filename = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
                print(f"Selected file: {filename}")


            self.data_window = Toplevel(self.main_window)
            self.data_window.title('Data')
            self.data_window.geometry("1000x500")


            drop_down_window_frame = Frame(self.data_window,bg='grey',width=1000, height=100)
            drop_down_window_frame.pack()
            drop_down_window_frame.propagate(False)


            content_area_frame = Frame(self.data_window, bg='white',width=1000, height=600)
            content_area_frame.pack()
            content_area_frame.propagate(False)


            data_collection_drop_down_window = StringVar(self.data_window)
            data_collection_drop_down_window.set('Choose method of data collection')

            data_collection_drop_down_window.trace('w', data_collection_option_changed)
            data_collection_drop_down_window_menu = OptionMenu(drop_down_window_frame, data_collection_drop_down_window, 'pull from csv file', 'guassian noise')
            data_collection_drop_down_window_menu.pack(padx=10, pady=30)


            file_button = Button(content_area_frame, text='Choose CSV file', command=data_collection_open_file)

            mean = DoubleVar()
            std = DoubleVar()
            function = StringVar()




            mean_slider = Scale(content_area_frame, variable=mean, from_=0, to=10, label='Mean', resolution=0.1, orient='horizontal',length=75)
            std_slider = Scale(content_area_frame, variable=std, from_=0.1, to=10, label='Standard Deviation', resolution=0.1, orient='horizontal',length=125)


            
            #---------------------------------------------------------------
        else:
            self.data_window.destroy()
            self.data_window = None


    def draw_predict_window(self):
        if self.predict_window is None or not self.predict_window.winfo_exists():
            #-------------------Predict UI Code-------------------------------------


            self.predict_window = Toplevel(self.main_window)
            self.predict_window.title('Predict')
            self.predict_window.geometry("1000x500")
            

            #add code later
            #-----------------------------------------------------------------
        else:
            self.predict_window.destroy()
            self.predict_window = None

    def draw_optimize_window(self):
        if self.optimze_window is None or not self.optimze_window.winfo_exists():
            #-------------------Optimize UI Code-------------------------------------
            
            self.optimze_window = Toplevel(self.main_window)
            self.optimze_window.title('Optimize')
            self.optimze_window.geometry("1000x500")
            
            tools = Frame(self.optimze_window, height=100, width=500)
            tools.pack()

            cost_function_label = Label(tools,text="Cost: ",)
            cost_function_label.pack()        

            learning_rate_variable = StringVar().set("") #variable that whatever is in the text box gets stored and is set as nothing as default
            
            learning_rate_text_box = Entry(tools, bg="White", fg = "Black", textvariable= learning_rate_variable)
            learning_rate_text_box.pack()

            preform_regression_button = Button(tools, text="Perform Regression", command=lambda: self.update_graph(self.data_object, self.function_object))
            preform_regression_button.pack()
            
            self.optimze_window.mainloop()

            #add code later
            #-----------------------------------------------------------------
        else:
            self.optimze_window.destroy()
            self.optimze_window = None


    def update_graph(self,data_object,function_object):
        function = function_object.function
        x_data = data_object.x_values
        y_data = data_object.y_values
        predicted_y_data = FunctionUtils.compute_array_of_xvalues_multi_threaded(function,x_data)
        
        self.graph.clear() # resets the graph
        self.graph.scatter(x_data, y_data)
        self.graph.scatter(x_data, predicted_y_data)
        self.graph_canvas.draw()



