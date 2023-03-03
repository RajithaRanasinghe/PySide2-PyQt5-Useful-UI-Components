from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide2.QtWebEngineWidgets import QWebEngineView
import folium.plugins
import random
import numpy as np

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for the map
        layout = QVBoxLayout(self)

        # Create a folium map centered on the equator
        m = folium.Map(location=[40.75, 73.97], tiles='stamentoner',control_scale = True, zoom_start=13)

        # Generate some random data for each location
        data = []
        for lat in np.arange(40.7500, 40.760, 0.001):
            for lon in np.arange(73.9700, 73.9800, 0.001):
                data.append((lat, lon, random.uniform(0, 1)))
        
        # Add a heatmap layer to the map
        #heatmap = folium.plugins.HeatMap(data, name='Heatmap', min_opacity=0.5, max_val=10)
        heatmap = folium.plugins.HeatMap(data, radius = 20, gradient={.2: 'green', .5: 'blue', .8: 'yellow', 1: 'red'})

        
        heatmap.add_to(m)

        # Add a layer control to the map
        folium.LayerControl().add_to(m)

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
