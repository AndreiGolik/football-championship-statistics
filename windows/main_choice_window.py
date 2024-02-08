# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_choice_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1014, 611)
        self.main = QWidget(MainWindow)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.034, y1:0.0456364, x2:1, y2:1, stop:0.409091 rgba(255, 130, 67, 255), stop:0.704545 rgba(255, 168, 168, 255));\n"
"font-family: Consolas")
        self.widget = QWidget(self.main)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(210, 100, 591, 371))
        self.choice_table = QVBoxLayout(self.widget)
        self.choice_table.setObjectName(u"choice_table")
        self.choice_table.setContentsMargins(0, 0, 0, 0)
        self.label_choice = QLabel(self.widget)
        self.label_choice.setObjectName(u"label_choice")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        self.label_choice.setFont(font)
        self.label_choice.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.983136, x2:0, y2:0.0852273, stop:0.409091 rgba(255, 152, 100, 255), stop:0.801136 rgba(255, 142, 142, 255))")
        self.label_choice.setAlignment(Qt.AlignCenter)

        self.choice_table.addWidget(self.label_choice)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rus_button = QPushButton(self.widget)
        self.rus_button.setObjectName(u"rus_button")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setBold(True)
        self.rus_button.setFont(font1)

        self.horizontalLayout.addWidget(self.rus_button)

        self.fnl_button = QPushButton(self.widget)
        self.fnl_button.setObjectName(u"fnl_button")
        self.fnl_button.setFont(font1)

        self.horizontalLayout.addWidget(self.fnl_button)

        self.eng_button = QPushButton(self.widget)
        self.eng_button.setObjectName(u"eng_button")
        self.eng_button.setFont(font1)

        self.horizontalLayout.addWidget(self.eng_button)


        self.choice_table.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ger_button = QPushButton(self.widget)
        self.ger_button.setObjectName(u"ger_button")
        self.ger_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.ger_button)

        self.spain_button = QPushButton(self.widget)
        self.spain_button.setObjectName(u"spain_button")
        self.spain_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.spain_button)

        self.italy_button = QPushButton(self.widget)
        self.italy_button.setObjectName(u"italy_button")
        self.italy_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.italy_button)


        self.choice_table.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.france_button = QPushButton(self.widget)
        self.france_button.setObjectName(u"france_button")
        self.france_button.setFont(font1)

        self.horizontalLayout_3.addWidget(self.france_button)

        self.turk_button = QPushButton(self.widget)
        self.turk_button.setObjectName(u"turk_button")
        self.turk_button.setFont(font1)

        self.horizontalLayout_3.addWidget(self.turk_button)

        self.port_button = QPushButton(self.widget)
        self.port_button.setObjectName(u"port_button")
        self.port_button.setFont(font1)

        self.horizontalLayout_3.addWidget(self.port_button)


        self.choice_table.addLayout(self.horizontalLayout_3)

        self.nether_button = QPushButton(self.widget)
        self.nether_button.setObjectName(u"nether_button")
        self.nether_button.setFont(font1)

        self.choice_table.addWidget(self.nether_button)

        MainWindow.setCentralWidget(self.main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tabel Football Championship", None))
        self.label_choice.setText(QCoreApplication.translate("MainWindow", u"What championship do you want to watch?", None))
        self.rus_button.setText(QCoreApplication.translate("MainWindow", u"Russia", None))
        self.fnl_button.setText(QCoreApplication.translate("MainWindow", u"FNL", None))
        self.eng_button.setText(QCoreApplication.translate("MainWindow", u"England", None))
        self.ger_button.setText(QCoreApplication.translate("MainWindow", u"Germany", None))
        self.spain_button.setText(QCoreApplication.translate("MainWindow", u"Spain", None))
        self.italy_button.setText(QCoreApplication.translate("MainWindow", u"Italy", None))
        self.france_button.setText(QCoreApplication.translate("MainWindow", u"France", None))
        self.turk_button.setText(QCoreApplication.translate("MainWindow", u"Turkey", None))
        self.port_button.setText(QCoreApplication.translate("MainWindow", u"Portugal", None))
        self.nether_button.setText(QCoreApplication.translate("MainWindow", u"Netherlands", None))
    # retranslateUi

