import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

IMG_WIDTH = 28
IMG_HEIGHT = 28

class DataPreparation:
    def __init__(self, filename):
        self.file_name = filename
        self.train_image_data = []
        self.test_image_data = []
        self.image_height, self.image_width = IMG_HEIGHT, IMG_WIDTH
        self.num_images = 0

    def load_train_image_data(self):
        with open(self.file_name, 'rb') as file:
            train_data = file.read()
            magic_number = int.from_bytes(train_data[:4], 'big')
            num_images = int.from_bytes(train_data[4:8], 'big')
            rows = int.from_bytes(train_data[8:12], 'big')
            cols = int.from_bytes(train_data[12:16], 'big')
            assert magic_number == 2051
            assert rows == self.image_height and cols == self.image_width
            image_data = np.frombuffer(train_data[16:], dtype=np.uint8)

        self.num_images = num_images
        self.image_data = image_data.reshape(self.num_images, self.image_height, self.image_width)
        return self
    
    def load_test_image_data(self):
        with open(self.file_name, 'rb') as file:
            labels_data = file.read()
            magic_number = int.from_bytes(labels_data[:4], 'big')
            num_labels = int.from_bytes(labels_data[4:8], 'big')
            assert magic_number == 2049
            
            labels = np.frombuffer(labels_data[8:], dtype=np.uint8)
        
        self.test_image_data = []
        for label in labels:
            one_hot = np.zeros(10, dtype=np.uint8)
            one_hot[label] = 1
            self.test_image_data.append(one_hot)
        
        self.test_image_data = np.array(self.test_image_data)
        return self
    
    def normalize_data(self):
        self.train_image_data = self.train_image_data / 255.0
        return self

    def flatten_data(self):
        self.train_image_data = self.train_image_data.reshape(self.num_images, -1)
        return self

    def get_train_data(self):
        return self.train_image_data
    
    def get_test_data(self):
        return self.test_image_data

if __name__ == '__main__':

    #np.set_printoptions(threshold=np.inf)
    """
    Use this format to initialize the data
    
    train_data = DataPreparation(r"mnist-ds\train-images.idx3-ubyte") \
                    .load_train_image_data() \
                    .normalize_data() \
                    .flatten_data() \
                    .get_train_data()

    test_data = DataPreparation(r"mnist-ds\train-labels.idx1-ubyte") \
                    .load_test_image_data() \
                    .get_test_data()
    """
    
    # with open('training.txt','w') as file:
    #     file.write(str(train_data))
    # with open('testing.txt','w') as file:
    #     file.write(str(test_data))
