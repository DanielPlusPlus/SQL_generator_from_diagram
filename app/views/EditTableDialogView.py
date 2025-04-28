from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QComboBox, QDialog, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSpinBox, QTableView, QWidget, QHeaderView)

from app.views.delegates.ComboBoxDelegate import ComboBoxDelegate


class EditTableDialogView(QDialog):
    def __init__(self, ParentWindow, ObtainedTable):
        super().__init__(ParentWindow)
        self.ObtainedTable = ObtainedTable
        self.dataTypes = ["NUMBER", "FLOAT", "CHAR", "VARCHAR2", "NCHAR", "NVARCHAR2", "DATE", "CLOB", "BLOB"]

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"EditTableDialog")
        self.resize(600, 400)
        self.setWindowTitle(u"Edit Table")

        self.gridLayout = QGridLayout(self)

        self.horizontalLayout = QHBoxLayout()
        self.tableNameLabel = QLabel(u"Table Name", self)
        self.tableNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tableNameLineEdit = QLineEdit(self)
        self.tableNameLineEdit.setMaxLength(30)
        self.tableNameLineEdit.setText(self.ObtainedTable.getTableName())
        self.horizontalLayout.addWidget(self.tableNameLabel)
        self.horizontalLayout.addWidget(self.tableNameLineEdit)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 7)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.addStretch()
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.columnNameLabel = QLabel(u"Column Name", self)
        self.columnNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.columnNameLineEdit = QLineEdit(self)
        self.columnNameLineEdit.setMaxLength(30)
        self.horizontalLayout_3.addWidget(self.columnNameLabel)
        self.horizontalLayout_3.addWidget(self.columnNameLineEdit)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 7)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.dataTypeLabel = QLabel(u"Data type", self)
        self.dataTypeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dataTypeComboBox = QComboBox(self)
        self.dataTypeComboBox.addItems(self.dataTypes)
        self.horizontalLayout_4.addWidget(self.dataTypeLabel)
        self.horizontalLayout_4.addWidget(self.dataTypeComboBox)
        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.lengthLabel = QLabel(u"Length", self)
        self.lengthLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lengthSpinBox = QSpinBox(self)
        self.lengthSpinBox.setRange(0, 4000)
        self.horizontalLayout_5.addWidget(self.lengthLabel)
        self.horizontalLayout_5.addWidget(self.lengthSpinBox)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 5)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.tableView = QTableView(self)
        self.tableView.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableView.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.tableView.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.tableView.setModel(self.ObtainedTable.getTableColumnsModel())
        dataTypesComboDelegate = ComboBoxDelegate(self.dataTypes, self.tableView)
        self.tableView.setItemDelegateForColumn(1, dataTypesComboDelegate)
        header = self.tableView.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignLeft)
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.horizontalLayout_7.addWidget(self.tableView)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 0, 1, 3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.addColumnButton = QPushButton(u"Add Column", self)
        self.deleteColumnButton = QPushButton(u"Delete Selected Column", self)
        self.editColumnButton = QPushButton(u"Edit Selected Column", self)
        self.horizontalLayout_8.addWidget(self.addColumnButton)
        self.horizontalLayout_8.addWidget(self.deleteColumnButton)
        self.horizontalLayout_8.addWidget(self.editColumnButton)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_12 = QHBoxLayout()
        self.pleceholderWidget = QWidget(self)
        self.cancelButton = QPushButton(u"Cancel", self)
        self.okButton = QPushButton(u"OK", self)
        self.horizontalLayout_10.addWidget(self.pleceholderWidget)
        self.horizontalLayout_11.addWidget(self.pleceholderWidget)
        self.horizontalLayout_12.addWidget(self.cancelButton)
        self.horizontalLayout_12.addWidget(self.okButton)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 1)

        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 0, 1, 3)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 6)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 2)

    def displayDialog(self):
        result = self.exec()
        return result
