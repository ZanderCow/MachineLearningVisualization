import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class UI:
    def plot_graph(self,Data,Function):
        self.Graph.clear() # resets the graph
        self.Graph.scatter(Data.xdata,Data.ydata)
        
        #Scatters another graph over top
        self.Graph.scatter(Data.xdata, Function.makePredictions(Data.xdata))
        

        self.GraphCanvas.draw()

        ''' (cost function Label)
        Cost.get_cost() #computes cost
        self.CostFunctionLabel["text"] = ("Cost: " + str(Cost.mean_squared_error)) #updates cost function
        print(Hypothesis.hyp)
        '''
    
    def doRegression(self):
        self.plot_graph()
    


                        
    def __init__(self,Data,Function):
        #Main Window
        self.window = Tk()
        self.window.title("Machine Learning Thing")
        self.window.geometry("1000x500")
        self.LN = ""

        #Graphing_Figure
        self.GraphFigure = Figure(figsize = (5, 5), dpi = 100)

        #Subplot
        self.Graph = self.GraphFigure.add_subplot(111) #creates subplotgraph

        self.GraphCanvas = FigureCanvasTkAgg(self.GraphFigure, master = self.window) # Binds the subplot graph to the figure

        self.GraphCanvas.get_tk_widget().pack(side=RIGHT,anchor='e',expand=YES,fill=BOTH)



        #Frame that stores the user functionality tools
        self.Tools = Frame(
            self.window,
            height=100,
            width=500
            ).pack(anchor='c',fill=BOTH) # creates the function area canvas where all the buttons are


        self.CostFunctionLabel = Label(
            self.Tools,
                text="Cost: ",
                )
        self.CostFunctionLabel.pack()


        self.LearningRateVariable = StringVar()
        self.LearningRateVariable.set("")
        self.LearningRate_TextBox = Entry(
            self.Tools,
            bg="White",
            fg = "Black",
            textvariable= self.LearningRateVariable,
            ).pack()
        
        self.PreformRegression = Button(
            self.Tools,
            text="Preform Regression",
            command=self.doRegression
            ).pack()
        
        self.plot_graph(Data,Function)
        self.window.mainloop()
