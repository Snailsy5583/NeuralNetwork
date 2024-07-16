from Neuron import *
from DataPreparation import DataPreparation
import numpy as np

class Layer:
    #retrieve weights, inputs, and bias from first iteration
    #pass previous layer input into new layer (output of first iteration serves as input of next)
    def __init__(self, num_neurons, prev_layer=None):
        self.num_neurons = num_neurons
        self.prev_layer = prev_layer
        
        self.neurons = [Neuron(len(prev_layer.getNeurons()) if prev_layer else 0) for i in range(num_neurons)]
        self.weights = np.random.randn(num_neurons)
        self.biases = np.random.randn(num_neurons)
        
        self.values = []
    
    def forward_prop(self,inputs):
        if not self.prev_layer:
            return None
        mat1 = np.array(self.prev_layer.values)
        print(mat1.shape)
        mat2 = np.array([np.append(neuron.weights,[neuron.bias]) for neuron in self.neurons])
        print(mat2.shape)
        mat2[:] = mat2.T
        
        self.values = np.matmul(mat1, mat2)
        
        return self.values
    
    def backward_prop(self,output_gradient):
        pass
    
    def values(self):
        return self.values
    
    def getNeurons(self):
        return self.neurons

    
# np.set_printoptions(threshold=np.inf)
# x = Layer(356000)
# z = Layer(16,x)

# #print(x.weights.shape)
# dp = DataPreparation(r'by_field\by_field\hssf_8')
# dp.get_images()
# #print(dp.create_data().shape)
# print(z.forward_prop(dp.create_data()))

    