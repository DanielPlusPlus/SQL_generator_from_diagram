from PySide6.QtWidgets import QDialog

from app.views.ConfirmationDialogView import ConfirmationDialogView
from app.views.TableContextMenuView import TableContextMenuView
from app.views.EditTableDialogView import EditTableDialogView
from app.controllers.TableContextMenuController import TableContextMenuController
from app.controllers.EditTableDialogController import EditTableDialogController
from app.enums.TableContextMenuEnum import TableContextMenuEnum


class TableController:
    def __init__(self, ParentWindow, TableView, TableModel):
        self.ParentWindow = ParentWindow
        self.TableView = TableView
        self.TableModel = TableModel
        self.TableContextMenuView = TableContextMenuView(self.ParentWindow)
        self.TableContextMenuView.setup_UI()
        self.TableContextMenuController = TableContextMenuController(self.TableContextMenuView)
        self.TempTable = None
        self.isTableInTransfer = False
        self.isContextMenuAtWork = False

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

    def editTable(self, cursorPosition):
        ObtainedTable = self.TableModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            EditTableDialog = EditTableDialogView(self.ParentWindow)
            EditTableDialog.setupUi()
            EditTableDialogControl = EditTableDialogController(EditTableDialog)
            result = EditTableDialog.exec()
            if result == QDialog.Accepted:
                print("OK")
            elif result == QDialog.Rejected:
                print("Cancel")

    def selectTableInTransfer(self, cursorPosition):
        self.TempTable = self.TableModel.getTableFromPosition(cursorPosition)
        if self.TempTable is not None:
            self.TableModel.deleteSelectedTable(self.TempTable)
            self.isTableInTransfer = True

    def unselectTableInTransfer(self, cursorPosition):
        self.TempTable.changeTablePosition(cursorPosition.x(), cursorPosition.y())
        self.TableModel.addSelectedTable(self.TempTable)
        self.isTableInTransfer = False
        self.TempTable = None

    def selectDrawTempTable(self, position):
        self.TableView.drawTempTable(position)

    def selectDrawTable(self):
        self.TableView.drawTables()

    def getTableInTransferStatus(self):
        return self.isTableInTransfer

    def displayTableContextMenu(self, cursorPosition, globalCursorPosition):
        ObtainedTable = self.TableModel.getTableFromPosition(cursorPosition)
        if ObtainedTable is not None:
            self.isContextMenuAtWork = True
            self.TableContextMenuView.exec(globalCursorPosition)
            if self.TableContextMenuController.getSelectEditTableStatus():
                self.TableContextMenuController.unselectEditTable()
                self.isContextMenuAtWork = False
                return TableContextMenuEnum.EDIT
            elif self.TableContextMenuController.getSelectDeleteTableStatus():
                self.TableContextMenuController.unselectDeleteTable()
                self.isContextMenuAtWork = False
                return TableContextMenuEnum.DELETE
            return TableContextMenuEnum.NONE

    def unselectContextMenuAtWork(self):
        self.isContextMenuAtWork = False

    def getContextMenuAtWorkStatus(self):
        return self.isContextMenuAtWork
