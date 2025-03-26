from PySide6.QtWidgets import QMainWindow

from app.views.MainWindowView import MainWindowView
from app.views.ToolBarView import ToolBarView
from app.views.DrawingAreaView import DrawingAreaView
from app.controllers.MainWindowController import MainWindowController
from app.controllers.ToolBarController import ToolBarController
from app.controllers.DrawingAreaController import DrawingAreaController
from app.models.TableModel import TableModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # views
        self.MainWindowView = MainWindowView()
        self.MainWindowView.setupUi(self)

        self.ToolBarView = ToolBarView(self)
        self.ToolBarView.setupUI()
        self.addToolBar(self.ToolBarView)

        # controllers
        self.MainWindowController = MainWindowController(self.MainWindowView)
        self.ToolBarController = ToolBarController(self.ToolBarView)
        self.DrawingAreaController = DrawingAreaController()

        # models
        self.TableModel = TableModel()

        # views
        self.drawingAreaView = DrawingAreaView(self.DrawingAreaController)
        self.drawingAreaView.setupUI()
        self.MainWindowView.addCentralWidget(self.drawingAreaView)

        # controller
        self.DrawingAreaController.setView(self.drawingAreaView)
        self.DrawingAreaController.setModel(self.TableModel)
        self.DrawingAreaController.setFriendlyController(self.MainWindowController)
