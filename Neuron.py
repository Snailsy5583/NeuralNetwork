import numpy as np

def sigmoid(x):
        return 1.0/(1.0+np.exp(-x))


class Neuron():
    def __init__(self):
        self.value = 0
        
        self.weights = []
        self.bias = 0