import sys
import os
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
    from PySide2.QtGui import QPixmap
    from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen,QTabWidget,QMainWindow,QLabel
    from PySide2.QtCore import QTimer
elif 'PyQt5' in sys.modules:
    from PyQt5.QtGui import QPixmap
    from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen,QTabWidget,QMainWindow,QLabel
    from PyQt5.QtCore import QTimer
else:
    print("Missing PySide2 or PyQt5")

class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.FILE_NAME = 'logo_test.png'
        self.FOLDER_NAME = ''
        self.flashSplash(self.FILE_NAME,self.FOLDER_NAME)

        self.Label = QLabel("Main Application")
        self.setCentralWidget(self.Label)



    def flashSplash(self, FILE_NAME, FOLDER_NAME):
        FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__))+FOLDER_NAME,FILE_NAME)
        
        self.splash = QSplashScreen(QPixmap(FILE_PATH))

        self.splash.show()

        # Close SplashScreen after 5 seconds (5000 ms)
        QTimer.singleShot(5000, self.splash.close)
        # Splash Screen will close after opening Main widget
        self.splash.finish(self)

if __name__ == '__main__':
    sys.argv.append('--no-sandbox')
    app = QApplication(sys.argv)
    QApplication.processEvents()
    main = Main()
    main.show()
    sys.exit(app.exec_())