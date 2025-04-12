class EditTableDialogController:
    def __init__(self, EditTableDialogView):
        self.isAddColumnSelected = False
        self.isDeleteColumnSelected = False
        self.isEditColumnSelected = False

        EditTableDialogView.addColumnButton.clicked.connect(self.selectAddColumn)
        EditTableDialogView.deleteColumnButton.clicked.connect(self.selectDeleteColumn)
        EditTableDialogView.editColumnButton.clicked.connect(self.selectEditColumn)
        EditTableDialogView.cancelButton.clicked.connect(EditTableDialogView.reject)
        EditTableDialogView.okButton.clicked.connect(EditTableDialogView.accept)

    def selectAddColumn(self):
        self.isAddColumnSelected = True
        print("Add column")

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
