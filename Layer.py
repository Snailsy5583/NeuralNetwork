from Neuron import *
from DataPreparation import DataPreparation
from ActivationFunc import ActivationFunction as af
import numpy as np
import timeit

class Layer:
    #retrieve weights, inputs, and bias from first iteration
    #pass previous layer input into new layer (output of first iteration serves as input of next)
    def __init__(self, num_neurons, prev_layer=None):
        self.num_neurons = num_neurons
        self.prev_layer = prev_layer
        
        num_weights = prev_layer.num_neurons if prev_layer else 0
        self.neurons = [Neuron(num_weights) for i in range(num_neurons)]
    
    def forward_prop(self):
        if not self.prev_layer:
            return None
        mat1 = np.asmatrix(np.append(np.asarray(self.prev_layer.getValues()), 1))
        
        mat2 = np.asmatrix([np.append(neuron.weights,neuron.bias) for neuron in self.neurons])
        mat2 = mat2.T
        
        values = np.asarray(np.matmul(mat1, mat2)).flatten()
        
        self.setValues(values, af.sigmoid)
        
        return self.getValues()
    
    def forward_prop_dot(self):
        if not self.prev_layer:
            return None
        mat1 = np.asmatrix(self.prev_layer.getValues())
        
        mat2 = np.asmatrix([neuron.weights for neuron in self.neurons])
        mat2 = mat2.T
        
        values = np.asarray(np.dot(mat1, mat2) + np.asarray([neuron.bias for neuron in self.neurons])).flatten()
        
        self.setValues(values, af.sigmoid)
        
        return self.getValues()
    
    def backward_prop(self,output_gradient):
        pass
    
    def getValues(self):
        return [neuron.value for neuron in self.neurons]
    
    def setValues(self, values, activationFunc=af.linear):
        for i in range(len(values)):
            self.neurons[i].value = activationFunc(values[i])
            
    def getWeights(self):
        return [neuron.weights for neuron in self.neurons]
    
    def getBiases(self):
        return [[neuron.bias] for neuron in self.neurons]
    
    def getNeurons(self):
        return self.neurons

    
np.set_printoptions(threshold=np.inf)
x = Layer(20)
z = Layer(16, x)
#print(x.weights.shape)
# dp = DataPreparation(r'by_field\by_field\hssf_8')
# dp.get_images()
# x.setValues(dp.create_data())
print(z.forward_prop())
print(z.forward_prop_readable())
print(z.forward_prop_dot())