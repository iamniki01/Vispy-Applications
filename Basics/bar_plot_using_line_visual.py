from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import vispy.scene
from vispy.scene import visuals
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create a QWidget to hold the vispy canvas
        canvas_widget = QWidget()

        # create a vispy canvas and add it to the QWidget
        canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
        canvas.create_native()
        canvas_widget.setLayout(QVBoxLayout())
        canvas_widget.layout().addWidget(canvas.native)

        # create a view for the vispy canvas
        view = canvas.central_widget.add_view()

        # create dummy data for the POD, Precision, and f1 score plots
        data = np.random.rand(10)

        x_values = np.arange(len(data))
        y_values = np.zeros(len(data))
        heights = data

        # create a LineVisual for each line in the bar graph
        line_visuals = []
        for i in range(len(x_values)):
            x = x_values[i]
            y = y_values[i]
            height = heights[i]
            line_visual = vispy.scene.visuals.Line(pos=np.array([(x, y), (x, y+height)]), color=(1.0, 0.0, 0.0, 1))
            line_visuals.append(line_visual)

        # add the LineVisuals to the view
        for line_visual in line_visuals:
            view.add(line_visual)

        # set the camera and axis labels for the view
        view.camera = vispy.scene.cameras.PanZoomCamera()
        view.camera.set_range((0, 10), (0, 1))
        view.camera.aspect = None
        view.camera.update()
        view.camera.set_default_state()
        view.camera.flip = (False, True, False)
        view.unfreeze()
        view.axis = vispy.visuals.xyz_axis.XYZAxisVisual()
        
        # set the layout of the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(QHBoxLayout())
        central_widget.layout().addWidget(canvas_widget)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
