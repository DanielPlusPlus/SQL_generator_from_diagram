from app.models.TableColumnsModel import TableColumnsModel

from copy import deepcopy


class EditTableDialogController:
    def __init__(self, EditTableDialogView, ObtainedTable):
        self.EditTableDialogView = EditTableDialogView
        self.ObtainedTable = ObtainedTable
        ObtainedTableColumnsModel = ObtainedTable.getTableColumnsModel()
        originalColumns = ObtainedTableColumnsModel.getColumns()
        copiedColumns = deepcopy(originalColumns)
        self.TempTableColumnsModel = TableColumnsModel(copiedColumns)
        self.isEditColumnSelected = False

        self.EditTableDialogView.tableView.setModel(self.TempTableColumnsModel)

        self.EditTableDialogView.addColumnButton.clicked.connect(self.selectAddColumn)
        self.EditTableDialogView.deleteColumnButton.clicked.connect(self.selectDeleteColumn)
        self.EditTableDialogView.editColumnButton.clicked.connect(self.selectEditColumn)
        self.EditTableDialogView.cancelButton.clicked.connect(self.selectCancel)
        self.EditTableDialogView.okButton.clicked.connect(self.selectOK)

    def selectAddColumn(self):
        columnName = self.EditTableDialogView.columnNameLineEdit.text()
        dataType = self.EditTableDialogView.dataTypeComboBox.currentText()
        length = self.EditTableDialogView.lengthSpinBox.value()

        self.TempTableColumnsModel.addColumn(dataType, length, columnName)

        self.EditTableDialogView.columnNameLineEdit.clear()
        self.EditTableDialogView.dataTypeComboBox.setCurrentIndex(0)
        self.EditTableDialogView.lengthSpinBox.setValue(0)

    def selectDeleteColumn(self):
        selectedRows = self.EditTableDialogView.tableView.selectionModel().selectedRows()
        if selectedRows:
            selectedRowNumber = selectedRows[0].row()
            self.TempTableColumnsModel.deleteColumn(selectedRowNumber)

    def selectEditColumn(self):
        self.isEditColumnSelected = True
        print("Edit column")

    def unselectEditColumn(self):
        self.isEditColumnSelected = False

    def getSelectEditColumnStatus(self):
        return self.isEditColumnSelected

    def selectCancel(self):
        self.EditTableDialogView.reject()

    def selectOK(self):
        self.editTableName()
        self.editTableColumns()
        self.editTableDimensions()
        self.EditTableDialogView.accept()

    def editTableName(self):
        newName = self.EditTableDialogView.tableNameLineEdit.text()
        self.ObtainedTable.editTableName(newName)

    def editTableColumns(self):
        self.ObtainedTable.changeTableColumnsModel(self.TempTableColumnsModel)

    def editTableDimensions(self):
        self.ObtainedTable.changeTableDimensions()
