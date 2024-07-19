import os
import random
import pickle as pickle_rick
from typing import List
import numpy as np

from Layer import *
from ActivationFunc import ActivationFunction as AF   

class Network():
    # sizes is list of nums for number of neurons at each layer
    def __init__(self, sizes):
        self.sizes = sizes
        self.num_layers = len(sizes)
        self.layers = [Layer(self.sizes[0])]
        for i in range(1, self.numLayers):
            self.layers.append(Layer(self.sizes[i], self.layers[i-1])) # give it a reference to the prev layer as well
    
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
    
    def forward_prop(self, input):
        self.layers[0].setValues(input)
        for i in range(1, len(self.layers)):
            self.layers[i].forward_prop()
        return self.layers[-1].getValues()
    
    def cost(self, batman):
        output = self.layers[-1]
        error = 0
        for i in range(len(batman)):
            error += (output[i] - batman[i])**2
            
        self.cost = error
        return self.cost
        #back    
    
    def save(self, prefix:str):
        os.mkdir(f"saves/{prefix}")
        with open(f"saves/{prefix}/sizes.pkl", 'wb') as file:
            pickle_rick.dump(self.sizes, file)
        with open(f"saves/{prefix}/layers.pkl", 'wb') as file:
            hidden_layers = self.layers[1:-1]
            pickle_rick.dump(hidden_layers, file)
    
    def load(self, prefix):
        with open(f"saves/{prefix}/sizes.pkl", 'rb') as sizes:
            with open(f"saves/{prefix}/layers.pkl", 'rb') as layers:
                self.sizes = pickle_rick.load(sizes)
                hidden_layers = pickle_rick.load(layers)
                self.layers = np.asarray([Layer(self.sizes[0])] + hidden_layers + [Layer(self.sizes[-1])])
                
                return self.layers
            
def superman(data, num_copies=1024, survival_rate=0.1, finish=128, sizes=[28*28, 16, 16, 16, 10], num_random=50): # genetic algorithm
    survivors:List[Network] = []
    while finish >= 0:
        networks:List[Network] = survivors + [Network(sizes) for i in range(num_copies - len(survivors))]
        
        for network in networks:
            output = network.forward_prop() # set input
            cost = network.cost() # set the correct data
            if len(survivors) < num_copies*survival_rate:
                survivors.append(network)
                survivors.sort(key=lambda net: net.cost)
            elif cost < survivors[-1].cost:
                survivors[-1] = network
                survivors.sort(key=lambda net: net.cost)
                
            
        finish -= 1

if __name__ == "__main__":
    superman()

## Calc output for a single nueron given weights, bias, and inputs

# a = current activation function
#     def forward(self, a):
#         for w,b in zip(self.weights, self.biases):
#             a = sigmoid(np.dot(w,a) + b)
#         return a

