import sys
import threading
import time

import Testing
from Network import Network as net
import numpy as np

# def drawCallback(image):
#     print("sigma")
#     print(image)
    

# app, w = Testing.gen(drawCallback)
    
# sys.exit(app.exec())

Layers = [8,4,2]
Data = np.asarray([1,2,3,4,5,6,7,8])
parameters = net.intialize2(Layers)
out = net(Layers).forward_model(Data, parameters)
print(out)
