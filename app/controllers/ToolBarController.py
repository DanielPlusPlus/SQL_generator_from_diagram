class ToolBarController:
    def __init__(self, ToolBarView):
        self.TableModel = None
        self.isTableSelected = False
        ToolBarView.actionCreateTable.triggered.connect(self.selectCreateTableTool)
        ToolBarView.actionCreate_1_1_Rel.triggered.connect(self.selectCreate_1_1_Rel)
        ToolBarView.actionCreate_1_n_Rel.triggered.connect(self.selectCreate_1_n_Rel)
        ToolBarView.actionCreate_n_n_Rel.triggered.connect(self.selectCreate_n_n_Rel)
        ToolBarView.actionSaveDiagram.triggered.connect(self.selectSaveDiagram)
        ToolBarView.actionGenerateSQL.triggered.connect(self.selectGenerateSQL)
        # trzeba stworzyc anulowanie akcji

    def setTableModel(self, TableModel):
        self.TableModel = TableModel

    def selectCreateTableTool(self):
        self.isTableSelected = True

    def unselectCreateTableTool(self):
        self.isTableSelected = False

    def getCreateTableToolStatus(self):
        return self.isTableSelected

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
