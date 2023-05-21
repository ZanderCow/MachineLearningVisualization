import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class UI: 
    '''
    builds the UI when a object of the class is instantiated
    '''                  
    def __init__(self,data_object,function_object):
        #Main Window
        self.window = Tk()
        self.window.title("Machine Learning Thing")
        self.window.geometry("1000x500")

        #Graphing_Figure
        self.graph_figure = Figure(figsize = (5, 5), dpi = 100)
        #Subplot
        self.graph = self.graph_figure.add_subplot(111) #creates subplotgraph
        self.graph_canvas = FigureCanvasTkAgg(self.graph_figure, master = self.window) # Binds the subplot graph to the figure
        self.graph_canvas.get_tk_widget().pack(side=RIGHT)


        #Frame that stores the user functionality tools
        self.tools = Frame(self.window, height=100, width=500).pack() # creates the function area canvas where all the buttons are

        #cost function label
        self.cost_function_label = Label(self.tools, text="Cost: ",)
        self.cost_function_label.pack()

        #variable that whatever is in the text box gets stored
        self.learning_rate_variable = StringVar()
        self.learning_rate_variable.set("")
        self.learning_rate_text_box = Entry(self.tools, bg="White", fg = "Black", textvariable= self.learning_rate_variable).pack()
        
        #preform regression
        self.preform_regression = Button(self.tools,text="Preform Regression", command=None).pack()
        
        #updates cost function label to match the cost
        self.cost_function_label["text"] = "Cost: " + str(function_object.compute_cost(data_object)) #updates cost function

        self.plot_graph(data_object,function_object)
        self.window.mainloop()


        


 
    def plot_graph(self,data_object,function_object):
        """
        Plots the graph.

        Parameters:
            data_object (Data): An instance of the Data class.
            function_object (Function): An instance of the Function class.
        """
        self.graph.clear() # resets the graph
        self.graph.scatter(data_object.xdata, data_object.ydata)
        
        #Scatters another graph over top 
        # also calls .make_predictions() on the function_object
        self.graph.scatter(data_object.xdata, function_object.make_predictions(data_object.xdata))

        self.graph_canvas.draw()

    
   