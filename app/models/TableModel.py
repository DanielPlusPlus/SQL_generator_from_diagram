from PySide6.QtCore import QPoint, QRect


class Table:
    def __init__(self, x, y, width, rowHeight, rowsNumber, tableNumber):
        self.Rectangle = QRect(x - width // 2, y - (rowHeight * rowsNumber) // 2, width, rowHeight * rowsNumber)
        self.tableWidth = width
        self.rowHeight = rowHeight
        self.rowsNumber = rowsNumber
        self.tableNumber = tableNumber

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

    def contains(self, point):
        if self.Rectangle.contains(point):
            return True

    def changeTablePosition(self, x, y):
        newRectangle = QRect(x - self.getTableWidth() // 2, y - (self.getRowHeight() * self.getRowsNumber()) // 2,
                             self.getTableWidth(), self.rowHeight * self.getRowsNumber())
        self.Rectangle = newRectangle


class TableModel:
    def __init__(self):
        self.tables = []
        self.tableNumber = 1

    def addTable(self, position, width=100, rowsHeight=20, rowsNumber=5):
        CreatedTable = Table(position.x(), position.y(), width, rowsHeight, rowsNumber, self.tableNumber)
        self.tables.append(CreatedTable)
        self.tableNumber += 1

    def addSelectedTable(self, SelectedTable):
        self.tables.append(SelectedTable)

    def clearTables(self):
        self.tables.clear()

    def getTables(self):
        return self.tables

    def deleteSelectedTable(self, SelectedTable):
        self.tables.remove(SelectedTable)

    def getTableFromPosition(self, position):
        for ObtainedTable in self.tables:
            if ObtainedTable.contains(QPoint(position.x(), position.y())):
                return ObtainedTable
        return None
