from PySide6.QtCore import QRect


class TableModel:
    def __init__(self):
        self.tables = []

    def addTable(self, position, width=100, row_height=20, num_rows=5):
        tableRect = QRect(position.x() - width // 2,
                          position.y() - (row_height * num_rows) // 2,
                          width, row_height * num_rows)
        self.tables.append(tableRect)

    def clearTables(self):
        self.tables.clear()
