from app.views.ConfirmationDialogView import ConfirmationDialogView


class TableController:
    def __init__(self, ParentWindow, TableView, TableModel):
        self.ParentWindow = ParentWindow
        self.TableView = TableView
        self.TableModel = TableModel
        self.TempTable = None
        self.isTableInMotion = False

    def addTable(self, cursorPosition):
        self.TableModel.addTable(cursorPosition)

    def deleteTable(self, cursorPosition):
        ObtainedTable = self.TableModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            dialogTitle = "WARNING"
            dialogText = "Are you about deleting this table?"
            ConfirmationDialog = ConfirmationDialogView(self.ParentWindow, dialogTitle, dialogText)
            if ConfirmationDialog.displayDialog():
                self.TableModel.deleteSelectedTable(ObtainedTable)

    def displayTable(self, cursorPosition):
        ObtainedTable = self.TableModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            print(ObtainedTable.getTableNumber())

    def selectTableInMotion(self, cursorPosition):
        self.TempTable = self.TableModel.getTableFromPosition(cursorPosition)
        self.TableModel.deleteSelectedTable(self.TempTable)
        self.isTableInMotion = True

    def unselectTableInMotion(self, cursorPosition):
        self.TempTable.changeTablePosition(cursorPosition.x(), cursorPosition.y())
        self.TableModel.addSelectedTable(self.TempTable)
        self.isTableInMotion = False
        self.TempTable = None

    def selectDrawTempTable(self, position):
        self.TableView.drawTempTable(position)

    def selectDrawTable(self):
        self.TableView.drawTables()

    def getTableInMotionStatus(self):
        return self.isTableInMotion


