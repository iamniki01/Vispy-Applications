import sys
import numpy as np
from vispy import scene
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QApplication
from vispy.scene.visuals import Markers


class ScatterPlot(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create data for the scatter plot
        n = 300
        x = np.linspace(200, 600, n).astype(np.int32)
        pos = np.random.randint(low=100, high=800, size= n)
        
        

        # Create a canvas
        self.canvas = scene.SceneCanvas(keys='interactive')

        # Create a PyQt5 widget to display the canvas
        layout = QVBoxLayout()
        layout.addWidget(self.canvas.native)
        self.setLayout(layout)

        self.view = self.canvas.central_widget.add_view()

        # Create a scatter plot
        Markers( pos=np.column_stack((x, pos)), parent=self.view.scene,  edge_color="lightblue", size=10)

        # Add the scatter plot to the canvas
        #self.canvas.add_visual(scatter)

        self.setWindowTitle('Scatter Plot')
        self.setGeometry(100, 100, 800, 800)

if __name__ == '__main__':
    appQt = QApplication(sys.argv)
    scatterPlot = ScatterPlot()
    scatterPlot.show()
    appQt.exec_()
