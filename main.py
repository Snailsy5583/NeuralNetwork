import PIL
from PySide6.QtGui import QMouseEvent
import numpy as np
import sys
import matplotlib

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Draw something")
        self.setGeometry(500, 300, 120, 120)
        
        self.image = QPixmap(120, 120)
        self.image.fill(QColor(0,0,0))
        
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFixedSize(120, 120)
        
        self.label.setPixmap(self.image)
        
        self.lastPoint = 0
        self.brushSize = 3
        
        io = QIODevice()
        self.imageData = self.image.save(io, "PNG")
        
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
        
        self.lastPoint = event.position()
        
    


app = QApplication(sys.argv)
w = MainWindow()
sys.exit(app.exec())