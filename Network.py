import os
import random
import pickle
import numpy as np

from Layer import *
from ActivationFunc import ActivationFunction as AF   

class Network():
    # sizes is list of nums for number of neurons at each layer
    def __init__(self, sizes):
        self.sizes = sizes
        self.numLayers = len(sizes)
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
    
    def cost(self, batman):
        output = self.layers[-1]
        error = 0
        for i in range(len(batman)):
            error += (batman[i] - output[i])**2
        
        return error

    

        #back
        
    def save(self, prefix:str):
        os.mkdir(f"saves/{prefix}")
        with open(f"saves/{prefix}/sizes.pkl", 'wb') as file:
            pickle.dump(self.sizes, file)
        with open(f"saves/{prefix}/layers.pkl", 'wb') as file:
            hidden_layers = self.layers[1:-1]
            pickle.dump(hidden_layers, file)
    
    def load(self, prefix):
        with open(f"saves/{prefix}/sizes.pkl", 'rb') as sizes:
            with open(f"saves/{prefix}/layers.pkl", 'rb') as layers:
                self.sizes = pickle.load(sizes)
                hidden_layers = pickle.load(layers)
                self.layers = np.asarray([Layer(self.sizes[0])] + hidden_layers + [Layer(self.sizes[-1])])
                
                return self.layers

if __name__ == "__main__":
    network = Network([28*28, 16, 16, 16, 10])
    network.save("sussy")
    print(network.sizes)
    print(network.layers[2].getWeights())

## Calc output for a single nueron given weights, bias, and inputs

# a = current activation function
#     def forward(self, a):
#         for w,b in zip(self.weights, self.biases):
#             a = sigmoid(np.dot(w,a) + b)
#         return a

