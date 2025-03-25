from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize


class ToolBarView(QToolBar):
    def __init__(self, MainWindow):
        super().__init__("Tools", MainWindow)
        self.setIconSize(QSize(32, 32))
        self.setupUI()

    def setupUI(self):
        self.actionCreateTable = QAction(QIcon("app\\icons\\table.png"), "Create table", self)
        self.addAction(self.actionCreateTable)

        self.actionCreate_1_1_Rel = QAction(QIcon("app\\icons\\1_1.png"), "Create 1:1 relationship", self)
        self.addAction(self.actionCreate_1_1_Rel)

        self.actionCreate_1_n_Rel = QAction(QIcon("app\\icons\\1_n.png"), "Create 1:n relationship", self)
        self.addAction(self.actionCreate_1_n_Rel)

        self.actionCreate_n_n_Rel = QAction(QIcon("app\\icons\\n_n.png"), "Create n:n relationship", self)
        self.addAction(self.actionCreate_n_n_Rel)

        self.actionSaveDiagram = QAction(QIcon("app\\icons\\saveDiagram.png"), "Save diagram", self)
        self.addAction(self.actionSaveDiagram)

        self.actionGenerateSQL = QAction(QIcon("app\\icons\\generateSQL.png"), "Generate SQL code", self)
        self.addAction(self.actionGenerateSQL)