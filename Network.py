import random
import numpy as np

# Activation Funciton
def sigmoid(x):
        return 1.0/(1.0+np.exp(-x))


class Net:
    
    #sizes is list of nums for number of input nodes at each layer
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.rand(y, 1) for y in sizes[1:]]
        self.weights = [np.random.rand(y,x) for x,y in zip(sizes[:-1], sizes[1:])] ###
                        
    # a = current activation function
    def forward(self, a):
        for w,b in zip(self.weights, self.biases): 
            a = sigmoid(np.dot(w,a) + b)
        return a



## Calc output for a single nueron given weights, bias, and inputs
