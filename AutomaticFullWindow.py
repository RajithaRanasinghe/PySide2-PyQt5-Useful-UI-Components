import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QScrollArea

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget with a layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Add a label to the layout
        label = QLabel("Hello, World!")
        layout.addWidget(label)

        # Create a scroll area and set its widget to the central widget
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(central_widget)

        # Set the QMainWindow's central widget to the scroll area
        self.setCentralWidget(scroll_area)

        # Set the window title and show the window maximized
        self.setWindowTitle("My Window")
        self.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
