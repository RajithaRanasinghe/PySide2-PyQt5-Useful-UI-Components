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
    from PySide2.QtGui import QPixmap,QPalette,QColor
    from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen,QTabWidget,QMainWindow,QLabel,QStyleFactory,QDialogButtonBox
    from PySide2.QtCore import QTimer,Qt,QSize
elif 'PyQt5' in sys.modules:
    from PyQt5.QtGui import QPixmap,QPalette
    from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen,QTabWidget,QMainWindow,QLabel,QStyleFactory,QDialogButtonBox
    from PyQt5.QtCore import QTimer,Qt,QSize,QColor
else:
    print("Missing PySide2 or PyQt5")

class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.styleSheetList = QStyleFactory.keys()
        self.buttonBox = QDialogButtonBox(Qt.Vertical)
        self.setFixedSize(QSize(800, 480))
        self.colorPalettes()

        self.buttonarray = {}
        for i,style in enumerate(self.styleSheetList):
            self.buttonarray['btn_'+str(style)] = QPushButton(str(style))
            self.buttonarray['btn_'+str(style)].setObjectName('button_{}'.format(style))
            s = self.buttonarray['btn_'+str(style)].text()
            self.buttonarray['btn_'+str(style)].clicked.connect((lambda  s=s : lambda :self.setUserStyle(s))())             
            self.buttonBox.addButton(self.buttonarray['btn_'+str(style)], QDialogButtonBox.ActionRole)

        self.btn_dark = QPushButton('Dark')
        self.btn_light = QPushButton('Light')
        self.btn_dark.clicked.connect(self.setDarkPalette)
        self.btn_light.clicked.connect(self.setLightPalette)
        self.buttonBox.addButton(self.btn_dark, QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.btn_light, QDialogButtonBox.ActionRole)

        self.setCentralWidget(self.buttonBox)

    def setUserStyle(self, style):
        print("Selected Style = {}".format(style))
        app.setStyle(style)

    def setDarkPalette(self):
        app.setPalette(self.dark_palette)

    def setLightPalette(self):
        app.setPalette(self.default_palette)

    def colorPalettes(self):
        self.default_palette = QPalette()
        self.dark_palette = QPalette()
        self.dark_palette = QPalette()
        self.dark_palette.setColor(QPalette.Window, QColor(50, 50, 50))
        self.dark_palette.setColor(QPalette.WindowText, Qt.white)
        self.dark_palette.setColor(QPalette.Base, QColor(0, 0, 0))
        self.dark_palette.setColor(QPalette.AlternateBase, QColor(50, 50, 50))
        self.dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        self.dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        self.dark_palette.setColor(QPalette.Text, Qt.white)
        self.dark_palette.setColor(QPalette.Button, QColor(50, 50, 50))
        self.dark_palette.setColor(QPalette.ButtonText, Qt.white)
        self.dark_palette.setColor(QPalette.BrightText, Qt.red)
        self.dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        self.dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        self.dark_palette.setColor(QPalette.HighlightedText, Qt.black)


if __name__ == '__main__':
    sys.argv.append('--no-sandbox')
    app = QApplication(sys.argv)
    QApplication.processEvents()
    main = Main()
    main.show()
    sys.exit(app.exec_())