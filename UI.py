import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from DataUtils import DataUtils
from FunctionUtils import FunctionUtils

class UI:               
    def __init__(self,data_object,function_object):

        self.window = Tk()
        self.window.title("Machine Learning Thing")
        self.window.geometry("1000x500")


        self.graph_figure = Figure(
            figsize = (5, 5), 
            dpi = 100)
        

        self.graph = self.graph_figure.add_subplot(111) #creates subplotgraph


        self.graph_canvas = FigureCanvasTkAgg( #calls a API that allows you to put a matplotlib graph in a tkinter frame 
            self.graph_figure, 
            master = self.window) 
        

        self.graph_canvas.get_tk_widget().pack(side=RIGHT)


        self.tools = Frame(
            self.window, 
            height=100, 
            width=500).pack()
        
        

        self.cost_function_label = Label(
            self.tools,
            text="Cost: ",)


        self.cost_function_label.pack()        


        self.learning_rate_variable = StringVar().set("") #variable that whatever is in the text box gets stored and is set as nothing as default


        self.learning_rate_text_box = Entry(
            self.tools,
            bg="White",
            fg = "Black",
            textvariable= self.learning_rate_variable
            ).pack()


        self.preform_regression_button = Button(
            self.tools,
            text="Preform Regression", 
            command=self.update_graph(data_object,function_object)
            ).pack()


        #self.cost_function_label["text"] = "Cost: " + str(function_object.compute_cost(data_object)) #updates cost function



        self.window.mainloop()
    

    def update_graph(self,data_object,function_object):

        function = function_object.function
        x_data = data_object.x_values
        y_data = data_object.y_values
        predicted_y_data = FunctionUtils.compute_array_of_xvalues_multi_threaded(function,x_data)
        
        self.graph.clear() # resets the graph
        self.graph.scatter(x_data, y_data)
        self.graph.scatter(x_data, predicted_y_data)
        self.graph_canvas.draw()


    def 




    def run(self):
        self.window.mainloop()
   
   