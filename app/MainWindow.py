from PySide6.QtWidgets import QMainWindow, QToolBar
from app.AppMainWindow import Ui_MainWindow
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createToolBar()

    def createToolBar(self):
        self.toolBar = QToolBar("Tools")
        self.toolBar.setIconSize(QSize(32, 32))
        self.addToolBar(self.toolBar)

        self.actionCreateTable = QAction(QIcon("app\\icons\\table.png"), "Create table", self)
        self.toolBar.addAction(self.actionCreateTable)
        self.actionCreateTable.triggered.connect(self.selectCreateTableTool)

        self.actionCreate_1_1_Rel = QAction(QIcon("app\\icons\\1_1.png"), "Create 1:1 relationship", self)
        self.toolBar.addAction(self.actionCreate_1_1_Rel)
        self.actionCreate_1_1_Rel.triggered.connect(self.selectCreate_1_1_Rel)

        self.actionCreate_1_n_Rel = QAction(QIcon("app\\icons\\1_n.png"), "Create 1:n relationship", self)
        self.toolBar.addAction(self.actionCreate_1_n_Rel)
        self.actionCreate_1_n_Rel.triggered.connect(self.selectCreate_1_n_Rel)

        self.actionCreate_n_n_Rel = QAction(QIcon("app\\icons\\n_n.png"), "Create n:n relationship", self)
        self.toolBar.addAction(self.actionCreate_n_n_Rel)
        self.actionCreate_n_n_Rel.triggered.connect(self.selectCreate_n_n_Rel)

        self.actionSaveDiagram = QAction(QIcon("app\\icons\\saveDiagram.png"), "Save diagram", self)
        self.toolBar.addAction(self.actionSaveDiagram)
        self.actionSaveDiagram.triggered.connect(self.selectSaveDiagram)

        self.actionGenerateSQL = QAction(QIcon("app\\icons\\generateSQL.png"), "Generate SQL code", self)
        self.toolBar.addAction(self.actionGenerateSQL)
        self.actionGenerateSQL.triggered.connect(self.selectGenerateSQL)

    def selectCreateTableTool(self):
        print("Selected create table tool")

    def selectCreate_1_1_Rel(self):
        print("Selected create 1:1 relationship")

    def selectCreate_1_n_Rel(self):
        print("Selected create 1:n relationship")

    def selectCreate_n_n_Rel(self):
        print("Selected create n:n relationship")

    def selectSaveDiagram(self):
        print("Selected save diagram tool")

    def selectGenerateSQL(self):
        print("Selected generate SQL tool")

