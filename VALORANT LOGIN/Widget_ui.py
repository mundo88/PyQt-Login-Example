# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import Widget_Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 720)
        Form.setWindowOpacity(1.000000000000000)
        Form.setStyleSheet(u"background-color: rgb(249, 249, 249);")
        self.username_line_edit = QLineEdit(Form)
        self.username_line_edit.setObjectName(u"username_line_edit")
        self.username_line_edit.setGeometry(QRect(56, 217, 288, 48))
        self.username_line_edit.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	color: rgb(51, 51, 51);\n"
"	font: 75 8pt \"Microsoft YaHei\";\n"
"	background-color: rgb(237, 237, 237);\n"
"	padding:0px 10px\n"
"}\n"
"QLineEdit::hover {\n"
"	background-color: rgb(231, 231, 231);\n"
"}\n"
"QLineEdit::focus {\n"
"	border: 2px solid rgb(51, 51, 51);\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.password_line_edit = QLineEdit(Form)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setGeometry(QRect(56, 281, 288, 48))
        self.password_line_edit.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	color: rgb(51, 51, 51);\n"
"	font: 75 8pt \"Microsoft YaHei\";\n"
"	background-color: rgb(237, 237, 237);\n"
"	padding:0px 10px\n"
"}\n"
"QLineEdit::hover {\n"
"	background-color: rgb(231, 231, 231);\n"
"}\n"
"QLineEdit::focus {\n"
"	border: 2px solid rgb(51, 51, 51);\n"
"	background-color: rgb(249, 249, 249);\n"
"}")
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.sign_in_label = QLabel(Form)
        self.sign_in_label.setObjectName(u"sign_in_label")
        self.sign_in_label.setGeometry(QRect(160, 159, 80, 33))
        self.sign_in_label.setStyleSheet(u"border-image: url(:/resources/resources/Sign_in.png);")
        self.facebook_button = QPushButton(Form)
        self.facebook_button.setObjectName(u"facebook_button")
        self.facebook_button.setGeometry(QRect(56, 353, 91, 32))
        self.facebook_button.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/resources/resources/Facebook.png);\n"
"}\n"
"QPushButton::hover {\n"
"	border-image: url(:/resources/resources/Facebook_hovered.png);\n"
"}")
        self.google_button = QPushButton(Form)
        self.google_button.setObjectName(u"google_button")
        self.google_button.setGeometry(QRect(155, 353, 90, 32))
        self.google_button.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/resources/resources/Google.png);\n"
"}\n"
"QPushButton::hover {\n"
"	border-image: url(:/resources/resources/Google_hovered.png);\n"
"}")
        self.apple_button = QPushButton(Form)
        self.apple_button.setObjectName(u"apple_button")
        self.apple_button.setGeometry(QRect(253, 353, 91, 32))
        self.apple_button.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/resources/resources/Apple.png);\n"
"}\n"
"QPushButton::hover {\n"
"	border-image: url(:/resources/resources/Apple_hovered.png);\n"
"}")
        self.help_tooltip = QPushButton(Form)
        self.help_tooltip.setObjectName(u"help_tooltip")
        self.help_tooltip.setGeometry(QRect(326, 44, 22, 22))
        self.help_tooltip.setStyleSheet(u"border-image: url(:/resources/resources/Help2.png);")
        self.stay_signed_in_checkbox = QCheckBox(Form)
        self.stay_signed_in_checkbox.setObjectName(u"stay_signed_in_checkbox")
        self.stay_signed_in_checkbox.setGeometry(QRect(56, 395, 17, 21))
        self.stay_signed_in_checkbox.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"	border-image: url(:/resources/resources/Checkbox_unchecked.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"	border-image: url(:/resources/resources/Checkbox_unchecked_hovered.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border-image: url(:/resources/resources/Checkbox_checked.png);\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"	border-image: url(:/resources/resources/Checkbox_checked_hovered.png);\n"
"}")
        self.login_button = QPushButton(Form)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(168, 512, 64, 64))
        self.login_button.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/resources/resources/Login_button.png);\n"
"}\n"
"QPushButton::hover {\n"
"	border-image: url(:/resources/resources/Login_button_hovered.png);\n"
"}")
        self.version_label = QLabel(Form)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setGeometry(QRect(298, 657, 48, 18))
        self.version_label.setStyleSheet(u"QLabel {\n"
"	border-image: url(:/resources/resources/version_label.png);\n"
"}\n"
"QLabel::hover {\n"
"	border-image: url(:/resources/resources/version_label_hovered.png);\n"
"}")
        self.label_1 = QLabel(Form)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(156, 637, 88, 18))
        self.label_1.setStyleSheet(u"QLabel {\n"
"	border-image: url(:/resources/resources/Label_1.png);\n"
"}\n"
"QLabel::hover {\n"
"	border-image: url(:/resources/resources/Label_1_hovered.png);\n"
"}")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(149, 654, 102, 18))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	border-image: url(:/resources/resources/Label_2.png);\n"
"}\n"
"QLabel::hover {\n"
"	border-image: url(:/resources/resources/Label_2_hovered.png);\n"
"}")
        self.checkbox_label = QLabel(Form)
        self.checkbox_label.setObjectName(u"checkbox_label")
        self.checkbox_label.setGeometry(QRect(77, 395, 94, 22))
        self.checkbox_label.setStyleSheet(u"QLabel {\n"
"	border-image: url(:/resources/resources/Checkbox_label.png);\n"
"}\n"
"QLabel::hover {\n"
"	border-image: url(:/resources/resources/Checkbox_label_hovered.png);\n"
"}")
        self.riot_games_logo = QLabel(Form)
        self.riot_games_logo.setObjectName(u"riot_games_logo")
        self.riot_games_logo.setGeometry(QRect(138, 51, 126, 61))
        self.riot_games_logo.setStyleSheet(u"border-image: url(:/resources/resources/Riot_Games.png);")
        self.username_label = QLabel(Form)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(72, 236, 59, 8))
        self.username_label.setStyleSheet(u"border-image: url(:/resources/resources/Username_label.png);")
        self.password_label = QLabel(Form)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(72, 300, 61, 8))
        self.password_label.setStyleSheet(u"border-image: url(:/resources/resources/Password_label.png);")
        QWidget.setTabOrder(self.help_tooltip, self.username_line_edit)
        QWidget.setTabOrder(self.username_line_edit, self.password_line_edit)
        QWidget.setTabOrder(self.password_line_edit, self.facebook_button)
        QWidget.setTabOrder(self.facebook_button, self.google_button)
        QWidget.setTabOrder(self.google_button, self.apple_button)
        QWidget.setTabOrder(self.apple_button, self.stay_signed_in_checkbox)
        QWidget.setTabOrder(self.stay_signed_in_checkbox, self.login_button)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Widget", None))
        self.sign_in_label.setText("")
        self.facebook_button.setText("")
        self.google_button.setText("")
        self.apple_button.setText("")
        self.help_tooltip.setText("")
        self.stay_signed_in_checkbox.setText("")
        self.login_button.setText("")
        self.version_label.setText("")
        self.label_1.setText("")
        self.label_2.setText("")
        self.checkbox_label.setText("")
        self.riot_games_logo.setText("")
        self.username_label.setText("")
        self.password_label.setText("")
    # retranslateUi

