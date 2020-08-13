import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from views.MainView.ui_mainview import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.swMain.setCurrentIndex(0)
        self._set_connects()

    def _set_connects(self):
        self.ui.btnResearcher.clicked.connect(self._click_researcher)

    def _click_researcher(self):
        self.ui.swMain.setCurrentIndex(1)

    def _le_email_connect(self):
        self.ui.leEmail.setText("")

