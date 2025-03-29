from PySide6.QtWidgets import QWidget


class DrawingAreaView(QWidget):
    def __init__(self, DrawingAreaController):
        super().__init__()
        self.setMinimumSize(500, 500)
        self.DrawingAreaController = DrawingAreaController
        self.TableModel = None
        self.TableController = None
        self.setMouseTracking(True)

    def setupUI(self):
        self.setObjectName(u"DrawingArea")

    def setTableModel(self, TableModel):
        self.TableModel = TableModel

    def mouseMoveEvent(self, event):
        self.DrawingAreaController.handleMouseMove(event)
        self.update()

    def mousePressEvent(self, event):
        self.DrawingAreaController.handleMousePress(event)
        self.update()

    def paintEvent(self, event):
        self.DrawingAreaController.handlePaintEvent()
