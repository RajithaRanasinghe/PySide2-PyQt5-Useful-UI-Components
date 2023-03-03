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
        m = folium.Map(location=[75, 170], zoom_start=2)

        # Generate some random data for each location
        data = []
        for lat in np.arange(75.0, 76.0, 0.1):
            print(lat)
            for lon in np.arange(170.0, 171.0, 0.1):
                data.append((lat, lon, random.uniform(0, 100)))
        
        # Add a heatmap layer to the map
        #heatmap = folium.plugins.HeatMap(data, name='Heatmap', min_opacity=0.5, max_val=10)
        heatmap = folium.plugins.HeatMap(
            data,
            name='Heatmap',
            min_opacity=0.5,
            max_val=100,
            gradient={
                0.4: 'blue',
                0.6: 'yellow',
                1.0: 'red'
            }
        )

        
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
