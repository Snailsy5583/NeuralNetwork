import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

IMG_WIDTH = 28
IMG_HEIGHT = 28

class DataPreparation:
    def __init__(self, filename):
        self.file_name = filename
        self.image_data = []
        self.image_height, self.image_width = IMG_HEIGHT, IMG_WIDTH
        self.num_images = 0

    def load_image_data(self):
        with open(self.file_name, 'rb') as file:
            data = file.read()
            magic_number = int.from_bytes(data[:4], 'big')
            num_images = int.from_bytes(data[4:8], 'big')
            rows = int.from_bytes(data[8:12], 'big')
            cols = int.from_bytes(data[12:16], 'big')
            assert magic_number == 2051
            assert rows == self.image_height and cols == self.image_width
            image_data = np.frombuffer(data[16:], dtype=np.uint8)

        self.num_images = num_images
        self.image_data = image_data.reshape(self.num_images, self.image_height, self.image_width)
        return self

    def normalize_data(self):
        self.image_data = self.image_data / 255.0
        return self

    def flatten_data(self):
        self.image_data = self.image_data.reshape(self.num_images, -1)
        return self

    def get_data(self):
        return self.image_data

if __name__ == '__main__':

    #np.set_printoptions(threshold=np.inf)
    """
    Use this format to initialize the data
    train_data = DataPreparation(r"mnist-ds\train-images.idx3-ubyte") \
                    .load_image_data() \
                    .normalize_data() \
                    .flatten_data() \
                    .get_data()

    test_data = DataPreparation(r"mnist-ds\t10k-images.idx3-ubyte") \
                    .load_image_data() \
                    .normalize_data() \
                    .flatten_data() \
                    .get_data()
    """
    # with open('training.txt','w') as file:
    #     file.write(str(train_data))
    # with open('testing.txt','w') as file:
    #     file.write(str(test_data))
