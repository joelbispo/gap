# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication

from infrastructure.ui_to_py import convert_ui_to_py
from views.MainView.mainview import MainWindow

if __name__ == "__main__":
    convert_ui_to_py()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
