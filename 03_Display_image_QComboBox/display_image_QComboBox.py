import sys
import os
import numpy as np
try:
    import PySide2
    print("PySide2 Detected")
except:
    pass
try:
    import PyQt5
    print("PySide2 Detected")
except:
    pass

if 'PySide2' in sys.modules:
    from PySide2.QtGui import QPixmap,QPalette,QColor,QPainter, QPen, QBrush, QImage
    from PySide2.QtWidgets import QWidget,QComboBox,QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen,QTabWidget,QMainWindow,QLabel,QStyleFactory,QDialogButtonBox
    from PySide2.QtCore import QTimer,Qt,QSize
elif 'PyQt5' in sys.modules:
    from PyQt5.QtGui import QPixmap,QPalette,QPainter, QPen, QColor, QBrush, QImage
    from PyQt5.QtWidgets import QWidget,QComboBox,QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen,QTabWidget,QMainWindow,QLabel,QStyleFactory,QDialogButtonBox
    from PyQt5.QtCore import QTimer,Qt,QSize,QColor
else:
    print("Missing PySide2 or PyQt5")

class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.title = "Image Example"
        self.setWindowTitle(self.title)
        
        # Set graphic widget
        self.FILE_NAME = "sample.png" 
        self.graphic_wdgt =  QLabel(self)

        
        self.saveImageShow(self.FILE_NAME)
        #self.randomImageShow()
        self.initUI()
        self.select_img_cmbx.activated.connect(self.selectImage)

    def selectImage(self):
        i = self.select_img_cmbx.currentText()
        if i == "Saved Image":
            self.saveImageShow(self.FILE_NAME)
        elif i == "Random Generated Image":
            self.randomImageShow()


    def numpyToQimage(self, numpy_Array):
        w = numpy_Array.shape[0]
        h = numpy_Array.shape[1]
        channels = numpy_Array.shape[2]
        bytesPerLine = channels * w
        print('image width = {} height = {} channels = {}'.format(w,h,channels))
        QimagefromNumpy = QImage(numpy_Array.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)
        return QimagefromNumpy


    def randomImageShow(self):
        image_numpy = np.random.randint(0, 256, size = (300, 300, 3)).astype(np.uint8)
        image_numpy[100:200,100:200,0] = 255

        randomQimage = self.numpyToQimage(image_numpy)

        pixmap = QPixmap()
        self.resize(pixmap.width(),pixmap.height())
        pixmap.convertFromImage(randomQimage)
        self.graphic_wdgt.setPixmap(pixmap)



    def saveImageShow(self, FILE_NAME):
        FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),FILE_NAME)
        saveImg = QImage(FILE_PATH)
        pixmap = QPixmap()
        self.resize(pixmap.width(),pixmap.height())
        pixmap.convertFromImage(saveImg)
        self.graphic_wdgt.setPixmap(pixmap)



    def initUI(self):
        # Set Layout
        self.verticle_layout = QVBoxLayout()
        self.verticle_widget = QWidget()
        # Select Image
        self.select_img_label = QLabel("Select Image")
        self.select_img_cmbx = QComboBox()
        self.select_img_cmbx.addItem("Saved Image")
        self.select_img_cmbx.addItem("Random Generated Image")

        # add layouts to widget
        self.verticle_layout.addWidget(self.select_img_label)
        self.verticle_layout.addWidget(self.select_img_cmbx)
        self.verticle_layout.addWidget(self.graphic_wdgt)

        self.verticle_widget.setLayout(self.verticle_layout)
        self.setCentralWidget(self.verticle_widget)

 

if __name__ == '__main__':
    sys.argv.append('--no-sandbox')
    app = QApplication(sys.argv)
    QApplication.processEvents()
    main = Main()
    main.show()
    sys.exit(app.exec_())