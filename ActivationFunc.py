import numpy as np

class ActivationFunction:

	def __init__(self):
		pass

	def sigmoid(x):
		return 1.0/(1.0+np.exp(-x))
	
	def sigmoid_der(x):
		return np.exp(-x) / ((1.0+np.exp(-x)) ** 2)
	
	def tanh(x):
		return np.tanh(x)
	
	def ReLU(x):
		return max(0.0,x)
	
	def softmax(x):
		pass #implement after neuron and layer have been implemented

	#allow for user input to choose different activation functions 