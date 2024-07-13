from PIL import Image
from numpy import asarray
import numpy as np
import sys
import matplotlib
import os

class DataPreparation:
    def __init__(self,directory):
        self.directory = directory
        self.image_paths = []
        self.image_data = []
    
    def get_images(self):
        for file in os.listdir(directory):
            if file.endswith('.png'):
                self.image_paths.append(os.path.join(self.directory,file))
    
    def create_data(self):
        for file in self.image_paths:
            img = Image.open(file)
            image_data = asarray(img)
            self.image_data.append(image_data)
        np.array(self.image_data)
        return self.image_data
    
if __name__ == "__main__":
    directory = r'by_field\by_field\hsf_0\const\4a'
    data = DataPreparation(directory)
    data.get_images()
    print(data.create_data())
