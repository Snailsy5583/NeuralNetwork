import random
import numpy as np

from Layer import *
from ActivationFunc import *

class Network():
    #sizes is list of nums for number of neurons at each layer
    def __init__(self, sizes):
        self.sizes = sizes
        self.numLayers = len(sizes)
        
        self.layers = [Layer(self.sizes[i]) for i in range(self.numLayers)]
    
    # a = current activation function
    def forward(self, a):
        for w,b in zip(self.weights, self.biases):
            a = sigmoid(np.dot(w,a) + b)
        return a
    
    def forwardMat(self):
        for i in range(self.numLayers-2): # for each hidden layer
            
            
            # update layer
            



## Calc output for a single nueron given weights, bias, and inputs
