__version__ = 1
from re import S
from typing_extensions import Self
from PyQt5 import QtWidgets,QtGui,QtCore
from .ui.main import mainWindow
from .module.dropdownMenu import UserDropdownMenu
from .module.settingDialog import SettingDialog




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)


        self.user_menu = UserDropdownMenu(self)
        self.setting_dialog = SettingDialog(self)
    

        self.init_btn()

    def init_btn(self):
        self.ui.chat_link.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.member_link.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.todo_list_link.clicked.connect(lambda:self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.on_send_image.clicked.connect(self.openFileNamesDialog)

        self.ui.user_btn.clicked.connect(self.user_menu.onShow)
        self.user_menu.pushButton_3.clicked.connect(lambda:(self.setting_dialog.show(),self.user_menu.setVisible(False)))





    def openFileNamesDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;PNG (*.png)", options=options)
        if files:
            print(files)



    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        self.oldX = event.globalX()
        self.oldY = event.globalY()
        if not self.user_menu.underMouse() and self.user_menu.isVisible():
            self.user_menu.setVisible(False)
