from concurrent.futures import ThreadPoolExecutor

class FunctionUtils:
    def compute_single_value(coefficents, powers, x):
        y = 0
        for coefficent,power in zip(coefficents,powers):
            y += (coefficent * (x ** power))
        return y
    
    def compute_array_of_values(coefficients, powers, x_values):
        pass
    
    def compute_cost(coefficents,powers,actual_values):
        pass
