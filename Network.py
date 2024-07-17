import random
import numpy as np

from Layer import *
from ActivationFunc import ActivationFunction as AF   

class Network():
    #sizes is list of nums for number of neurons at each layer
    def __init__(self, sizes):
        self.sizes = sizes
        self.numLayers = len(sizes)
        self.layers = [Layer(self.sizes[i]) for i in range(self.numLayers)]
    
    def intialize2(dims):
        parameters = {}
        layers = len(dims) #number of layers teehee [128, 16, 16, 10]

        for l in (1, layers - 1):
            #randn(3,2) = array [[a,b],[c,d],[e,f]]
            parameters['w' + str(l)] = np.random.randn(dims[l], dims[l-1]) 
            parameters['b' + str(l)] = np.zeros(shape=(dims[l], 1))
        
        return parameters
    
    # put in array of inputs
    def forward_model(self, X, parameters):
        input = X
        layers = len(parameters) // 2

        for l in range(1, layers - 1):
            last = input
            input = Layer_huh.forward_prop(parameters['w' + str(l)], 
                                           parameters['b' + str(1)], 
                                           last,
                                           activation=af.ReLU)
            
        #Linear to sigmoid
        final = Layer_huh.forward_prop(parameters['w' + str(layers - 1)], 
                                  parameters['b' + str(layers - 1)], 
                                  input,
                                  activation=af.sigmoid)
        return final
    
    def cost(self, batman):
        output = self.layers[-1]
        error = 0
        for i in range(len(batman)):
            error += (batman[i] - output[i])**2
        
        return error

    

        #back



## Calc output for a single nueron given weights, bias, and inputs

# a = current activation function
#     def forward(self, a):
#         for w,b in zip(self.weights, self.biases):
#             a = sigmoid(np.dot(w,a) + b)
#         return a

