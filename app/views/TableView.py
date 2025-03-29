from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt


class TableView:
    def __init__(self, TableModel, ParentWindow):
        self.TableModel = TableModel
        self.ParentWindow = ParentWindow
        self.drawTables()

    def drawTables(self):
        painter = QPainter(self.ParentWindow)
        painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.PenStyle.SolidLine))
        tables = self.TableModel.getTables()
        for table in tables:
            self.drawTable(painter, table)

    def drawTable(self, painter, table):
        for i in range(table.getRowsNumber() + 1):
            y = table.getTop() + i * table.getRowHeight()
            painter.drawLine(table.getLeft(), y, table.getRight(), y)
        painter.drawRect(table.getRectangle())
