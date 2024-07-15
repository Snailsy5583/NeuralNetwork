import sys
import threading
import time

import Testing

def drawCallback(image):
    print("sigma")
    print(image)
    

app, w = Testing.gen(drawCallback)
    
sys.exit(app.exec())
