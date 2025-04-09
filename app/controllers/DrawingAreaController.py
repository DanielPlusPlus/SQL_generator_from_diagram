from PySide6.QtCore import Qt, QPoint

from app.enums.TableContextMenuEnum import TableContextMenuEnum


class DrawingAreaController:
    def __init__(self):
        self.DrawingAreaView = None
        self.cursorPosition = QPoint()
        self.MainWindowController = None
        self.ToolBarController = None
        self.TableController = None

    def setDrawingAreaView(self, DrawingAreaView):
        self.DrawingAreaView = DrawingAreaView

    def setMainWindowController(self, MainWindowController):
        self.MainWindowController = MainWindowController

    def setToolBarController(self, ToolBarController):
        self.ToolBarController = ToolBarController

    def setTableController(self, TableController):
        self.TableController = TableController

    def handleMouseMove(self, event):
        self.cursorPosition = event.position().toPoint()
        self.MainWindowController.updateStatusBarInView(self.cursorPosition)

    def handleMousePress(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.ToolBarController.getCreateTableToolStatus():
                self.TableController.addTable(self.cursorPosition)
            elif self.TableController.getTableInMotionStatus():
                self.TableController.unselectTableInMotion(self.cursorPosition)
            elif self.TableController.getContextMenuAtWorkStatus():
                self.TableController.unselectContextMenuAtWork()
            else:
                self.TableController.selectTableInMotion(self.cursorPosition)
        elif event.button() == Qt.MouseButton.RightButton:
            if self.ToolBarController.getCreateTableToolStatus():
                pass  # miejsce na anulowanie rysowania
            else:
                globalCursorPosition = self.DrawingAreaView.convertCursorPositionToGlobal(self.cursorPosition)
                result = self.TableController.displayTableContextMenu(self.cursorPosition, globalCursorPosition)
                if result == TableContextMenuEnum.EDIT:
                    self.TableController.editTable(self.cursorPosition)
                elif result == TableContextMenuEnum.DELETE:
                    self.TableController.deleteTable(self.cursorPosition)

    def handleMouseRelease(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.ToolBarController.getCreateTableToolStatus():
                self.ToolBarController.unselectCreateTableTool()

    def handlePaintEvent(self):
        if self.ToolBarController.getCreateTableToolStatus():
            self.TableController.selectDrawTempTable(self.cursorPosition)
        elif self.TableController.getTableInMotionStatus():
            self.TableController.selectDrawTempTable(self.cursorPosition)
        self.TableController.selectDrawTable()
