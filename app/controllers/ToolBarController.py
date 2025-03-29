from PySide6.QtCore import QPoint


class ToolBarController:
    def __init__(self, ToolBarView):
        self.TableModel = None
        ToolBarView.actionCreateTable.triggered.connect(self.selectCreateTableTool)
        ToolBarView.actionCreate_1_1_Rel.triggered.connect(self.selectCreate_1_1_Rel)
        ToolBarView.actionCreate_1_n_Rel.triggered.connect(self.selectCreate_1_n_Rel)
        ToolBarView.actionCreate_n_n_Rel.triggered.connect(self.selectCreate_n_n_Rel)
        ToolBarView.actionSaveDiagram.triggered.connect(self.selectSaveDiagram)
        ToolBarView.actionGenerateSQL.triggered.connect(self.selectGenerateSQL)

    def setTableModel(self, TableModel):
        self.TableModel = TableModel
        self.position = QPoint(200, 200)

    def selectCreateTableTool(self):
        self.TableModel.addTable(self.position)

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
