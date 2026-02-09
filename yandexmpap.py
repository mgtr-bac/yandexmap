import sys
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt


class MapApp(QWidget):
    def __init__(self):
        super().__init__()
        self.lat = 55.753630
        self.lon = 37.620070
        self.zoom = 15
        self.initUI()
        self.update_map()

    def initUI(self):
        self.setGeometry(100, 100, 600, 450)
        self.setWindowTitle('Map Application')
        self.map_label = QLabel(self)
        self.map_label.resize(600, 450)

    def update_map(self):
        map_params = {
            "ll": f"{self.lon},{self.lat}",
            "z": self.zoom,
            "l": "map",
            "size": "600,450"
        }
        api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(api_server, params=map_params)

        if response:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.map_label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.zoom < 21:
                self.zoom += 1
                self.update_map()
        elif event.key() == Qt.Key_PageDown:
            if self.zoom > 0:
                self.zoom -= 1
                self.update_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapApp()
    ex.show()
    sys.exit(app.exec_())