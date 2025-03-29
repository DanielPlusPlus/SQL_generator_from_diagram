from PySide6.QtCore import QRect


class Table:
    def __init__(self, x, y, width, rowHeight, rowsNumber, tableNumber):
        self.rectangle = QRect(x - width // 2, y - (rowHeight * rowsNumber) // 2, width, rowHeight * rowsNumber)
        self.rowHeight = rowHeight
        self.rowsNumber = rowsNumber
        self.tableNumber = tableNumber

    def getRectangle(self):
        return self.rectangle

    def getTop(self):
        return self.rectangle.top()

    def getLeft(self):
        return self.rectangle.left()

    def getRight(self):
        return self.rectangle.right()

    def getRowHeight(self):
        return self.rowHeight

    def getRowsNumber(self):
        return self.rowsNumber

    def getTableNumber(self):
        return self.tableNumber

    def contains(self, point):
        return self.rectangle.contains(point)


class TableModel:
    def __init__(self):
        self.tables = []
        self.tableNumber = 1

    def addTable(self, position, width=100, rowsHeight=20, rowsNumber=5):
        table = Table(position.x() - width // 2,
                      position.y() - (rowsHeight * rowsNumber) // 2,
                      width, rowsHeight * rowsNumber, rowsNumber, self.tableNumber)
        self.tables.append(table)
        self.tableNumber += 1

    def clearTables(self):
        self.tables.clear()

    def getTables(self):
        return self.tables
