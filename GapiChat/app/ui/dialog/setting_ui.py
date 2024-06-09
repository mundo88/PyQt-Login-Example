# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_settingUi(object):
    def setupUi(self, settingUi):
        if not settingUi.objectName():
            settingUi.setObjectName(u"settingUi")
        settingUi.resize(838, 573)
        settingUi.setMaximumSize(QSize(16777215, 16777215))
        settingUi.setStyleSheet(u"QWidget {\n"
"	font-family:Segoe UI;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
" QCheckBox {color: rgb(71,75,78);}\n"
" QCheckBox::indicator {\n"
"   width:24px;\n"
"	height:24px;\n"
"font-size:12px;\n"
"	border-image: url(:/icon/icon/unchecked-checkbox-50.png)\n"
" }\n"
"QCheckBox::indicator:hover {\n"
"         \n"
"	border-image: url(:/icon/icon/unchecked-checkbox-hover-50.png);\n"
"}\n"
"QCheckBox::indicator:checked {       \n"
"        \n"
"	border-image: url(:/icon/icon/checked-checkbox-50.png);\n"
"}\n"
"QComboBox {\n"
"	\n"
"	border:1px solid transparent;\n"
"	padding:6px 12px;\n"
"	background-color:#f2f2f2;\n"
"	border-radius:4px;\n"
"	font-size:14px\n"
"}\n"
"QComboBox:hover {\n"
"	background-color:#e2e2e2;\n"
"}\n"
"QComboBox:focus {\n"
"	border-color:#ef4725;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border:none;\n"
"	border-image: url(:/icon/icon/ar-down.png);\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"    border-left: 1px solid #cacaca; /* This seems to replace the whole arrow of "
                        "the combo box */\n"
"	min-width:30px\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        color: rgb(0, 0, 0);   \n"
"        background-color: rgb(255, 255, 255);\n"
"        padding: 10px;\n"
"        selection-background-color: #ef4725;\n"
"        border:none;\n"
"		 border-radius:4px;\n"
"		height:30px\n"
"   }\n"
"\n"
"QListView::item {\n"
"	height:30px;\n"
"}\n"
"QRadioButton::indicator {\n"
"	border-image:url(:/icon/icon/unchecked-radio-button.png);\n"
"	background-repeat:none;\n"
"	background-position:center;\n"
"	width:24px;\n"
"	height:24px;\n"
"}\n"
"QRadioButton::indicator::hover {\n"
"	border-image: url(:/icon/icon/hover-radio-button.png);\n"
"}\n"
"QRadioButton::indicator::checked {\n"
"	border-image: url(:/icon/icon/checked-radio-button.png);\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(settingUi)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_bar_settings = QWidget(settingUi)
        self.side_bar_settings.setObjectName(u"side_bar_settings")
        self.side_bar_settings.setMinimumSize(QSize(260, 0))
        self.side_bar_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_bar_settings.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	font-size:16px;\n"
"	text-align:left;\n"
"	padding:16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color:#f5f5f5;\n"
"}\n"
"QWidget#side_bar_settings {\n"
"	border-right:1px solid #cacaca\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.side_bar_settings)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 1, 0)
        self.btn_general = QPushButton(self.side_bar_settings)
        self.btn_general.setObjectName(u"btn_general")
        icon = QIcon()
        icon.addFile(u":/icon-color/icon-color/settings-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_general.setIcon(icon)
        self.btn_general.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_general)

        self.btn_active = QPushButton(self.side_bar_settings)
        self.btn_active.setObjectName(u"btn_active")
        icon1 = QIcon()
        icon1.addFile(u":/icon-color/icon-color/active-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_active.setIcon(icon1)
        self.btn_active.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_active)

        self.btn_notification = QPushButton(self.side_bar_settings)
        self.btn_notification.setObjectName(u"btn_notification")
        icon2 = QIcon()
        icon2.addFile(u":/icon-color/icon-color/notification-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_notification.setIcon(icon2)
        self.btn_notification.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_notification)

        self.btn_theme = QPushButton(self.side_bar_settings)
        self.btn_theme.setObjectName(u"btn_theme")
        icon3 = QIcon()
        icon3.addFile(u":/icon-color/icon-color/themes-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_theme.setIcon(icon3)
        self.btn_theme.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_theme)

        self.btn_policy = QPushButton(self.side_bar_settings)
        self.btn_policy.setObjectName(u"btn_policy")
        icon4 = QIcon()
        icon4.addFile(u":/icon-color/icon-color/policy-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_policy.setIcon(icon4)
        self.btn_policy.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_policy, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.side_bar_settings)

        self.stackedWidget = QStackedWidget(settingUi)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.general_page = QWidget()
        self.general_page.setObjectName(u"general_page")
        self.horizontalLayout_2 = QHBoxLayout(self.general_page)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.general_page)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_general = QWidget(self.widget_2)
        self.header_general.setObjectName(u"header_general")
        self.header_general.setMinimumSize(QSize(0, 0))
        self.header_general.setMaximumSize(QSize(16777215, 64))
        self.header_general.setStyleSheet(u"QWidget #header_general {\n"
"	border-bottom:1px solid #cacaca\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.header_general)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(24, 0, 24, 1)
        self.label = QLabel(self.header_general)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.header_general)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(24, 0, 24, 0)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignTop)

        self.checkBox = QCheckBox(self.widget_3)
        self.checkBox.setObjectName(u"checkBox")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.checkBox.setFont(font)

        self.verticalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.widget_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font)

        self.verticalLayout_3.addWidget(self.checkBox_2)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.general_page)
        self.active_page = QWidget()
        self.active_page.setObjectName(u"active_page")
        self.horizontalLayout_5 = QHBoxLayout(self.active_page)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.active_page)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.header_general_2 = QWidget(self.widget_4)
        self.header_general_2.setObjectName(u"header_general_2")
        self.header_general_2.setMinimumSize(QSize(0, 0))
        self.header_general_2.setMaximumSize(QSize(16777215, 64))
        self.header_general_2.setStyleSheet(u"QWidget #header_general_2 {\n"
"	border-bottom:1px solid #cacaca\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.header_general_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(24, 0, 24, 1)
        self.label_3 = QLabel(self.header_general_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.header_general_2)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setSpacing(22)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(24, 0, 24, 0)
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_5.addWidget(self.label_4, 0, Qt.AlignTop)

        self.checkBox_3 = QCheckBox(self.widget_5)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBox_3)

        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 12, 60, -1)
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.label_5.setFont(font1)
        self.label_5.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout_5.addWidget(self.widget_6)


        self.verticalLayout_4.addWidget(self.widget_5, 0, Qt.AlignTop)


        self.horizontalLayout_5.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.active_page)
        self.notification_page = QWidget()
        self.notification_page.setObjectName(u"notification_page")
        self.verticalLayout_8 = QVBoxLayout(self.notification_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.notification_page)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_6 = QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.header_general_3 = QWidget(self.widget_7)
        self.header_general_3.setObjectName(u"header_general_3")
        self.header_general_3.setMinimumSize(QSize(0, 0))
        self.header_general_3.setMaximumSize(QSize(16777215, 64))
        self.header_general_3.setStyleSheet(u"QWidget #header_general_3 {\n"
"	border-bottom:1px solid #cacaca\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.header_general_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(24, 0, 24, 1)
        self.label_7 = QLabel(self.header_general_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))

        self.verticalLayout_11.addWidget(self.label_7)


        self.verticalLayout_6.addWidget(self.header_general_3)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(24, 12, 24, 0)
        self.label_8 = QLabel(self.widget_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 24))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(True)
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8, 0, Qt.AlignTop)

        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setMaximumSize(QSize(16777215, 45))
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setMargin(0)

        self.verticalLayout_7.addWidget(self.label_9)

        self.widget = QWidget(self.widget_8)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"\n"
"	border-bottom:1px solid #cacaca\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, -1, 24)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"text-align:left;\n"
"border:none;\n"
"color:#e74725;\n"
"font-weight:bold")
        icon5 = QIcon()
        icon5.addFile(u":/icon-color/icon-color/icons8-windows-10-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.pushButton)


        self.verticalLayout_7.addWidget(self.widget)

        self.label_10 = QLabel(self.widget_8)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"QWidget#widget_9 {\n"
"\n"
"	border-bottom:1px solid #cacaca\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.widget_9)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 9, 0, 24)
        self.checkBox_4 = QCheckBox(self.widget_9)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMinimumSize(QSize(0, 0))
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.checkBox_4)


        self.verticalLayout_7.addWidget(self.widget_9)


        self.verticalLayout_6.addWidget(self.widget_8, 0, Qt.AlignTop)

        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_12 = QVBoxLayout(self.widget_10)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(24, 16, 24, 0)
        self.label_11 = QLabel(self.widget_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_12.addWidget(self.label_11, 0, Qt.AlignTop)

        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 24, 0, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(24)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(self.widget_11)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.widget_11)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.widget_11)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.widget_11)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.label_14 = QLabel(self.widget_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_12 = QLabel(self.widget_11)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)


        self.horizontalLayout_7.addLayout(self.gridLayout)


        self.verticalLayout_12.addWidget(self.widget_11, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.widget_10, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.notification_page)
        self.theme_page = QWidget()
        self.theme_page.setObjectName(u"theme_page")
        self.horizontalLayout_10 = QHBoxLayout(self.theme_page)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.theme_page)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_13 = QVBoxLayout(self.widget_12)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.header_general_4 = QWidget(self.widget_12)
        self.header_general_4.setObjectName(u"header_general_4")
        self.header_general_4.setMinimumSize(QSize(0, 0))
        self.header_general_4.setMaximumSize(QSize(16777215, 64))
        self.header_general_4.setStyleSheet(u"QWidget #header_general_4 {\n"
"	border-bottom:1px solid #cacaca\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.header_general_4)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(24, 0, 24, 1)
        self.label_16 = QLabel(self.header_general_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 0))

        self.verticalLayout_14.addWidget(self.label_16)


        self.verticalLayout_13.addWidget(self.header_general_4)

        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_15 = QVBoxLayout(self.widget_13)
        self.verticalLayout_15.setSpacing(12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(24, 12, 24, 24)
        self.label_17 = QLabel(self.widget_13)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 24))
        self.label_17.setMaximumSize(QSize(16777215, 30))
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"QRadioButton {\n"
"	background-color: transparent;\n"
"}")

        self.verticalLayout_15.addWidget(self.label_17, 0, Qt.AlignTop)

        self.widget_15 = QWidget(self.widget_13)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"QRadioButton {\n"
"	background-color:transparent\n"
"}\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_11.setSpacing(14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 10, 0)
        self.widget_14 = QWidget(self.widget_15)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 0))
        self.widget_14.setMaximumSize(QSize(16777215, 16777215))
        self.widget_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.widget_14.setLayoutDirection(Qt.LeftToRight)
        self.widget_14.setStyleSheet(u"QWidget#widget_14 {\n"
"	border-radius:4px;\n"
"	border:1px solid #cacaca;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.widget_14)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(12, 12, 12, 12)
        self.btn_light = QPushButton(self.widget_14)
        self.btn_light.setObjectName(u"btn_light")
        self.btn_light.setMinimumSize(QSize(140, 87))
        self.btn_light.setMaximumSize(QSize(140, 87))
        self.btn_light.setStyleSheet(u"border-image: url(:/image/image/light-theme.svg);")

        self.verticalLayout_16.addWidget(self.btn_light)

        self.widget_19 = QWidget(self.widget_14)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 6, 0, 0)
        self.label_18 = QLabel(self.widget_19)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_9.addWidget(self.label_18)

        self.light_radio = QRadioButton(self.widget_19)
        self.light_radio.setObjectName(u"light_radio")
        self.light_radio.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_9.addWidget(self.light_radio)


        self.verticalLayout_16.addWidget(self.widget_19)


        self.horizontalLayout_11.addWidget(self.widget_14)

        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 0))
        self.widget_16.setMaximumSize(QSize(16777215, 16777215))
        self.widget_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.widget_16.setLayoutDirection(Qt.LeftToRight)
        self.widget_16.setStyleSheet(u"QWidget#widget_16 {\n"
"	border-radius:4px;\n"
"	border:1px solid #cacaca;\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.widget_16)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(12, 12, 12, 12)
        self.btn_dark = QPushButton(self.widget_16)
        self.btn_dark.setObjectName(u"btn_dark")
        self.btn_dark.setMinimumSize(QSize(140, 87))
        self.btn_dark.setMaximumSize(QSize(140, 87))
        self.btn_dark.setStyleSheet(u"border-image: url(:/image/image/dark-theme.svg);")

        self.verticalLayout_17.addWidget(self.btn_dark)

        self.widget_20 = QWidget(self.widget_16)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 6, 0, 0)
        self.label_19 = QLabel(self.widget_20)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_19)

        self.dark_radio = QRadioButton(self.widget_20)
        self.dark_radio.setObjectName(u"dark_radio")
        self.dark_radio.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_13.addWidget(self.dark_radio)


        self.verticalLayout_17.addWidget(self.widget_20)


        self.horizontalLayout_11.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_15)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 0))
        self.widget_17.setMaximumSize(QSize(16777215, 16777215))
        self.widget_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.widget_17.setLayoutDirection(Qt.LeftToRight)
        self.widget_17.setStyleSheet(u"QWidget#widget_17 {\n"
"	border-radius:4px;\n"
"	border:1px solid #cacaca;\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.widget_17)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(12, 12, 12, 12)
        self.btn_hight_contrast = QPushButton(self.widget_17)
        self.btn_hight_contrast.setObjectName(u"btn_hight_contrast")
        self.btn_hight_contrast.setMinimumSize(QSize(140, 87))
        self.btn_hight_contrast.setMaximumSize(QSize(140, 87))
        self.btn_hight_contrast.setStyleSheet(u"border-image: url(:/image/image/hight-contrast-theme.svg)")

        self.verticalLayout_18.addWidget(self.btn_hight_contrast)

        self.widget_21 = QWidget(self.widget_17)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 6, 0, 0)
        self.label_20 = QLabel(self.widget_21)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_20)

        self.hight_contrast_radio = QRadioButton(self.widget_21)
        self.hight_contrast_radio.setObjectName(u"hight_contrast_radio")
        self.hight_contrast_radio.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_14.addWidget(self.hight_contrast_radio)


        self.verticalLayout_18.addWidget(self.widget_21)


        self.horizontalLayout_11.addWidget(self.widget_17)


        self.verticalLayout_15.addWidget(self.widget_15, 0, Qt.AlignLeft)

        self.widget_18 = QWidget(self.widget_13)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setStyleSheet(u"QWidget #widget_18 {\n"
"	border-bottom:1px solid #cacaca\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 6, 0, 32)
        self.checkBox_5 = QCheckBox(self.widget_18)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font)
        self.checkBox_5.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_5.setChecked(True)

        self.horizontalLayout_12.addWidget(self.checkBox_5, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.widget_18)

        self.label_21 = QLabel(self.widget_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 24))
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"QRadioButton {\n"
"	background-color: transparent;\n"
"}")

        self.verticalLayout_15.addWidget(self.label_21)

        self.widget_22 = QWidget(self.widget_13)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_17.setSpacing(14)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(0, 0))
        self.widget_23.setMaximumSize(QSize(16777215, 16777215))
        self.widget_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.widget_23.setLayoutDirection(Qt.LeftToRight)
        self.widget_23.setStyleSheet(u"QWidget#widget_23 {\n"
"	border-radius:4px;\n"
"	border:1px solid #cacaca;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.widget_23)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(12, 12, 12, 12)
        self.btn_comfy = QPushButton(self.widget_23)
        self.btn_comfy.setObjectName(u"btn_comfy")
        self.btn_comfy.setMinimumSize(QSize(140, 87))
        self.btn_comfy.setMaximumSize(QSize(140, 87))
        self.btn_comfy.setStyleSheet(u"border-image: url(:/image/image/chat-density-comfy-default.svg);")

        self.verticalLayout_19.addWidget(self.btn_comfy)

        self.widget_24 = QWidget(self.widget_23)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 6, 0, 0)
        self.label_22 = QLabel(self.widget_24)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)
        self.label_22.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_15.addWidget(self.label_22)

        self.comfy_radio = QRadioButton(self.widget_24)
        self.comfy_radio.setObjectName(u"comfy_radio")
        self.comfy_radio.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_15.addWidget(self.comfy_radio)


        self.verticalLayout_19.addWidget(self.widget_24)


        self.horizontalLayout_17.addWidget(self.widget_23)

        self.widget_25 = QWidget(self.widget_22)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(0, 0))
        self.widget_25.setMaximumSize(QSize(16777215, 16777215))
        self.widget_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.widget_25.setLayoutDirection(Qt.LeftToRight)
        self.widget_25.setStyleSheet(u"QWidget#widget_25 {\n"
"	border-radius:4px;\n"
"	border:1px solid #cacaca;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.widget_25)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(12, 12, 12, 12)
        self.btn_compact = QPushButton(self.widget_25)
        self.btn_compact.setObjectName(u"btn_compact")
        self.btn_compact.setMinimumSize(QSize(140, 87))
        self.btn_compact.setMaximumSize(QSize(140, 87))
        self.btn_compact.setStyleSheet(u"border-image: url(:/image/image/chat-density-compact-default.svg);")

        self.verticalLayout_20.addWidget(self.btn_compact)

        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 6, 0, 0)
        self.label_23 = QLabel(self.widget_26)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)
        self.label_23.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_16.addWidget(self.label_23)

        self.compact_radio = QRadioButton(self.widget_26)
        self.compact_radio.setObjectName(u"compact_radio")
        self.compact_radio.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_16.addWidget(self.compact_radio)


        self.verticalLayout_20.addWidget(self.widget_26)


        self.horizontalLayout_17.addWidget(self.widget_25)


        self.verticalLayout_15.addWidget(self.widget_22, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.widget_13, 0, Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.widget_12)

        self.stackedWidget.addWidget(self.theme_page)
        self.policy_page = QWidget()
        self.policy_page.setObjectName(u"policy_page")
        self.verticalLayout_22 = QVBoxLayout(self.policy_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.header_general_5 = QWidget(self.policy_page)
        self.header_general_5.setObjectName(u"header_general_5")
        self.header_general_5.setMinimumSize(QSize(0, 0))
        self.header_general_5.setMaximumSize(QSize(16777215, 64))
        self.header_general_5.setStyleSheet(u"QWidget #header_general_5 {\n"
"	border-bottom:1px solid #cacaca\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.header_general_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(24, 0, 24, 1)
        self.label_15 = QLabel(self.header_general_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.label_15)


        self.verticalLayout_22.addWidget(self.header_general_5)

        self.widget_27 = QWidget(self.policy_page)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setStyleSheet(u"QLabel {\n"
"	color:#000;\n"
"	text-decoration: underline;\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.widget_27)
        self.verticalLayout_21.setSpacing(12)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(24, 24, 24, 0)
        self.label_24 = QLabel(self.widget_27)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"text-decoration: underline;")

        self.verticalLayout_21.addWidget(self.label_24)

        self.label_25 = QLabel(self.widget_27)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_21.addWidget(self.label_25)

        self.label_26 = QLabel(self.widget_27)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_21.addWidget(self.label_26)

        self.label_28 = QLabel(self.widget_27)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_21.addWidget(self.label_28)


        self.verticalLayout_22.addWidget(self.widget_27, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.policy_page)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(settingUi)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(settingUi)
    # setupUi

    def retranslateUi(self, settingUi):
        settingUi.setWindowTitle(QCoreApplication.translate("settingUi", u"C\u00e0i \u0111\u1eb7t", None))
        self.btn_general.setText(QCoreApplication.translate("settingUi", u"  Chung", None))
        self.btn_active.setText(QCoreApplication.translate("settingUi", u"  Tr\u1ea1ng th\u00e1i ho\u1ea1t \u0111\u1ed9ng", None))
        self.btn_notification.setText(QCoreApplication.translate("settingUi", u"  Th\u00f4ng b\u00e1o", None))
        self.btn_theme.setText(QCoreApplication.translate("settingUi", u"  Giao di\u1ec7n v\u00e0 tr\u1ee3 n\u0103ng", None))
        self.btn_policy.setText(QCoreApplication.translate("settingUi", u"  Ch\u00ednh s\u00e1ch", None))
        self.label.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">C\u00e0i \u0111\u1eb7t chung</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">H\u1ec7 th\u1ed1ng</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("settingUi", u"Kh\u1edfi \u0111\u1ed9ng c\u00f9ng h\u1ec7 th\u1ed1ng", None))
        self.checkBox_2.setText(QCoreApplication.translate("settingUi", u"Icon thanh t\u00e1c v\u1ee5", None))
        self.label_3.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Tr\u1ea1ng th\u00e1i ho\u1ea1t \u0111\u1ed9ng</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Hi\u1ec3n th\u1ecb trang th\u00e1i ho\u1ea1t \u0111\u1ed9ng</span></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("settingUi", u"Trang th\u00e1i ho\u1ea1t \u0111\u1ed9ng", None))
        self.label_6.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Tr\u1ea1ng th\u00e1i ho\u1ea1t \u0111\u1ed9ng : \u0110ang b\u1eadt</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p>B\u1ea1n b\u00e8 v\u00e0 ng\u01b0\u1eddi li\u00ean h\u1ec7 c\u1ee7a b\u1ea1n s\u1ebd bi\u1ebft khi n\u00e0o b\u1ea1n \u0111ang ho\u1ea1t \u0111\u1ed9ng ho\u1eb7c ho\u1ea1t \u0111\u1ed9ng g\u1ea7n \u0111\u00e2y. B\u1ea1n s\u1ebd hi\u1ec3n th\u1ecb l\u00e0 \u0111ang ho\u1ea1t \u0111\u1ed9ng ho\u1eb7c ho\u1ea1t \u0111\u1ed9ng g\u1ea7n \u0111\u00e2y, tr\u1eeb khi b\u1ea1n t\u1eaft c\u00e0i \u0111\u1eb7t n\u00e0y \u1edf m\u1ecdi n\u01a1i b\u1ea1n \u0111ang d\u00f9ng Messenger hay Facebook. B\u1ea1n c\u0169ng s\u1ebd bi\u1ebft khi n\u00e0o b\u1ea1n b\u00e8 v\u00e0 ng\u01b0\u1eddi li\u00ean h\u1ec7 c\u1ee7a m\u00ecnh \u0111ang ho\u1ea1t \u0111\u1ed9ng ho\u1eb7c ho\u1ea1t \u0111\u1ed9ng g\u1ea7n \u0111\u00e2y.</p><p><br/></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">C\u00e0i \u0111\u1eb7t th\u00f4ng b\u00e1o</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:11pt;\">Th\u00f4ng b\u00e1o v\u00e0 \u00e2m thanh</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("settingUi", u"M\u1edf c\u00e0i \u0111\u1eb7t th\u00f4ng b\u00e1o Windows \u0111\u1ec3 cho ph\u00e9p Gapi g\u1eedi th\u00f4ng b\u00e1o c\u0169ng nh\u01b0 thay \u0111\u1ed5i giao di\u1ec7n v\u00e0 \u00e2m thanh c\u1ee7a ch\u00fang.\n"
"", None))
        self.pushButton.setText(QCoreApplication.translate("settingUi", u"M\u1edf c\u00e0i \u0111\u1eb7t th\u00f4ng b\u00e1o Windows", None))
        self.label_10.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Xem tr\u01b0\u1edbc tin nh\u1eafn</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("settingUi", u"Hi\u1ec3n th\u1ecb b\u1ea3n xem tr\u01b0\u1edbc c\u1ee7a tin nh\u1eafn", None))
        self.label_11.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Cu\u1ed9c tr\u00f2 chuy\u1ec7n</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><a name=\"settings-widget-text-1\"/><span style=\" font-family:'-apple-system,BlinkMacSystemFont,Segoe UI,system-ui,Apple Color Emoji,Segoe UI Emoji,Segoe UI Web,sans-serif'; font-size:14px; color:#242424;\">T</span><span style=\" font-family:'-apple-system,BlinkMacSystemFont,Segoe UI,system-ui,Apple Color Emoji,Segoe UI Emoji,Segoe UI Web,sans-serif'; font-size:14px; color:#242424;\">in nh\u1eafn</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("settingUi", u"Bi\u1ec3u ng\u1eef v\u00e0 ngu\u1ed3n c\u1ea5p d\u1eef li\u1ec7u", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("settingUi", u"Ch\u1ec9 hi\u1ec3n th\u1ecb trong ngu\u1ed3n c\u1ea5p d\u1eef li\u1ec7u", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("settingUi", u"Bi\u1ec3u ng\u1eef v\u00e0 ngu\u1ed3n c\u1ea5p d\u1eef li\u1ec7u", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("settingUi", u"Ch\u1ec9 hi\u1ec3n th\u1ecb trong ngu\u1ed3n c\u1ea5p d\u1eef li\u1ec7u", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("settingUi", u"T\u1eaft", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("settingUi", u"Bi\u1ec3u ng\u1eef", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("settingUi", u"T\u1eaft", None))

        self.label_14.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-family:'-apple-system,BlinkMacSystemFont,Segoe UI,system-ui,Apple Color Emoji,Segoe UI Emoji,Segoe UI Web,sans-serif'; font-size:14px; color:#242424; background-color:#ffffff;\">L\u01b0\u1ee3t th\u00edch v\u00e0 t\u01b0\u01a1ng t\u00e1c</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><a name=\"settings-widget-text-0\"/><span style=\" font-family:'-apple-system,BlinkMacSystemFont,Segoe UI,system-ui,Apple Color Emoji,Segoe UI Emoji,Segoe UI Web,sans-serif'; font-size:14px; color:#242424;\">L</span><span style=\" font-family:'-apple-system,BlinkMacSystemFont,Segoe UI,system-ui,Apple Color Emoji,Segoe UI Emoji,Segoe UI Web,sans-serif'; font-size:14px; color:#242424;\">\u01b0\u1ee3t @\u0111\u1ec1 c\u1eadp</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Giao di\u1ec7n v\u00e0 tr\u1ee3 n\u0103ng</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:11pt;\">Ch\u1ee7 \u0111\u1ec1</span></p></body></html>", None))
        self.btn_light.setText("")
        self.label_18.setText(QCoreApplication.translate("settingUi", u"S\u00e1ng", None))
        self.light_radio.setText("")
        self.btn_dark.setText("")
        self.label_19.setText(QCoreApplication.translate("settingUi", u"T\u1ed1i", None))
        self.dark_radio.setText("")
        self.btn_hight_contrast.setText("")
        self.label_20.setText(QCoreApplication.translate("settingUi", u"T\u01b0\u01a1ng ph\u1ea3n cao", None))
        self.hight_contrast_radio.setText("")
        self.checkBox_5.setText(QCoreApplication.translate("settingUi", u"Theo ch\u1ee7 \u0111\u1ec1 c\u1ee7a h\u1ec7 \u0111i\u1ec1u h\u00e0nh", None))
        self.label_21.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:11pt;\">M\u1eadt \u0111\u1ed9 tin nh\u1eafn</span></p></body></html>", None))
        self.btn_comfy.setText("")
        self.label_22.setText(QCoreApplication.translate("settingUi", u"Tho\u00e1ng", None))
        self.comfy_radio.setText("")
        self.btn_compact.setText("")
        self.label_23.setText(QCoreApplication.translate("settingUi", u"G\u1ecdn", None))
        self.compact_radio.setText("")
        self.label_15.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">C\u00e0i \u0111\u1eb7t chung</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("settingUi", u"<a href=\"https://www.facebook.com/legal/terms\"style=\" font-size:11pt; text-decoration: underline; color:#000000;\">\u0110i\u1ec1u kho\u1ea3n d\u1ecbch v\u1ee5</a>", None))
        self.label_25.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><a href=\"https://www.facebook.com/legal/terms\"><span style=\" font-size:11pt; text-decoration: underline; color:#000000;\">Ch\u00ednh s\u00e1ch d\u1eef li\u1ec7u</span></a></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><a href=\"https://www.facebook.com/policies/cookies/\"><span style=\" font-size:11pt; text-decoration: underline; color:#000000;\">Ch\u00ednh s\u00e1ch cookie</span></a></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("settingUi", u"<html><head/><body><p><a href=\"https://www.facebook.com/about/basics\"><span style=\" font-size:11pt; text-decoration: underline; color:#000000;\">Quy\u1ec1n ri\u00eang t\u01b0 c\u01a1 b\u1ea3n</span></a></p></body></html>", None))
    # retranslateUi

