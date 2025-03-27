from PySide6.QtWidgets import QMainWindow

from app.views.MainWindowView import MainWindowView
from app.views.ToolBarView import ToolBarView
from app.views.ScrollAreaView import ScrollAreaView
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
        self.ScrollAreaView = ScrollAreaView(self)
        self.DrawingAreaView = DrawingAreaView(self.DrawingAreaController)
        self.ScrollAreaView.setupUI(self.DrawingAreaView)
        self.DrawingAreaView.setupUI()
        self.MainWindowView.addCentralWidget(self.ScrollAreaView)

        # controller
        self.ToolBarController.setTableModel(self.TableModel)
        self.DrawingAreaController.setView(self.DrawingAreaView)
        self.DrawingAreaController.setModel(self.TableModel)
        self.DrawingAreaController.setFriendlyController(self.MainWindowController)

        # views
        self.DrawingAreaView.setTableModel(self.TableModel)
