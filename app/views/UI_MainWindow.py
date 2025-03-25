from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QMenuBar,  QStatusBar, QWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")

        self.gridLayout.addLayout(self.horizontalLayout_1, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.drawingArea = QWidget(self.centralwidget)
        self.drawingArea.setObjectName(u"drawingArea")

        self.horizontalLayout_2.addWidget(self.drawingArea)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SQL generator from diagram", None))

