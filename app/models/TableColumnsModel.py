from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


class TableColumnsModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.columns = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.columns)

    def columnCount(self, parent=QModelIndex):
        return 6

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        column = index.column()

        if role in (Qt.DisplayRole, Qt.EditRole):
            if column == 0:
                return self.columns[row]["name"]
            elif column == 1:
                return self.columns[row]["type"]
            elif column == 2:
                return ""
            elif column == 3:
                return ""
            elif column == 4:
                return ""
            elif column == 5:
                return ""

        if role == Qt.CheckStateRole and column == 2:
            return Qt.Checked if self.columns[row]["uq"] else Qt.Unchecked
        elif role == Qt.CheckStateRole and column == 3:
            return Qt.Checked if self.columns[row]["uq"] else Qt.Unchecked
        elif role == Qt.CheckStateRole and column == 3:
            return Qt.Checked if self.columns[row]["notnull"] else Qt.Unchecked
        elif role == Qt.CheckStateRole and column == 4:
            return Qt.Checked if self.columns[row]["pk"] else Qt.Unchecked
        elif role == Qt.CheckStateRole and column == 5:
            return Qt.Checked if self.columns[row]["fk"] else Qt.Unchecked

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            headers = ["Column Name", "Type", "UNIQUE", "NOT NULL", "PK", "FK"]
            return headers[section]

        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return str(section + 1)

        return None
