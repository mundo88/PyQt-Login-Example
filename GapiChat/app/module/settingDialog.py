from ..ui.dialog.settingUiDialog import Ui_settingUi
from PyQt5 import QtWidgets,QtCore,QtGui

class SettingDialog(QtWidgets.QDialog,Ui_settingUi):
    def __init__(self, parent=None):
        super(SettingDialog, self).__init__(parent)

        self.setupUi(self)
        self.setWindowFlags(
            QtCore.Qt.Dialog  | 
            QtCore.Qt.WindowCloseButtonHint |
            QtCore.Qt.WindowMinimizeButtonHint |
            QtCore.Qt.WindowMaximizeButtonHint
        )

        self.ACTIVE_BTN_COLOR = "background-color:#f2f2f2"
        self.DEACTIVE_BTN_COLOR = "background-color:#fff"
        
        self.init__app()

    def init__app(self):
        self.stackedWidget.setCurrentIndex(0)
        self.side_bar_settings.findChildren(QtWidgets.QPushButton)[0].setStyleSheet(self.ACTIVE_BTN_COLOR)

        [btn.clicked.connect(self.changeSettingPage) for btn in self.side_bar_settings.findChildren(QtWidgets.QPushButton)]
            
        theme_group = QtWidgets.QButtonGroup(self.widget_15) # Number group
        theme_group.addButton(self.light_radio)
        theme_group.addButton(self.dark_radio)
        theme_group.addButton(self.hight_contrast_radio)
        
        chat_density_group= QtWidgets.QButtonGroup(self.widget_22) # Number group
        chat_density_group.addButton(self.comfy_radio)
        chat_density_group.addButton(self.compact_radio)

        self.widget_14.mousePressEvent = lambda event :self.checkedRadio(self.light_radio)

        self.widget_16.mousePressEvent = lambda event :self.checkedRadio(self.dark_radio)
        self.widget_17.mousePressEvent = lambda event :self.checkedRadio(self.hight_contrast_radio)

        self.widget_23.mousePressEvent = lambda event :self.checkedRadio(self.comfy_radio)
        self.widget_25.mousePressEvent = lambda event :self.checkedRadio(self.compact_radio)


        self.btn_light.clicked.connect(lambda :self.checkedRadio(self.light_radio))
        self.btn_dark.clicked.connect(lambda :self.checkedRadio(self.dark_radio))
        self.btn_hight_contrast.clicked.connect(lambda :self.checkedRadio(self.hight_contrast_radio))

        self.btn_comfy.clicked.connect(lambda :self.checkedRadio(self.comfy_radio))
        self.btn_compact.clicked.connect(lambda :self.checkedRadio(self.compact_radio))


    def checkedRadio(self,radio):
        radio.setChecked(True)


    def changeSettingPage(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_general":
            self.stackedWidget.setCurrentWidget(self.general_page)
        if btnName == "btn_active":
            self.stackedWidget.setCurrentWidget(self.active_page)
        if btnName == "btn_notification":
            self.stackedWidget.setCurrentWidget(self.notification_page)
        if btnName == "btn_theme":
           self.stackedWidget.setCurrentWidget(self.theme_page)
        if btnName == "btn_policy":
           self.stackedWidget.setCurrentWidget(self.policy_page)
        self.resetStyle()
        btn.setStyleSheet(self.ACTIVE_BTN_COLOR)

    def resetStyle(self):
        for btn in self.side_bar_settings.findChildren(QtWidgets.QPushButton):
            btn.setStyleSheet(self.DEACTIVE_BTN_COLOR)

