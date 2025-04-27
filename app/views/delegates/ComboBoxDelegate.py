from PySide6.QtWidgets import QStyledItemDelegate, QComboBox
from PySide6.QtCore import Qt


class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, dataTypes, parent=None):
        super().__init__(parent)
        self.dataTypes = dataTypes

    def createEditor(self, parent, option, index):
        comboBox = QComboBox(parent)
        comboBox.addItems(self.dataTypes)
        return comboBox

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.EditRole)
        valueIndex = editor.findText(value)
        if valueIndex >= 0:
            editor.setCurrentIndex(valueIndex)

    def setModelData(self, editor, model, index):
        value = editor.currentText()
        model.setData(index, value, Qt.EditRole)
