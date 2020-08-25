from PySide2.QtWidgets import QMainWindow

from controller.login_controller import LoginController
from model.user import user_logged
from views.AdminAreaView.AdminAreaView import AdminAreaView
from views.MainView.ui_mainview import Ui_MainWindow
from model import user

HOME_INDEX = 0
LOGIN_INDEX = 1
ADMIN_AREA_INDEX = 2


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.swMain.setCurrentIndex(HOME_INDEX)
        self._set_connects()

    def _set_connects(self):
        self.ui.btnResearcher.clicked.connect(self._click_researcher)
        self.ui.btnLogin.clicked.connect(self._click_login)

    def _click_researcher(self):
        self.ui.swMain.setCurrentIndex(LOGIN_INDEX)

    def _click_login(self):
        self.ui.lError.setText("")
        login_controller = LoginController()
        success, message = login_controller.login(self.ui.leEmail.text(), self.ui.lePassword.text())

        if not success:
            self.ui.lError.setText(message)
        else:
            admin_area = AdminAreaView()
            self.ui.swMain.insertWidget(ADMIN_AREA_INDEX, admin_area)
            self.ui.swMain.setCurrentIndex(ADMIN_AREA_INDEX)
            self.ui.lUser.setText(user_logged.email)

    def _le_email_connect(self):
        self.ui.leEmail.setText("")

