import sys

import PIL

import PIL.Image
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, drawCallback):
        super().__init__()
        
        self.drawCallback = drawCallback

        self.setWindowTitle("Draw something")
        self.setGeometry(500, 300, 128, 128)
        
        self.image = QPixmap(128, 128)
        self.image.fill(QColor(0,0,0))
        
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFixedSize(128, 128)
        
        self.label.setPixmap(self.image)
        
        self.lastPoint = 0
        self.brushSize = 3
        
        self.show()
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.lastPoint = event.position()
            
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        painter = QPainter()
        
        painter.begin(self.image)
        
        pen = QPen(Qt.GlobalColor.white, self.brushSize, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        
        painter.setPen(pen)
        painter.drawLine(self.lastPoint.toPoint(), event.position().toPoint())
        
        painter.end()
        
        self.label.setPixmap(self.image)
        self.drawCallback(self.getImage())
        
        self.lastPoint = event.position()

    def getImage(self):
        return PIL.Image.fromqpixmap(self.label.pixmap())

def gen(drawCallback):
    app = QApplication(sys.argv)
    w = MainWindow(drawCallback)
    
    return app, w