from PySide6.QtWidgets import QMainWindow

from app.views.ToolBarView import ToolBarView
from app.views.UI_MainWindow import Ui_MainWindow
from app.controllers.ToolBarController import ToolBarController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindowView = Ui_MainWindow()
        self.MainWindowView.setupUi(self)

        self.ToolBarView = ToolBarView(self)
        self.addToolBar(self.ToolBarView)
        self.ToolBarController = ToolBarController(self.ToolBarView)
