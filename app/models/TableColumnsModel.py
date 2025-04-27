from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


class TableColumnsModel(QAbstractTableModel):
    def __init__(self, columns=None):
        super().__init__()
        self.columns = columns or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.columns)

    def columnCount(self, parent=QModelIndex):
        return 7

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()
        column = index.column()

        if role in (Qt.DisplayRole, Qt.EditRole):
            if column == 0:
                return self.columns[row]["columnName"]
            elif column == 1:
                return self.columns[row]["dataType"]
            elif column == 2:
                return self.columns[row]["length"]
            elif column in (3, 4, 5, 6):
                return ""

        if role == Qt.CheckStateRole:
            if column == 3:
                return Qt.Checked if self.columns[row]["unique"] else Qt.Unchecked
            elif column == 4:
                return Qt.Checked if self.columns[row]["notNull"] else Qt.Unchecked
            elif column == 5:
                return Qt.Checked if self.columns[row]["pk"] else Qt.Unchecked
            elif column == 6:
                return Qt.Unchecked

        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        if index.column() in (0, 1, 2):
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        if index.column() in (3, 4, 5):
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable
        if index.column() == 6:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled

        return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return None

        row = index.row()
        column = index.column()

        if role == Qt.EditRole:
            if column == 0:
                self.columns[row]["columnName"] = value
            elif column == 1:
                self.columns[row]["dataType"] = value
            elif column == 2:
                self.columns[row]["length"] = value
            self.dataChanged.emit(index, index)
            return True

        if role == Qt.CheckStateRole:
            value = Qt.CheckState(value)
            if column == 3:
                self.columns[row]["unique"] = (value == Qt.Checked)
            elif column == 4:
                self.columns[row]["notNull"] = (value == Qt.Checked)
            elif column == 5:
                self.columns[row]["pk"] = (value == Qt.Checked)
            elif column == 6:
                pass
            self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole, Qt.CheckStateRole])
            return True

        return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            headers = ["Column Name", "Type", "Length", "UNIQUE", "NOT NULL", "PK", "FK"]
            return headers[section]

        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return str(section + 1)

        return None

    def addColumn(self, dataType, length, columnName="Empty Name"):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.columns.append({"columnName": columnName, "dataType": dataType, "length": length, "unique": False,
                             "notNull": False, "pk": False, "fk": False})
        self.endInsertRows()

    def deleteColumn(self, row):
        if 0 <= row < self.rowCount():
            self.beginRemoveRows(QModelIndex(), row, row)
            del self.columns[row]
            self.endRemoveRows()

    def getColumns(self):
        return self.columns
