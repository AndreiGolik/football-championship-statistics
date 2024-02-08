# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statistics_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHeaderView,
    QLabel, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(759, 461)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(141, 73, 112, 255), stop:0.426136 rgba(128, 73, 173, 255), stop:1 rgba(210, 76, 188, 255));")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 70, 711, 311))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.layoutWidget)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.table = QTableWidget(self.layoutWidget)
        if (self.table.columnCount() < 7):
            self.table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.table.rowCount() < 8):
            self.table.setRowCount(8)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table.setItem(3, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table.setItem(4, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table.setItem(5, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table.setItem(6, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table.setItem(7, 0, __qtablewidgetitem14)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.983136, x2:0, y2:0.0852273, stop:0.409091 rgba(255, 152, 100, 255), stop:0.801136 rgba(255, 142, 142, 255));")
        self.table.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table.setDragEnabled(False)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Statistics", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u2116", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u0430\u043d\u0434\u044b", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u0418\u0433\u0440", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0431\u0435\u0434", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"\u041d\u0438\u0447\u044c\u0438\u0445", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"\u041e\u0447\u043a\u043e\u0432", None));

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.table.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"1", None));
        ___qtablewidgetitem8 = self.table.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"2", None));
        ___qtablewidgetitem9 = self.table.item(2, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"3", None));
        ___qtablewidgetitem10 = self.table.item(3, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"4", None));
        ___qtablewidgetitem11 = self.table.item(4, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"5", None));
        ___qtablewidgetitem12 = self.table.item(5, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"6", None));
        ___qtablewidgetitem13 = self.table.item(6, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"7", None));
        ___qtablewidgetitem14 = self.table.item(7, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"8", None));
        self.table.setSortingEnabled(__sortingEnabled)

    # retranslateUi

