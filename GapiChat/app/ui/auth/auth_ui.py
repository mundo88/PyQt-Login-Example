# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_AuthScreen(object):
    def setupUi(self, AuthScreen):
        if not AuthScreen.objectName():
            AuthScreen.setObjectName(u"AuthScreen")
        AuthScreen.setWindowModality(Qt.ApplicationModal)
        AuthScreen.setEnabled(True)
        AuthScreen.resize(1205, 780)
        AuthScreen.setMinimumSize(QSize(1205, 780))
        AuthScreen.setMaximumSize(QSize(1247, 780))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        AuthScreen.setFont(font)
        icon = QIcon()
        icon.addFile(u":/image/image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        AuthScreen.setWindowIcon(icon)
        AuthScreen.setAutoFillBackground(False)
        AuthScreen.setStyleSheet(u"font-family:Segoe UI")
        AuthScreen.setSizeGripEnabled(False)
        self.horizontalLayout = QHBoxLayout(AuthScreen)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.style = QWidget(AuthScreen)
        self.style.setObjectName(u"style")
        self.style.setFont(font)
        self.style.setStyleSheet(u"#auth_bg {\n"
"	background-color:#f4f4f4;\n"
"}\n"
"#auth_form {\n"
"	background-color:#fff;\n"
"}\n"
"QLineEdit {\n"
"	background: #FFFFFF;\n"
"	border: 1px solid #D3D7DF;\n"
"	border-radius: 4px;\n"
"	color : #50565f;\n"
"	padding-left:16px\n"
"    \n"
"}\n"
"QLineEdit:hover , QLineEdit:focus {\n"
"	border-color: #065FD4;    \n"
"}\n"
"\n"
"QPushButton:pressed   {\n"
"	margin:1px\n"
"}\n"
"\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.style)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.container = QWidget(self.style)
        self.container.setObjectName(u"container")
        self.container.setFont(font)
        self.horizontalLayout_7 = QHBoxLayout(self.container)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.auth_bg = QWidget(self.container)
        self.auth_bg.setObjectName(u"auth_bg")
        self.auth_bg.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.auth_bg)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(40, 30, 40, 30)
        self.auth_bg_content = QWidget(self.auth_bg)
        self.auth_bg_content.setObjectName(u"auth_bg_content")
        self.auth_bg_content.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.auth_bg_content)
        self.verticalLayout_6.setSpacing(50)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.auth_bg_content)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMaximumSize(QSize(115, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.home_btn.setFont(font1)
        self.home_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn.setLayoutDirection(Qt.LeftToRight)
        self.home_btn.setStyleSheet(u"color: rgb(137, 141, 147);\n"
"border:none")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon1)
        self.home_btn.setIconSize(QSize(24, 24))
        self.home_btn.setAutoDefault(True)
        self.home_btn.setFlat(True)

        self.verticalLayout_6.addWidget(self.home_btn)

        self.widget = QWidget(self.auth_bg_content)
        self.widget.setObjectName(u"widget")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(True)
        self.widget.setFont(font2)
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.widget)

        self.widget_2 = QWidget(self.auth_bg_content)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 335))
        self.widget_2.setFont(font)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(475, 335))
        self.label_2.setMaximumSize(QSize(445, 335))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border-image: url(:/image/image/auth-apppng.png);")

        self.horizontalLayout_8.addWidget(self.label_2)


        self.verticalLayout_6.addWidget(self.widget_2)


        self.verticalLayout_4.addWidget(self.auth_bg_content)


        self.horizontalLayout_7.addWidget(self.auth_bg)

        self.auth_form = QWidget(self.container)
        self.auth_form.setObjectName(u"auth_form")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(13)
        self.auth_form.setFont(font3)
        self.horizontalLayout_9 = QHBoxLayout(self.auth_form)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.auth_form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setFont(font)
        self.widget_3.setFocusPolicy(Qt.ClickFocus)
        self.widget_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.widget_3.setAcceptDrops(False)
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setSpacing(25)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(140, 70, 140, 40)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_img = QLabel(self.widget_3)
        self.logo_img.setObjectName(u"logo_img")
        self.logo_img.setMaximumSize(QSize(21, 17))
        self.logo_img.setFont(font)
        self.logo_img.setStyleSheet(u"border-image: url(:/image/image/logo.png);")

        self.horizontalLayout_2.addWidget(self.logo_img)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)


        self.verticalLayout_11.addLayout(self.verticalLayout)

        self.login_gg_btn = QPushButton(self.widget_3)
        self.login_gg_btn.setObjectName(u"login_gg_btn")
        self.login_gg_btn.setMinimumSize(QSize(350, 45))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.login_gg_btn.setFont(font4)
        self.login_gg_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_gg_btn.setStyleSheet(u"#login_gg_btn {\n"
"\n"
"\n"
"color:#065FD4;\n"
"\n"
"font-weight:500;\n"
"\n"
"border-radius: 6px;\n"
"\n"
"background: #FFFFFF;\n"
"\n"
"border:1px solid #065FD4\n"
"}\n"
"\n"
"#login_gg_btn:hover {\n"
"	background-color :rgb(244, 244, 244)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon-color/icon-color/google.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_gg_btn.setIcon(icon2)

        self.verticalLayout_11.addWidget(self.login_gg_btn)

        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(40, 30, 271, 20))
        self.line.setMaximumSize(QSize(16777215, 30))
        self.line.setFont(font)
        self.line.setStyleSheet(u"color :#D3D7DF;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 30, 191, 20))
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.frame)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setFont(font)

        self.verticalLayout_2.addWidget(self.label_5)

        self.email_input = QLineEdit(self.widget_3)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setMinimumSize(QSize(350, 45))
        self.email_input.setFont(font3)
        self.email_input.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_2.addWidget(self.email_input)


        self.verticalLayout_11.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 25))
        self.label_6.setFont(font)

        self.verticalLayout_3.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pw_input = QLineEdit(self.widget_3)
        self.pw_input.setObjectName(u"pw_input")
        self.pw_input.setMinimumSize(QSize(350, 45))
        self.pw_input.setFont(font3)
        self.pw_input.setStyleSheet(u"padding-right:45px")
        self.pw_input.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.pw_input)

        self.show_hide_pw = QPushButton(self.widget_3)
        self.show_hide_pw.setObjectName(u"show_hide_pw")
        self.show_hide_pw.setFont(font)
        self.show_hide_pw.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_hide_pw.setStyleSheet(u"\n"
"border-image: url(:/icon/icon/eye.png);\n"
"width:24px;\n"
"height:24px;\n"
"margin-right:16px;")

        self.horizontalLayout_3.addWidget(self.show_hide_pw)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_11.addLayout(self.verticalLayout_3)

        self.login_btn = QPushButton(self.widget_3)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(350, 45))
        self.login_btn.setFont(font4)
        self.login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn.setStyleSheet(u"#login_btn {\n"
"	\n"
"	color:#FFF;\n"
"	font-weight:500;\n"
"	border-radius: 6px;\n"
"	background: #e74725;\n"
"}\n"
"\n"
"#login_btn:hover {\n"
"\n"
"	background: rgb(212, 63, 34);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login_btn.setIcon(icon3)
        self.login_btn.setAutoRepeat(False)

        self.verticalLayout_11.addWidget(self.login_btn)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setOpenExternalLinks(True)

        self.verticalLayout_11.addWidget(self.label_8)


        self.horizontalLayout_9.addWidget(self.widget_3)


        self.horizontalLayout_7.addWidget(self.auth_form)


        self.horizontalLayout_12.addWidget(self.container)


        self.horizontalLayout.addWidget(self.style)


        self.retranslateUi(AuthScreen)

        self.home_btn.setDefault(True)


        QMetaObject.connectSlotsByName(AuthScreen)
    # setupUi

    def retranslateUi(self, AuthScreen):
        AuthScreen.setWindowTitle(QCoreApplication.translate("AuthScreen", u"GapiChat", None))
        self.home_btn.setText(QCoreApplication.translate("AuthScreen", u"  Trang ch\u1ee7", None))
        self.label.setText(QCoreApplication.translate("AuthScreen", u"<html><head/><body><p><span style=\" font-size:22pt; color:#3b4350;\">Gapi gi\u00fap b\u1ea1n k\u1ebft n\u1ed1i v\u00e0 chia s\u1ebb v\u1edbi m\u1ecdi ng\u01b0\u1eddi trong cu\u1ed9c s\u1ed1ng c\u1ee7a b\u1ea1n..</span></p><p><span style=\" font-size:14pt; color:#898d93;\">Tham gia Gapi ngay b\u1eb1ng c\u00e1ch \u0111\u0103ng nh\u1eadp ho\u1eb7c \u0111\u0103ng k\u00ed.</span></p></body></html>", None))
        self.label_2.setText("")
        self.logo_img.setText("")
        self.label_3.setText(QCoreApplication.translate("AuthScreen", u"<html><head/><body><p><span style=\" font-size:24pt;\">Gapi</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("AuthScreen", u"<html><head/><body><p><span style=\" font-size:11pt; color:#898d93;\">Vui l\u00f2ng \u0111\u0103ng nh\u1eadp \u0111\u1ec3 s\u1eed d\u1ee5ng GapiChat.</span></p></body></html>", None))
        self.login_gg_btn.setText(QCoreApplication.translate("AuthScreen", u" Log in with Google", None))
        self.label_7.setText(QCoreApplication.translate("AuthScreen", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#e74425;\">LOG IN FOR EXTERNAL USER</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("AuthScreen", u"<html><head/><body><p><span style=\" font-size:16pt; color:#50565f;\">Username or Email</span></p></body></html>", None))
        self.email_input.setText("")
        self.email_input.setPlaceholderText(QCoreApplication.translate("AuthScreen", u"Enter your username or email", None))
        self.label_6.setText(QCoreApplication.translate("AuthScreen", u"<html><head/><body><p><span style=\" font-size:16pt; color:#50565f;\">Password</span></p></body></html>", None))
        self.pw_input.setText("")
        self.pw_input.setPlaceholderText(QCoreApplication.translate("AuthScreen", u"Enter your password", None))
#if QT_CONFIG(tooltip)
        self.show_hide_pw.setToolTip(QCoreApplication.translate("AuthScreen", u"Xem m\u1eadt kh\u1ea9u", None))
#endif // QT_CONFIG(tooltip)
        self.show_hide_pw.setText("")
        self.login_btn.setText(QCoreApplication.translate("AuthScreen", u"Log in ", None))
#if QT_CONFIG(shortcut)
        self.login_btn.setShortcut(QCoreApplication.translate("AuthScreen", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.label_8.setText(QCoreApplication.translate("AuthScreen", u"<p><span style=\" font-size:12pt; color:#898d93;\">I have not account ? </span><a href=\"http://192.168.0.16:8080/signup\" style=\" font-size:12pt;text-decoration:none; font-weight:600; color:#065fd4;\">Sign up now</span><span style=\" font-size:12pt; color:#065fd4;\">.</a></p>", None))
    # retranslateUi

