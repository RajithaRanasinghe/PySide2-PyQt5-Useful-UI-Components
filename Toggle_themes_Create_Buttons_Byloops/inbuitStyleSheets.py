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
    from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen,QTabWidget,QMainWindow,QLabel,QStyleFactory,QDialogButtonBox
    from PySide2.QtCore import QTimer,Qt,QSize
elif 'PyQt5' in sys.modules:
    from PyQt5.QtGui import QPixmap
    from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen,QTabWidget,QMainWindow,QLabel,QStyleFactory,QDialogButtonBox
    from PyQt5.QtCore import QTimer,Qt,QSize
else:
    print("Missing PySide2 or PyQt5")

class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.styleSheetList = QStyleFactory.keys()
        self.buttonBox = QDialogButtonBox(Qt.Vertical)
        self.setFixedSize(QSize(800, 480))

        self.buttonarray = {}
        for i,style in enumerate(self.styleSheetList):
            self.buttonarray['btn_'+str(style)] = QPushButton(str(style))
            self.buttonarray['btn_'+str(style)].setObjectName('button_{}'.format(style))
            s = self.buttonarray['btn_'+str(style)].text()
            self.buttonarray['btn_'+str(style)].clicked.connect((lambda  s=s : lambda :self.setUserStyle(s))())             
            self.buttonBox.addButton(self.buttonarray['btn_'+str(style)], QDialogButtonBox.ActionRole)

        self.setCentralWidget(self.buttonBox)

    def setUserStyle(self, style):
        print("Selected Style = {}".format(style))
        app.setStyle(style)


if __name__ == '__main__':
    sys.argv.append('--no-sandbox')
    app = QApplication(sys.argv)
    QApplication.processEvents()
    main = Main()
    main.show()
    sys.exit(app.exec_())