class EditTableDialogController:
    def __init__(self, EditTableDialogView, ObtainedTable):
        self.EditTableDialogView = EditTableDialogView
        self.ObtainedTable = ObtainedTable
        self.TableColumnsModel = ObtainedTable.getTableColumnsModel()
        self.originalColumns = self.TableColumnsModel.getOriginalColumns()
        self.copiedColumns = self.TableColumnsModel.getCopiedColumns()
        self.TableColumnsModel.changeColumns(self.copiedColumns)
        self.isEditColumnSelected = False

        self.EditTableDialogView.addColumnButton.clicked.connect(self.selectAddColumn)
        self.EditTableDialogView.deleteColumnButton.clicked.connect(self.selectDeleteColumn)
        self.EditTableDialogView.editColumnButton.clicked.connect(self.selectEditColumn)
        self.EditTableDialogView.cancelButton.clicked.connect(self.selectCancel)
        self.EditTableDialogView.okButton.clicked.connect(self.selectOK)

    def selectAddColumn(self):
        columnName = self.EditTableDialogView.columnNameLineEdit.text()
        dataType = self.EditTableDialogView.dataTypeComboBox.currentText()
        length = self.EditTableDialogView.lengthSpinBox.value()

        self.TableColumnsModel.addColumn(columnName, dataType, length)

        self.EditTableDialogView.columnNameLineEdit.clear()
        self.EditTableDialogView.dataTypeComboBox.setCurrentIndex(0)
        self.EditTableDialogView.lengthSpinBox.setValue(0)

    def selectDeleteColumn(self):
        print("Delete column")

    def selectEditColumn(self):
        self.isEditColumnSelected = True
        print("Edit column")

    def unselectEditColumn(self):
        self.isEditColumnSelected = False

    def getSelectEditColumnStatus(self):
        return self.isEditColumnSelected

    def selectCancel(self):
        self.restoreOriginalTableColumns()
        self.EditTableDialogView.reject()

    def selectOK(self):
        self.editTableName()
        self.EditTableDialogView.accept()

    def editTableName(self):
        newName = self.EditTableDialogView.tableNameLineEdit.text()
        self.ObtainedTable.editTableName(newName)

    def restoreOriginalTableColumns(self):
        self.TableColumnsModel.changeColumns(self.originalColumns)
