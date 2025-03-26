from PySide6.QtWidgets import QWidget


class DrawingAreaView(QWidget):
    def __init__(self, DrawingAreaController):
        super().__init__()
        self.DrawingAreaController = DrawingAreaController
        self.setMouseTracking(True)

    def setupUI(self):
        self.setObjectName(u"DrawingArea")

    def mouseMoveEvent(self, event):
        self.DrawingAreaController.handleMouseMove(event)
        self.update()

    def mousePressEvent(self, event):
        self.DrawingAreaController.handleMousePress(event)
        self.update()
