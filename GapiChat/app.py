from app.auth import login
from app import MainWindow
from PyQt5 import QtWidgets
import sys
import app.resources.resources


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = login.AuthLogin()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())