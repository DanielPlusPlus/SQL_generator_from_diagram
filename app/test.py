"""
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QMenuBar, QScrollArea
from PySide6.QtGui import QPainter, QPen, QColor, QAction
from PySide6.QtCore import Qt, QPoint, QRect
import sys


class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.drawing = False
        self.cursor_position = QPoint()
        self.tables = []  # Lista przechowująca narysowane tabele
        self.row_height = 20  # Wysokość pojedynczego wiersza
        self.num_rows = 5  # Liczba wierszy w tabeli
        self.table_width = 100  # Szerokość tabeli
        self.setMinimumSize(800, 600)  # Minimalny rozmiar obszaru roboczego

    def mouseMoveEvent(self, event):
        self.cursor_position = event.position().toPoint()
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            table_rect = QRect(self.cursor_position.x() - self.table_width // 2,
                               self.cursor_position.y() - (self.row_height * self.num_rows) // 2,
                               self.table_width, self.row_height * self.num_rows)
            self.tables.append(table_rect)
            self.adjustCanvasSize(table_rect)
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.PenStyle.SolidLine))

        for table in self.tables:
            self.drawTable(painter, table)

        # Rysowanie podążającej tabeli
        temp_rect = QRect(self.cursor_position.x() - self.table_width // 2,
                          self.cursor_position.y() - (self.row_height * self.num_rows) // 2,
                          self.table_width, self.row_height * self.num_rows)
        self.drawTable(painter, temp_rect)

    def drawTable(self, painter, rect):
        for i in range(self.num_rows + 1):
            y = rect.top() + i * self.row_height
            painter.drawLine(rect.left(), y, rect.right(), y)
        painter.drawRect(rect)

    def adjustCanvasSize(self, rect):
        new_width = max(self.width(), rect.right() + 50)
        new_height = max(self.height(), rect.bottom() + 50)
        self.setMinimumSize(new_width, new_height)
        self.resize(new_width, new_height)


class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dynamic Paint - PySide6")
        self.setGeometry(100, 100, 800, 600)

        self.scroll_area = QScrollArea(self)
        self.canvas = PaintWidget()
        self.scroll_area.setWidget(self.canvas)
        self.scroll_area.setWidgetResizable(True)
        self.setCentralWidget(self.scroll_area)

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        if not menubar:
            menubar = QMenuBar(self)
            self.setMenuBar(menubar)

        tools_menu = menubar.addMenu("Narzędzia")

        table_action = QAction("Tabela", self)
        table_action.triggered.connect(self.selectTableTool)
        tools_menu.addAction(table_action)

        self.statusBar().showMessage("Tryb rysowania tabeli z wierszami")

    def selectTableTool(self):
        self.canvas.tables.clear()
        self.canvas.update()
        self.statusBar().showMessage("Tryb rysowania tabeli z wierszami")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaintApp()
    window.show()
    sys.exit(app.exec())
"""

"""
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QScrollArea, QMessageBox, QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QAction
from PySide6.QtCore import Qt, QPoint, QRect
import sys


class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tables = []  # Lista tabel (prostokąty + numer)
        self.row_height = 20  # Wysokość pojedynczego wiersza
        self.num_rows = 5  # Liczba wierszy w tabeli
        self.table_width = 100  # Szerokość tabeli
        self.setMinimumSize(800, 600)  # Minimalny rozmiar obszaru roboczego
        self.table_counter = 1  # Numerowanie tabel
        self.drawing_enabled = False  # 🔹 Kontrola rysowania nowej tabeli

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            clicked_pos = event.position().toPoint()

            # 🔹 Sprawdzenie, czy kliknięto istniejącą tabelę
            for table_rect, table_number in self.tables:
                if table_rect.contains(clicked_pos):
                    self.showTableDialog(table_number)
                    return  # 🔹 Jeśli kliknięto tabelę, zakończ funkcję – nie rysuj nowej!

            # 🔹 Jeśli rysowanie tabel jest włączone – narysuj nową tabelę
            if self.drawing_enabled:
                table_rect = QRect(clicked_pos.x() - self.table_width // 2,
                                   clicked_pos.y() - (self.row_height * self.num_rows) // 2,
                                   self.table_width, self.row_height * self.num_rows)

                self.tables.append((table_rect, self.table_counter))  # Dodaj tabelę z numerem
                self.table_counter += 1  # Zwiększ numer tabeli
                self.drawing_enabled = False  # 🔹 Wyłącz rysowanie po postawieniu tabeli
                self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(Qt.GlobalColor.black), 2, Qt.PenStyle.SolidLine))

        # Rysowanie wszystkich tabel
        for table_rect, table_number in self.tables:
            self.drawTable(painter, table_rect)

    def drawTable(self, painter, rect):
        for i in range(self.num_rows + 1):
            y = rect.top() + i * self.row_height
            painter.drawLine(rect.left(), y, rect.right(), y)
        painter.drawRect(rect)

    def showTableDialog(self, table_number):
        msg = QMessageBox(self)
        msg.setWindowTitle("Informacja o tabeli")
        msg.setText(f"Kliknięto tabelę nr {table_number}")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()


class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rysowanie tabel - PySide6")
        self.setGeometry(100, 100, 800, 600)

        self.scroll_area = QScrollArea(self)
        self.canvas = PaintWidget()
        self.scroll_area.setWidget(self.canvas)
        self.scroll_area.setWidgetResizable(True)
        self.setCentralWidget(self.scroll_area)

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        tools_menu = menubar.addMenu("Narzędzia")

        # Akcja rysowania tabeli
        table_action = QAction("Rysuj tabelę", self)
        table_action.triggered.connect(self.selectTableTool)
        tools_menu.addAction(table_action)

        self.statusBar().showMessage("Wybierz opcję rysowania tabeli z menu")

    def selectTableTool(self):
        self.canvas.drawing_enabled = True
        self.statusBar().showMessage("Kliknij, aby narysować tabelę")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaintApp()
    window.show()
    sys.exit(app.exec())
"""

"""
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout,
    QLineEdit, QLabel, QComboBox, QPushButton,
    QSpinBox, QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import Qt
import sys

ORACLE_TYPES = {
    "VARCHAR": True,
    "NUMBER": True,
    "DATE": False,
    "CLOB": False,
}


class ColumnEditorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edytuj Tabelę")
        self.resize(450, 300)
        self.columns = []

        layout = QVBoxLayout()

        # Formularz
        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.type_combo = QComboBox()
        self.type_combo.addItems(ORACLE_TYPES.keys())
        self.length_input = QSpinBox()
        self.length_input.setMaximum(1000)
        self.length_input.setValue(20)
        self.length_input.setEnabled(True)

        form_layout.addWidget(QLabel("Nazwa"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Typ"))
        form_layout.addWidget(self.type_combo)
        form_layout.addWidget(QLabel("Długość"))
        form_layout.addWidget(self.length_input)

        layout.addLayout(form_layout)

        self.type_combo.currentTextChanged.connect(self.on_type_changed)

        # Tabela kolumn
        self.column_table = QTableWidget(0, 2)
        self.column_table.setHorizontalHeaderLabels(["Nazwa", "Typ"])
        self.column_table.horizontalHeader().setStretchLastSection(True)
        self.column_table.setEditTriggers(QTableWidget.NoEditTriggers)  # <-- BLOKUJEMY EDYCJĘ
        layout.addWidget(self.column_table)

        # Ustawienie szerokości kolumn na 50%
        self.set_column_widths()

        # Przycisk dodania kolumny
        add_button = QPushButton("Dodaj Kolumnę")
        add_button.clicked.connect(self.add_column)
        layout.addWidget(add_button)

        # Przycisk usuwania kolumny
        remove_button = QPushButton("Usuń Zaznaczoną Kolumnę")
        remove_button.clicked.connect(self.remove_selected_column)
        layout.addWidget(remove_button)

        # Przycisk OK
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

        self.setLayout(layout)

    def on_type_changed(self, text):
        self.length_input.setEnabled(ORACLE_TYPES.get(text, False))

    def add_column(self):
        name = self.name_input.text()
        dtype = self.type_combo.currentText()
        length = self.length_input.value()

        if not name:
            return

        type_display = f"{dtype}({length})" if ORACLE_TYPES[dtype] else dtype

        row = self.column_table.rowCount()
        self.column_table.insertRow(row)

        name_item = QTableWidgetItem(name)
        type_item = QTableWidgetItem(type_display)
        name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
        type_item.setFlags(type_item.flags() & ~Qt.ItemIsEditable)

        self.column_table.setItem(row, 0, name_item)
        self.column_table.setItem(row, 1, type_item)

        self.columns.append({
            "name": name,
            "type": dtype,
            "length": length if ORACLE_TYPES[dtype] else None
        })

        self.name_input.clear()
        self.length_input.setValue(20)

    def remove_selected_column(self):
        selected_row = self.column_table.currentRow()
        if selected_row >= 0:
            self.column_table.removeRow(selected_row)
            del self.columns[selected_row]

    def get_columns(self):
        return self.columns

    def set_column_widths(self):
        # Oblicz szerokość kolumn (np. każda na 50% dostępnej szerokości)
        total_width = self.column_table.viewport().width()
        column_width = total_width // 2
        self.column_table.setColumnWidth(0, column_width)
        self.column_table.setColumnWidth(1, column_width)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = ColumnEditorDialog()
    if dialog.exec() == QDialog.Accepted:
        columns = dialog.get_columns()
        print(columns)
    sys.exit(app.exec())

"""

"""
from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QSpinBox, QTableView, QWidget)


class EditTableDialoView(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"TablEditDialog")
        Dialog.resize(800, 600)
        self.gridLayout = QGridLayout(Dialog)
        self.horizontalLayout_5 = QHBoxLayout()
        self.label_4 = QLabel(Dialog)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.spinBox = QSpinBox(Dialog)

        self.horizontalLayout_5.addWidget(self.spinBox)

        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 5)

        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.label_2 = QLabel(Dialog)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(Dialog)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 7)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.label = QLabel(Dialog)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(Dialog)

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 7)

        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.tableView = QTableView(Dialog)
        self.tableView.setFrameShape(QFrame.Shape.StyledPanel)

        self.horizontalLayout_7.addWidget(self.tableView)

        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 0, 1, 3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.label_3 = QLabel(Dialog)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.comboBox = QComboBox(Dialog)

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 5)

        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.widget_3 = QWidget(Dialog)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.widget_3)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.widget = QWidget(Dialog)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.widget)

        self.pushButton_4 = QPushButton(Dialog)

        self.horizontalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(Dialog)

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 0, 1, 3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.pushButton = QPushButton(Dialog)

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Dialog)

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Dialog)

        self.horizontalLayout_8.addWidget(self.pushButton_3)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)

        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 3)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 6)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Length", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Table Name", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Column Name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Data type", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Add Column", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Delete Selected Column", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Edit Selected Column", None))
"""


"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox, QDialog, QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox, QTableView, QWidget
)


class EditTableDialogView(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("TablEditDialog")
        self.resize(800, 600)
        self.setWindowTitle("Dialog")

        self.gridLayout = QGridLayout(self)

        # Table Name
        self.horizontalLayout = QHBoxLayout()
        self.label_2 = QLabel("Table Name", self)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit = QLineEdit(self)
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 7)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        # Placeholder widget


        # Column Name
        self.horizontalLayout_3 = QHBoxLayout()
        self.label = QLabel("Column Name", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2 = QLineEdit(self)
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 7)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        # Data Type
        self.horizontalLayout_4 = QHBoxLayout()
        self.label_3 = QLabel("Data type", self)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox = QComboBox(self)
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        # Length
        self.horizontalLayout_5 = QHBoxLayout()
        self.label_4 = QLabel("Length", self)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox = QSpinBox(self)
        self.horizontalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_5.addWidget(self.spinBox)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 5)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)

        # Table View
        self.horizontalLayout_7 = QHBoxLayout()
        self.tableView = QTableView(self)
        self.tableView.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout_7.addWidget(self.tableView)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 0, 1, 3)

        # Column Action Buttons
        self.horizontalLayout_8 = QHBoxLayout()
        self.pushButton = QPushButton("Add Column", self)
        self.pushButton_2 = QPushButton("Delete Selected Column", self)
        self.pushButton_3 = QPushButton("Edit Selected Column", self)
        self.horizontalLayout_8.addWidget(self.pushButton)
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        self.horizontalLayout_8.addWidget(self.pushButton_3)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 3)

        # OK/Cancel Buttons
        self.horizontalLayout_9 = QHBoxLayout()
        self.widget = QWidget(self)
        self.horizontalLayout_9.addWidget(self.widget)
        self.widget2 = QWidget(self)
        self.horizontalLayout_9.addWidget(self.widget2)
        self.pushButton_4 = QPushButton("Cancel", self)
        self.pushButton_5 = QPushButton("OK", self)
        
        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.addWidget(self.pushButton_4)
        self.horizontalLayout_90.addWidget(self.pushButton_5)
        self.horizontalLayout_90.setStretch(0, 1)
        self.horizontalLayout_90.setStretch(1, 1)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_90)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 0, 1, 3)

        # Stretch settings
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 6)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 2)

        self.setModal(True)
"""
"""
from PySide6.QtCore import Qt
import sys

ORACLE_TYPES = {
    "VARCHAR": True,
    "NUMBER": True,
    "DATE": False,
    "CLOB": False,
}


class ColumnEditorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edytuj Tabelę")
        self.resize(450, 300)
        self.columns = []

        layout = QVBoxLayout()

        # Formularz
        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.type_combo = QComboBox()
        self.type_combo.addItems(ORACLE_TYPES.keys())
        self.length_input = QSpinBox()
        self.length_input.setMaximum(1000)
        self.length_input.setValue(20)
        self.length_input.setEnabled(True)

        form_layout.addWidget(QLabel("Nazwa"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Typ"))
        form_layout.addWidget(self.type_combo)
        form_layout.addWidget(QLabel("Długość"))
        form_layout.addWidget(self.length_input)

        layout.addLayout(form_layout)

        self.type_combo.currentTextChanged.connect(self.on_type_changed)

        # Tabela kolumn
        self.column_table = QTableWidget(0, 2)
        self.column_table.setHorizontalHeaderLabels(["Nazwa", "Typ"])
        self.column_table.horizontalHeader().setStretchLastSection(True)
        self.column_table.setEditTriggers(QTableWidget.NoEditTriggers)  # <-- BLOKUJEMY EDYCJĘ
        layout.addWidget(self.column_table)

        # Ustawienie szerokości kolumn na 50%
        self.set_column_widths()

        # Przycisk dodania kolumny
        add_button = QPushButton("Dodaj Kolumnę")
        add_button.clicked.connect(self.add_column)
        layout.addWidget(add_button)

        # Przycisk usuwania kolumny
        remove_button = QPushButton("Usuń Zaznaczoną Kolumnę")
        remove_button.clicked.connect(self.remove_selected_column)
        layout.addWidget(remove_button)

        # Przycisk OK
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

        self.setLayout(layout)

    def on_type_changed(self, text):
        self.length_input.setEnabled(ORACLE_TYPES.get(text, False))

    def add_column(self):
        name = self.name_input.text()
        dtype = self.type_combo.currentText()
        length = self.length_input.value()

        if not name:
            return

        type_display = f"{dtype}({length})" if ORACLE_TYPES[dtype] else dtype

        row = self.column_table.rowCount()
        self.column_table.insertRow(row)

        name_item = QTableWidgetItem(name)
        type_item = QTableWidgetItem(type_display)
        name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
        type_item.setFlags(type_item.flags() & ~Qt.ItemIsEditable)

        self.column_table.setItem(row, 0, name_item)
        self.column_table.setItem(row, 1, type_item)

        self.columns.append({
            "name": name,
            "type": dtype,
            "length": length if ORACLE_TYPES[dtype] else None
        })

        self.name_input.clear()
        self.length_input.setValue(20)

    def remove_selected_column(self):
        selected_row = self.column_table.currentRow()
        if selected_row >= 0:
            self.column_table.removeRow(selected_row)
            del self.columns[selected_row]

    def get_columns(self):
        return self.columns

    def set_column_widths(self):
        # Oblicz szerokość kolumn (np. każda na 50% dostępnej szerokości)
        total_width = self.column_table.viewport().width()
        column_width = total_width // 2
        self.column_table.setColumnWidth(0, column_width)
        self.column_table.setColumnWidth(1, column_width)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = ColumnEditorDialog()
    if dialog.exec() == QDialog.Accepted:
        columns = dialog.get_columns()
        print(columns)
    sys.exit(app.exec())
"""