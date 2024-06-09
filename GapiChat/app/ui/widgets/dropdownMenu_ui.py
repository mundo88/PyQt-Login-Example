# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dropdownMenu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(298, 250)
        Form.setStyleSheet(u"#Form {\n"
"	background:transparent;\n"
"}\n"
"#widget {\n"
"background-color: rgb(255, 255, 255);\n"
"font-family:Segoe UI;\n"
"font-size:14px;\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setCursor(QCursor(Qt.PointingHandCursor))
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.widget.setStyleSheet(u"QPushButton {\n"
"	text-align:left;\n"
"	padding: 14px 16px;\n"
"	border:none;\n"
"	font-weight:450;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#f5f5f5\n"
"}\n"
"\n"
"QWidget {\n"
"	border-radius:4px\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/icon/icon/user-24x24-black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/config-24x24-black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/favorites-24x24-black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/bug-24x24-black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"\n"
"background-color:#cacaca;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton_5)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"  Trang c\u00e1 nh\u00e2n", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"  C\u00e0i \u0111\u1eb7t", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"  \u0110\u00e3 l\u01b0u", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"    B\u00e1o c\u00e1o s\u1ef1 c\u1ed1", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u0110\u0103ng xu\u1ea5t", None))
    # retranslateUi

