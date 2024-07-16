import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

class DataPreparation:

    def __init__(self):
        (self.x_train, self.y_train), (self.x_test, self.y_test) = keras.datasets.mnist.load_data()

    def flatten_array(self):
        self.x_train = np.array(self.x_train.reshape((len(self.x_train)),(int(self.x_train.shape[1]) * int(self.x_train.shape[2]))))
        self.x_test = np.array(self.x_test.reshape((len(self.x_test)),(int(self.x_test.shape[1]) * int(self.x_test.shape[2]))))
    
    def select_num_images(self):
        pass

    def normalize_array(self):
        self.x_train = self.x_train.astype(np.float32)
        for i in range(len(self.x_train)):
            self.x_train[i] = ((self.x_train[i]) / 255.0) 

    def show_image(self):
        plt.matshow(self.x_train)
        plt.show()

if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)
    db = DataPreparation()
    db.flatten_array()
    db.normalize_array()
    print(db.x_train[0])
    print(db.x_test.shape)
    db.show_image() 
