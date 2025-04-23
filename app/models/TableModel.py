from PySide6.QtCore import QRect

from app.models.TableColumnsModel import TableColumnsModel


class TableModel:
    def __init__(self, x, y, width, rowHeight, rowsNumber, tableNumber):
        self.Rectangle = QRect(x - width // 2, y - (rowHeight * rowsNumber) // 2, width, rowHeight * rowsNumber)
        self.tableWidth = width
        self.rowHeight = rowHeight
        self.rowsNumber = rowsNumber
        self.tableNumber = tableNumber
        self.tableName = f"Table {tableNumber}"
        self.TableColumnsModel = TableColumnsModel()

    def getRectangle(self):
        return self.Rectangle

    def getTop(self):
        return self.Rectangle.top()

    def getLeft(self):
        return self.Rectangle.left()

    def getRight(self):
        return self.Rectangle.right()

    def getTableWidth(self):
        return self.tableWidth

    def getRowHeight(self):
        return self.rowHeight

    def getRowsNumber(self):
        return self.rowsNumber

    def getTableNumber(self):
        return self.tableNumber

    def getTableName(self):
        return self.tableName

    def editTableName(self, newName):
        self.tableName = newName

    def getTableColumnsModel(self):
        return self.TableColumnsModel

    def changeTableColumnsModel(self, NewTableColumnsModel):
        self.TableColumnsModel = NewTableColumnsModel

    def contains(self, point):
        if self.Rectangle.contains(point):
            return True

    def changeTablePosition(self, x, y):
        newRectangle = QRect(x - self.getTableWidth() // 2, y - (self.getRowHeight() * self.getRowsNumber()) // 2,
                             self.getTableWidth(), self.rowHeight * self.getRowsNumber())
        self.Rectangle = newRectangle
