import Neuron
from DataPreparation import DataPreparation
import numpy as np

def sigmoid(x):
        return 1.0/(1.0+np.exp(-x))

class Layer:

    #retrieve weights, inputs, and bias from first iteration
    #pass previous layer input into new layer (output of first iteration serves as input of next)

    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.weights = np.random.randn(num_neurons)
        self.biases = np.random.randn(num_neurons)
    
    def forward_prop(self,inputs):
        self.output = (np.dot(self.weights, inputs) + self.biases)
        return self.output
    
    def backward_prop(self,output_gradient):
        pass

    
np.set_printoptions(threshold=np.inf)
x = Layer(356000)
#print(x.weights.shape)
dp = DataPreparation(r'by_field\by_field\hssf_8')
dp.get_images()
#print(dp.create_data().shape)
print(x.forward_prop(dp.create_data()))

    