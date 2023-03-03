import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PySide2.QtCore import Qt
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a plain text edit widget
        self.text_edit = QPlainTextEdit()
        self.setCentralWidget(self.text_edit)

        # Redirect standard output and error streams to the text edit
        sys.stdout = TextEditStream(stdout=True, parent=self.text_edit)
        sys.stderr = TextEditStream(stdout=False, parent=self.text_edit)

        # Set some options for the text edit
        self.text_edit.setReadOnly(True)
        self.text_edit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.test()

    def test(self):
        for i in range(5):
            print(f"Message {i+1}")
        time.sleep(1)

class TextEditStream:
    def __init__(self, stdout=True, parent=None):
        self.stdout = stdout
        self.parent = parent

    def write(self, message):
        # Write the message to the text edit
        self.parent.insertPlainText(message)

    def flush(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
