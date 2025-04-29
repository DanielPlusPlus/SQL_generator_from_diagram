from PySide6.QtGui import QPainter, QPen, QColor, QFont
from PySide6.QtCore import Qt, QRect

from app.models.TablesModel import TableModel


class TablesView:
    def __init__(self, TablesModel, ParentWindow):
        self.TablesModel = TablesModel
        self.ParentWindow = ParentWindow
        self.drawTables()

    def drawTempTable(self, position, width=100, rowsHeight=20, rowsNumber=5):
        Painter = QPainter(self.ParentWindow)
        Painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.PenStyle.SolidLine))
        CreatedTable = TableModel(position.x(), position.y(), width, rowsHeight, rowsNumber, 0)
        self.drawTable(Painter, CreatedTable)

    def drawTables(self):
        Painter = QPainter(self.ParentWindow)
        Painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.PenStyle.SolidLine))
        tables = self.TablesModel.getTables()
        for ObtainedTable in tables:
            self.drawTable(Painter, ObtainedTable)

    def drawTable(self, Painter, ObtainedTable):
        obtainedTableColumns = ObtainedTable.getTableColumns()

        font = QFont("Sans", 10)
        font.setBold(True)
        Painter.setFont(font)

        titleRectangle = QRect(
            ObtainedTable.getLeft(),
            ObtainedTable.getTop() - ObtainedTable.getRowHeight(),
            ObtainedTable.getTableWidth(),
            ObtainedTable.getRowHeight()
        )
        Painter.drawText(titleRectangle, Qt.AlignCenter, ObtainedTable.getTableName())

        for row in range(ObtainedTable.getRowsNumber()):
            y = ObtainedTable.getTop() + row * ObtainedTable.getRowHeight()
            rowRectangle = QRect(ObtainedTable.getLeft(), y, ObtainedTable.getTableWidth(),
                                 ObtainedTable.getRowHeight())
            Painter.drawRect(rowRectangle)
            if row < len(obtainedTableColumns):
                Painter.drawText(rowRectangle, Qt.AlignCenter, f"{obtainedTableColumns[row]["columnName"]}")
        Painter.drawRect(ObtainedTable.getRectangle())
