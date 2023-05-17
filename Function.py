class Function:
    def __init__(self):
        self.function = [3] #function is represented as a array ([0,1,2] would be 0x^2 + 1x + 2]
        self.cost = 0

    '''
    (input) a array of values ex: [2,3,3,3] 
    Function sticks them into Fx and computes the output.
    '''
    def make_predictions(self,input):
        self.predictedValues = []
        self.reversedFunction = self.function[::-1] #reverses the function order (it makes it easer to compute)
        for dataPoint in input:
            y = 0
           #computes the function in parts. for example in [3,3,3] (3x^2+ 3x +3), it would compute 3x^2 first, 3x and then 3. 
            for i, element in enumerate(self.function):
                y += element * ((dataPoint) ** i)
            self.predictedValues.append(y)
        return self.predictedValues
    
    '''
    https://stackoverflow.com/questions/50457921/cost-function-mean-squared-error-formulae
    '''
    def compute_cost(self,input):
        sum = 0
        self.input_length = len(input)
        
        return  (1/(2(self.inputLength))) * (sum(self.make_predictions(input)))