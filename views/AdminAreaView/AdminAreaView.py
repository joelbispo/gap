from PySide2.QtWidgets import QWidget

from views.AdminAreaView.ui_AdminAreaView import Ui_AdminAreaView


class AdminAreaView(QWidget):
    def __init__(self):
        super(AdminAreaView, self).__init__()
        self.ui = Ui_AdminAreaView()
        self.ui.setupUi(self)