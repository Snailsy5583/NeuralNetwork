import numpy as np

class Neuron():
    def __init__(self, numOfWeights):
        self.value = 0
        
        self.weights = np.random.randn(numOfWeights)
        self.bias = np.random.rand()