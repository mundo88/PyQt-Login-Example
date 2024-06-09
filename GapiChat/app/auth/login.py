from PyQt5 import QtWidgets
from ..ui.auth import auth

class AuthLogin(QtWidgets.QDialog):
    def __init__(self):
        super(AuthLogin, self).__init__() # Call the inherited classes __init__ method
        self.ui = auth.Ui_AuthScreen()
        self.ui.setupUi(self)
        self.ui.show_hide_pw.clicked.connect(self.show_hide_pw)
        self.ui.login_btn.clicked.connect(self.handleLogin)

        self.hidePW = True
    def show_hide_pw(self):
        if self.hidePW:
            self.ui.show_hide_pw.setStyleSheet("border-image: url(:/image/image/hide.png);width:24px;height:24px;margin-right:16px;")
            self.hidePW = False
            self.ui.pw_input.setEchoMode(QtWidgets.QLineEdit.Normal)
            return
        self.ui.show_hide_pw.setStyleSheet("border-image: url(:/image/image/eye.png);width:24px;height:24px;margin-right:16px;")
        self.ui.pw_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.hidePW = True

        
    def handleLogin(self):
        if (self.ui.email_input.text() == 'foo' and
            self.ui.pw_input.text() == 'bar'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

    