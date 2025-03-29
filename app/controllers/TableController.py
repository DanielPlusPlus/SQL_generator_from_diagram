class TableController:
    def __init__(self, TableView):
        self.TableView = TableView

    def selectDrawTable(self):
        self.TableView.drawTables()