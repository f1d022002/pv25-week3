import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

class MouseTracker(QMainWindow):
    def __init__(huff):
        super().__init__()
        huff.initUI()
    
    def initUI(huff):
        huff.setWindowTitle("Tugas Week 3 - (F1D022002 - Andi Sibwayiq Abi Mahmud)")
        huff.setGeometry(100, 100, 600, 400)
        
        huff.label = QLabel("KLikk pak", huff)
        huff.label.setGeometry(200, 150, 200, 50)
        # 
        huff.label.setStyleSheet("background-color: white;")
        huff.label.setAlignment(Qt.AlignCenter)
        
        huff.setMouseTracking(True)
        huff.label.setMouseTracking(True)
    
    def mouseMoveEvent(huff, aksi):
        
        huff.label.setText(f"X: {aksi.x()}, Y: {aksi.y()}")
        
        if huff.label.geometry().contains(aksi.pos()):
            huff.relocateLabel()
    
    def relocateLabel(huff):
    
        max_x = huff.width() - huff.label.width()
        max_y = huff.height() - huff.label.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        huff.label.move(new_x, new_y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec_())