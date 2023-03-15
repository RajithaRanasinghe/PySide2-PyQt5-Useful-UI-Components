import pyqtgraph as pg
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide2.QtCore import QTimer
import numpy as np

class RealtimeMap(pg.GraphicsLayoutWidget):
    def __init__(self):
        super().__init__()

        # create a plot item and add it to the layout
        self.plot_item = self.addPlot()
        self.plot_item.showAxis('left', False)
        self.plot_item.showAxis('bottom', False)

        # create a scatter plot item to display the markers
        self.scatter = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
        self.plot_item.addItem(self.scatter)

        # set the range of the plot item to show the whole world
        self.plot_item.setRange(xRange=(-180, 180), yRange=(-90, 90))

    def update_map(self, latitude, longitude, value):
        # create a color map based on the measurement values
        cmap = pg.ColorMap([-1, 0, 1], [(255, 0, 0), (255, 255, 255), (0, 0, 255)])

        # map the measurement values to colors using the color map
        colors = cmap.map(value)

        # create a list of positions and colors for the markers
        pos = [{'pos': (longitude[i], latitude[i]), 'brush': colors[i]} for i in range(len(latitude))]

        # update the scatter plot item with the new positions and colors
        self.scatter.setData(pos)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # create an instance of RealtimeMap
        map_widget = RealtimeMap()

        # Create a layout for the map
        layout = QVBoxLayout(self)

        # add the map widget to the main window
        layout.addWidget(map_widget)

        # start a timer to update the map every second
        timer = QTimer()
        timer.timeout.connect(lambda: map_widget.update_map(latitude = np.random.uniform(75.0, 76.0), longitude = np.random.uniform(170.0, 171.0), value = np.random.uniform(0, 100)))
        timer.start(1000)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
