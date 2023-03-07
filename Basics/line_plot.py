import sys
import numpy as np
from vispy import scene
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QApplication
from vispy.scene.visuals import Line



class LinePlot(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Generate some dummy data
        n = 30
        x = np.linspace(200, 600, n).astype(np.int32)
        pod = np.random.randint(low=100, high=800, size= n)
        precision = np.random.randint(low=100, high=800, size= n)
        recall = np.random.randint(low=100, high=800, size= n)
        f1 = np.random.randint(low=100, high=800, size= n)



        # Set the data for the line plots
    
        self.canvas = scene.SceneCanvas(keys='interactive')

        # Create a PyQt5 widget to display the canvas
        layout = QVBoxLayout()
        layout.addWidget(self.canvas.native)
        self.setLayout(layout)

        self.view = self.canvas.central_widget.add_view()

        # Create a scatter plot
        # scatter = Markers( pos=np.array([[0, 0], [5,5], [60, 500]], float), parent=self.view.scene,  edge_color="lightblue", size=10)
        # Create the line visuals
        
        Line(pos=np.column_stack((x, pod)) ,parent= self.view.scene, color="orange", width=2.0)
        Line(pos=np.column_stack((x, precision)), parent= self.view.scene, color="blue", width=2.0)
        Line(pos=np.column_stack((x, recall)), parent= self.view.scene, color="red", width=2.0)
        Line(pos=np.column_stack((x, f1)), parent= self.view.scene, color="green", width=2.0)

        # Add the scatter plot to the canvas
        #self.canvas.add_visual(scatter)

        self.setWindowTitle('Line Plot')
        self.setGeometry(100, 100, 800, 800)

if __name__ == '__main__':
    appQt = QApplication(sys.argv)
    scatterPlot = LinePlot()
    scatterPlot.show()
    appQt.exec_()
