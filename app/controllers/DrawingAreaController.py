from PySide6.QtCore import Qt

from app.models.TableModel import TableModel
from PySide6.QtCore import QPoint


class DrawingAreaController:
    def __init__(self):
        self.DrawingAreaView = None
        self.cursorPosition = QPoint()
        self.Model = None
        self.Controller = None

    def setView(self, DrawingAreaView):
        self.DrawingAreaView = DrawingAreaView

    def setModel(self, SupportedModel):
        self.Model = SupportedModel

    def setFriendlyController(self, FriendlyController):
        self.Controller = FriendlyController

    def handleMouseMove(self, event):
        self.cursorPosition = event.position().toPoint()
        self.Controller.updateStatusBarInView(self.cursorPosition)

    def handleMousePress(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.Model = TableModel()
            self.Model.addTable(self.cursorPosition)
