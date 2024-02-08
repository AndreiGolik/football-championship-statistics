import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox

from config import COUNTRY_CHAMPIONSHIP, CHAMPIONSHIP
from football_static import ChampionshipsStaticParse
from windows.main_choice_window import Ui_MainWindow
from windows.statistics_window import Ui_Dialog


class FootballStatistics(QMainWindow):
    def __init__(self):
        super(FootballStatistics, self).__init__()

        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.label_choice.setText("Выберите чемпионат!")

        self.main_ui.rus_button.clicked.connect(self.__get_statistics)
        self.main_ui.fnl_button.clicked.connect(self.__get_statistics)
        self.main_ui.eng_button.clicked.connect(self.__get_statistics)
        self.main_ui.ger_button.clicked.connect(self.__get_statistics)
        self.main_ui.spain_button.clicked.connect(self.__get_statistics)
        self.main_ui.italy_button.clicked.connect(self.__get_statistics)
        self.main_ui.france_button.clicked.connect(self.__get_statistics)
        self.main_ui.nether_button.clicked.connect(self.__get_statistics)
        self.main_ui.port_button.clicked.connect(self.__get_statistics)
        self.main_ui.turk_button.clicked.connect(self.__get_statistics)


    def __get_statistics(self):
        self.new_dialog = QtWidgets.QDialog()
        self.ui_dialog = Ui_Dialog()
        self.ui_dialog.setupUi(self.new_dialog)

        sender_text = self.sender().text()

        ChampionshipsStaticParse().run()

        title = COUNTRY_CHAMPIONSHIP[sender_text]
        self.ui_dialog.label_title.setText(title)
        result = CHAMPIONSHIP[title]

        col = -1
        for value in list(result.values()):
            col += 1
            row = 0
            for elem in value:
                self.ui_dialog.table.setItem(row, col, QTableWidgetItem(elem))
                row += 1

        self.new_dialog.show()

    def __warning_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Предупреждение")
        msg.setText("Данный раздел пока отлаживается")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FootballStatistics()
    window.show()

    sys.exit(app.exec())

