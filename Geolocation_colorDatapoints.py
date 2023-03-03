from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide2.QtWebEngineWidgets import QWebEngineView
import folium
import folium.plugins
import random
import numpy as np


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for the map
        layout = QVBoxLayout(self)

        # Generate some random data for each location
        data = []

        for lat in np.arange(75.0, 76.0, 0.1):
            for lon in np.arange(170.0, 171.0, 0.1):
                value = random.uniform(0, 100)
                data.append((lat, lon, value))


        # Create a folium map centered on the equator
        m = folium.Map(location=[75.5, 170.5], zoom_start=2)

        # Create a color map for each data value
        #colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
        colors = ['#FFEDA0', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#B10026']
        color_map = {val: colors[i%len(colors)] for i, val in enumerate(sorted(set([d[2] for d in data])))}

        '''
        # Add markers to the map with a unique color for each data value
        for lat, lon, val in data:
            color = color_map[val]
            folium.Marker([lat, lon], icon=folium.Icon(color=color)).add_to(m)
        '''

        # Add a circle marker for each data point
        for lat, lon, val in data:
            color = color_map[val]
            folium.CircleMarker(location=[lat, lon], radius=10, fill=True, fill_color=color, fill_opacity=0.8, icon='square', stroke=False).add_to(m)
        



        # Convert the folium map to HTML and display it in a webview
        html = m.get_root().render()
        self.view = QWebEngineView()
        self.view.setHtml(html)
        layout.addWidget(self.view)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
