from PySide6.QtCore import Qt, QPoint

from app.models.TableModel import TableModel


class DrawingAreaController:
    def __init__(self):
        self.DrawingAreaView = None
        self.cursorPosition = QPoint()
        self.MainWindowController = None
        self.TableModel = None
        self.TableController = None
        self.TableView = None

    def setDrawingAreaView(self, DrawingAreaView):
        self.DrawingAreaView = DrawingAreaView

    def setTableView(self, TableView):
        self.TableView = TableView

    def setTableModel(self, TableModelObj):
        self.TableModel = TableModelObj

    def setMainWindowController(self, MainWindowController):
        self.MainWindowController = MainWindowController

    def setTableController(self, TableController):
        self.TableController = TableController

    def handleMouseMove(self, event):
        self.cursorPosition = event.position().toPoint()
        self.MainWindowController.updateStatusBarInView(self.cursorPosition)

    def handleMousePress(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.TableModel = TableModel()
            self.TableModel.addTable(self.cursorPosition)

    def handlePaintEvent(self):
        self.TableController.selectDrawTable()
