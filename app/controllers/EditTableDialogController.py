class EditTableDialogController:
    def __init__(self, EditTableDialogView, ObtainedTable):
        self.EditTableDialogView = EditTableDialogView
        self.ObtainedTable = ObtainedTable
        self.isAddColumnSelected = False
        self.isDeleteColumnSelected = False
        self.isEditColumnSelected = False
        self.EditTableDialogView.addColumnButton.clicked.connect(self.selectAddColumn)
        self.EditTableDialogView.deleteColumnButton.clicked.connect(self.selectDeleteColumn)
        self.EditTableDialogView.editColumnButton.clicked.connect(self.selectEditColumn)
        self.EditTableDialogView.cancelButton.clicked.connect(self.selectCancel)
        self.EditTableDialogView.okButton.clicked.connect(self.selectOK)

    def selectAddColumn(self):
        print("Add column")
        self.isAddColumnSelected = True

    def unselectAddColumn(self):
        self.isAddColumnSelected = False

    def getSelectAddColumnStatus(self):
        return self.isAddColumnSelected

    def selectDeleteColumn(self):
        self.isDeleteColumnSelected = True
        print("Delete column")

    def unselectDeleteColumn(self):
        self.isDeleteColumnSelected = False

    def getSelectDeleteColumnStatus(self):
        return self.isDeleteColumnSelected

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
        self.EditTableDialogView.accept()

    def editTableName(self):
        newName = self.EditTableDialogView.tableNameLineEdit.text()
        self.ObtainedTable.editTableName(newName)

    # klucz główny trzeba dać możliwość zaznaczania