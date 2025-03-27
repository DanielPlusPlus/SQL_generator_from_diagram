from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt


class DrawingAreaView(QWidget):
    def __init__(self, DrawingAreaController):
        super().__init__()
        self.setMinimumSize(500, 500)
        self.DrawingAreaController = DrawingAreaController
        self.TableModel = None
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
        painter = QPainter(self)
        painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.PenStyle.SolidLine))

        for tableRectangle in self.TableModel.tables:
            self.drawTable(painter, tableRectangle)

    def drawTable(self, painter, tableRectangle):
        for i in range(5):
            y = tableRectangle.top() + i * 5
            painter.drawLine(tableRectangle.left(), y, tableRectangle.right(), y)
        painter.drawRect(tableRectangle)
