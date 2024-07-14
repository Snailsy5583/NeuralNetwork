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
            if file.endswith('.png') or file.endswith('.jpg'):
                self.image_paths.append(os.path.join(self.directory,file))
    
    def create_data(self):
        for file in self.image_paths:
            img = Image.open(file).convert('RGB')
            raw_image_data = asarray(img)
            pixel_brightness_data = np.zeros(raw_image_data.shape[:2])
            for i in range(raw_image_data.shape[0]):
                for j in range(raw_image_data.shape[1]):
                    red, green, blue = raw_image_data[i,j]
                    pixel_brightness = (red) / 255
                    pixel_brightness_data[i,j] = pixel_brightness
        self.image_data = (pixel_brightness_data)
        new_image_data=  np.array(self.image_data).flatten()
        return new_image_data
if __name__ == "__main__":
    np.set_printoptions(threshold=np.inf)
    #Change directory based on what folder of images needs to used for training
    directory = r'by_field\by_field\hssf_8'
    data = DataPreparation(directory)
    data.get_images()
    with open('inputs.txt', 'w') as file:
        file.write(str(data.create_data()))
        file.write(str(data.create_data().shape))

