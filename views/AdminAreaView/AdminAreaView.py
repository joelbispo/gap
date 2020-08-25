from PySide2.QtWidgets import QWidget, QTableWidgetItem

from infrastructure.firebase_sdka_admin import db
from model.user import user_logged
from views.AdminAreaView.ui_AdminAreaView import Ui_AdminAreaView

COL_NAME = 0
COL_NUMBER = 1

class AdminAreaView(QWidget):
    def __init__(self):
        super(AdminAreaView, self).__init__()
        self.ui = Ui_AdminAreaView()
        self.ui.setupUi(self)
        self.load_table_experiment()

    def load_experiments(self):
        docs = db.collection('experiments').where('researcher', '==', user_logged.email).stream()
        return [doc.to_dict() for doc in docs]

    def load_table_experiment(self):
        experiments = self.load_experiments()
        for experiment in experiments:
            current_row = self.ui.tbExperiment.rowCount()
            self.ui.tbExperiment.insertRow(current_row)
            item_name = QTableWidgetItem()
            item_name.setText(experiment['name'])
            self.ui.tbExperiment.setItem(current_row-1, COL_NAME, item_name)

            item_number = QTableWidgetItem()
            item_number.setText(str(experiment['numberParticipants']))
            self.ui.tbExperiment.setItem(current_row-1, COL_NUMBER, item_number)


