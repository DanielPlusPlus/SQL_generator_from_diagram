from PySide6.QtCore import QRect

from app.models.TableColumnsModel import TableColumnsModel


class TableModel:
    def __init__(self, x, y, width, rowHeight, minRowsNumber, tableNumber):
        self.Rectangle = QRect(
            x - width // 2,
            y - (rowHeight * minRowsNumber) // 2,
            width,
            rowHeight * minRowsNumber
        )
        self.tableWidth = width
        self.rowHeight = rowHeight
        self.minRowsNumber = minRowsNumber
        self.rowsNumber = minRowsNumber
        self.tableNumber = tableNumber
        if not self.tableNumber:
            self.tableName = "New Table"
        else:
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

    def getTableColumns(self):
        return self.TableColumnsModel.columns

    def changeTableDimensions(self):
        self.rowsNumber = max(self.minRowsNumber, self.TableColumnsModel.rowCount())
        self.Rectangle = QRect(
            self.getLeft(),
            self.getTop(),
            self.tableWidth,
            self.rowsNumber * self.rowHeight
        )

    def changeTableColumnsModel(self, NewTableColumnsModel):
        self.TableColumnsModel = NewTableColumnsModel

    def changeTablePosition(self, x, y):
        newRectangle = QRect(
            x - self.getTableWidth() // 2,
            y - (self.getRowHeight() * self.getRowsNumber()) // 2,
            self.getTableWidth(),
            self.rowHeight * self.getRowsNumber()
        )
        self.Rectangle = newRectangle

    def contains(self, point):
        if self.Rectangle.contains(point):
            return True
