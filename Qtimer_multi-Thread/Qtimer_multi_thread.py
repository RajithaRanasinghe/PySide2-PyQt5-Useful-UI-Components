import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class ModbusComWorker(QObject):
    finished = Signal()

    def start(self):
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.process)
        self._timer.start(2000)

    def stop(self):
        self._timer.stop()
        self.finished.emit()

    def process(self):
        print('processing (thread: %r)' % QThread.currentThread())
        QThread.sleep(3)

if __name__ == "__main__":

    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    thread = QThread()
    worker = ModbusComWorker()
    worker.moveToThread(thread)

    def finish():
        print('shutting down...')
        thread.quit()
        thread.wait()
        app.quit()
        print('stopped')

    worker.finished.connect(finish)
    thread.started.connect(worker.start)
    thread.start()

    timer = QTimer()
    timer.setSingleShot(True)
    timer.timeout.connect(worker.stop)
    timer.start(15000)

    print('starting (thread: %r)' % QThread.currentThread())

    sys.exit(app.exec_())