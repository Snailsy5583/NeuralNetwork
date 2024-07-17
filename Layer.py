from Neuron import *
from DataPreparation import DataPreparation
from ActivationFunc import ActivationFunction as af
import numpy as np
import time

class Layer:
    #retrieve weights, inputs, and bias from first iteration
    #pass previous layer input into new layer (output of first iteration serves as input of next)
    def __init__(self, num_neurons, prev_layer=None):
        self.num_neurons = num_neurons
        self.prev_layer = prev_layer
        
        num_weights = prev_layer.num_neurons if prev_layer else 0
        self.neurons = [Neuron(num_weights) for i in range(num_neurons)] 
    
    def forward_prop(self): #use this one
        if not self.prev_layer:
            return None
        mat1 = np.asmatrix(self.prev_layer.getValues())
        
        mat2 = np.asmatrix([neuron.weights for neuron in self.neurons])
        mat2 = mat2.T
        
        values = np.asarray(np.dot(mat1, mat2) + np.asarray([neuron.bias for neuron in self.neurons])).flatten()
        
        self.setValues(values, af.sigmoid)
        
        return self.getValues()
    
    def forward_prop_matmul(self):
        if not self.prev_layer:
            return None
        mat1 = np.asmatrix(np.append(np.asarray(self.prev_layer.getValues()), 1))
        
        mat2 = np.asmatrix([np.append(neuron.weights,neuron.bias) for neuron in self.neurons])
        mat2 = mat2.T
        
        values = np.asarray(np.matmul(mat1, mat2)).flatten()
        
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

class Layer_huh:
    '''
    Retrieve weights, inputs, and bias from first iteration
    Pass previous layer input into new layer (output of first iteration serves as input of next)
    Sets amount of weights and biases to the number of neurons in prev layer

    '''
    def __init__(self, num_neurons, prev_layer=None):
        self.num_neurons = num_neurons
        self.prev_layer = prev_layer
        self.values = []
        if prev_layer:
            self.weights, self.biases = self.init_w_zeros(prev_layer.getValues().shape[0])

    def forward_prop(self, W, b, input, activation):
        values = activation(np.dot(W, input) + b)
        self.values
        return values

    def cost_der(self, X, y):
        return(X - y)
    
    def backward_prop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        #F
        # activation = [x]
        # z = []
        # for b, w in zip(self.biases, self.weights):
        #     a = np.dot(w, x) + b
        #     z.append(a)

        #X is final layer of activations
        #y is peerdictions
        delta = self.cost_der(x, y) * af.sigmoid_der[x[-1]]

    
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
    

def test_prop(num):
    x = Layer_huh(16384)
    z = Layer_huh(16, x)
    
    dp = DataPreparation(r'by_field\by_field\hssf_8')
    dp.get_images()
    x.setValues(dp.create_data())
    
    t1 = time.time()
    for i in range(num):
        z.forward_prop()
    t2 = time.time()
    print(t2-t1)
    
    t1 = time.time()
    for i in range(num):
        z.forward_prop_matmul()
    t2 = time.time()
    print(t2-t1)


if __name__ == "__main__":
    test_prop(5000)