# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main-window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1205, 780)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/image/image/logo-large.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"font-family:Segoe UI")
        self.style = QWidget(MainWindow)
        self.style.setObjectName(u"style")
        self.style.setCursor(QCursor(Qt.ArrowCursor))
        self.style.setStyleSheet(u"#style {\n"
"	background-color:#fff\n"
"}\n"
"QLineEdit {\n"
"	background: #FFFFFF;\n"
"	border-radius: 4px;\n"
"	color : #50565f;\n"
"	padding-left:16px;\n"
"	padding-right:16px;\n"
"	font-size:15px;\n"
"	border:1px solid transparent\n"
"    \n"
"}\n"
"QLineEdit:hover , QLineEdit:focus {\n"
"	border: 1px solid #e74725;    \n"
"}\n"
"QPushButton:pressed   {\n"
"	padding-bottom:1px\n"
"}\n"
"#user_setting {\n"
"	border-radius:22px;\n"
"	border:1px solid #D3D7DF\n"
"}\n"
"\n"
"#sidebar_menu QPushButton{\n"
"	border:none;\n"
"}\n"
"#sidebar {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QWidget #chat_sidebar {\n"
"	border-right:1px solid  #e0e0e0\n"
"}\n"
"\n"
"QWidget #chat_nav_user {\n"
"	border-bottom:1px solid  #e0e0e0\n"
"}\n"
"QWidget#chat_input {\n"
"	border-top:1px solid  #e0e0e0\n"
"}\n"
"QWidget #friend_chat_card{\n"
"	border-radius:4px;\n"
"}\n"
"#friend_chat_card:hover , #friend_chat_card:focus{\n"
"\n"
"	background-color:rgb(245, 245, 245);\n"
"}\n"
"\n"
"#sidebar_menu  QPushButton:hover {\n"
""
                        "	background-color:#f5f5f5\n"
"}\n"
"\n"
"")
        self.hboxLayout = QHBoxLayout(self.style)
        self.hboxLayout.setSpacing(0)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QWidget(self.style)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_content = QWidget(self.container)
        self.main_content.setObjectName(u"main_content")
        self.main_content.setFont(font)
        self.main_content.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.main_content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.main_content)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMaximumSize(QSize(80, 16777215))
        self.sidebar.setStyleSheet(u"#sibar {\n"
"	background-color: rgb(243, 108, 37);\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.sidebar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_menu = QWidget(self.sidebar)
        self.sidebar_menu.setObjectName(u"sidebar_menu")
        self.sidebar_menu.setMinimumSize(QSize(80, 0))
        self.sidebar_menu.setMaximumSize(QSize(80, 16777215))
        self.sidebar_menu.setStyleSheet(u"background-color: #f5f5f5;")
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_menu_content = QWidget(self.sidebar_menu)
        self.sidebar_menu_content.setObjectName(u"sidebar_menu_content")
        self.verticalLayout_3 = QVBoxLayout(self.sidebar_menu_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.chat_link = QPushButton(self.sidebar_menu_content)
        self.chat_link.setObjectName(u"chat_link")
        self.chat_link.setMinimumSize(QSize(80, 80))
        self.chat_link.setMaximumSize(QSize(80, 80))
        self.chat_link.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/icon-messages-active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chat_link.setIcon(icon1)
        self.chat_link.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.chat_link)

        self.member_link = QPushButton(self.sidebar_menu_content)
        self.member_link.setObjectName(u"member_link")
        self.member_link.setMinimumSize(QSize(80, 80))
        self.member_link.setMaximumSize(QSize(80, 80))
        self.member_link.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/icons8-member-active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.member_link.setIcon(icon2)
        self.member_link.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.member_link)

        self.todo_list_link = QPushButton(self.sidebar_menu_content)
        self.todo_list_link.setObjectName(u"todo_list_link")
        self.todo_list_link.setMinimumSize(QSize(80, 80))
        self.todo_list_link.setMaximumSize(QSize(80, 80))
        self.todo_list_link.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/icon-todo-list-active.png", QSize(), QIcon.Normal, QIcon.Off)
        self.todo_list_link.setIcon(icon3)
        self.todo_list_link.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.todo_list_link)


        self.verticalLayout_2.addWidget(self.sidebar_menu_content, 0, Qt.AlignTop)

        self.user_btn = QPushButton(self.sidebar_menu)
        self.user_btn.setObjectName(u"user_btn")
        self.user_btn.setMinimumSize(QSize(80, 80))
        self.user_btn.setMaximumSize(QSize(80, 80))
        self.user_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.user_btn.setStyleSheet(u"\n"
"border-radius:40px\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/image/image/avt-df.png", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon4)
        self.user_btn.setIconSize(QSize(44, 44))

        self.verticalLayout_2.addWidget(self.user_btn)


        self.horizontalLayout.addWidget(self.sidebar_menu)


        self.horizontalLayout_4.addWidget(self.sidebar)

        self.stackedWidget = QStackedWidget(self.main_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.chat_page = QWidget()
        self.chat_page.setObjectName(u"chat_page")
        self.horizontalLayout_5 = QHBoxLayout(self.chat_page)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.chat_container = QWidget(self.chat_page)
        self.chat_container.setObjectName(u"chat_container")
        self.chat_container.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_3 = QHBoxLayout(self.chat_container)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.chat_sidebar = QWidget(self.chat_container)
        self.chat_sidebar.setObjectName(u"chat_sidebar")
        self.chat_sidebar.setMaximumSize(QSize(300, 16777215))
        self.chat_sidebar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_5 = QVBoxLayout(self.chat_sidebar)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 16, 12, 0)
        self.chat_sidebar_top = QWidget(self.chat_sidebar)
        self.chat_sidebar_top.setObjectName(u"chat_sidebar_top")
        self.chat_sidebar_top.setMaximumSize(QSize(16777215, 99))
        self.chat_sidebar_top.setStyleSheet(u"border-bottom:")
        self.verticalLayout_4 = QVBoxLayout(self.chat_sidebar_top)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 0, 0, 0)
        self.frame = QFrame(self.chat_sidebar_top)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.chat__sidebar_title = QLabel(self.frame)
        self.chat__sidebar_title.setObjectName(u"chat__sidebar_title")
        self.chat__sidebar_title.setFont(font)

        self.horizontalLayout_2.addWidget(self.chat__sidebar_title)

        self.on_new_message = QPushButton(self.frame)
        self.on_new_message.setObjectName(u"on_new_message")
        self.on_new_message.setMinimumSize(QSize(36, 36))
        self.on_new_message.setMaximumSize(QSize(36, 36))
        self.on_new_message.setStyleSheet(u"border:none;\n"
"border-radius:44px")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/icons8-plus-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.on_new_message.setIcon(icon5)
        self.on_new_message.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.on_new_message)


        self.verticalLayout_4.addWidget(self.frame)

        self.search_input = QLineEdit(self.chat_sidebar_top)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setMinimumSize(QSize(0, 44))
        self.search_input.setStyleSheet(u"border-radius: 22px;\n"
"background-color:#f2f2f2;")

        self.verticalLayout_4.addWidget(self.search_input)


        self.verticalLayout_5.addWidget(self.chat_sidebar_top)

        self.user_chat_view = QWidget(self.chat_sidebar)
        self.user_chat_view.setObjectName(u"user_chat_view")
        self.verticalLayout_10 = QVBoxLayout(self.user_chat_view)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(12, 0, 0, 0)
        self.friend_chat_card = QWidget(self.user_chat_view)
        self.friend_chat_card.setObjectName(u"friend_chat_card")
        self.friend_chat_card.setMinimumSize(QSize(0, 64))
        self.friend_chat_card.setMaximumSize(QSize(16777215, 64))
        self.friend_chat_card.setCursor(QCursor(Qt.PointingHandCursor))
        self.friend_chat_card.setFocusPolicy(Qt.ClickFocus)
        self.friend_chat_card.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.friend_chat_card)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(12, 0, 12, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(0)
        self.friend_avt = QLabel(self.friend_chat_card)
        self.friend_avt.setObjectName(u"friend_avt")
        self.friend_avt.setStyleSheet(u"border-image:url(:/image/image/avt.jpg);\n"
"max-width:44px;\n"
"max-height:44px;\n"
"min-width:44px;\n"
"min-height:44px;\n"
"border-radius:22px")

        self.gridLayout.addWidget(self.friend_avt, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.friend_chat_card)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color:transparent")
        self.verticalLayout_6 = QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.friend_name = QLabel(self.widget_3)
        self.friend_name.setObjectName(u"friend_name")
        self.friend_name.setStyleSheet(u"font-size:16px;\n"
"font-weight:500;\n"
"background-color:transparent")

        self.verticalLayout_6.addWidget(self.friend_name)

        self.friend_last_message = QLabel(self.widget_3)
        self.friend_last_message.setObjectName(u"friend_last_message")
        self.friend_last_message.setStyleSheet(u"color:#65676b;\n"
"font-size:12px;\n"
"background-color:transparent")
        self.friend_last_message.setTextFormat(Qt.AutoText)
        self.friend_last_message.setScaledContents(False)
        self.friend_last_message.setWordWrap(False)
        self.friend_last_message.setIndent(-1)
        self.friend_last_message.setOpenExternalLinks(False)
        self.friend_last_message.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_6.addWidget(self.friend_last_message)


        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)

        self.friend_time_last_message = QLabel(self.friend_chat_card)
        self.friend_time_last_message.setObjectName(u"friend_time_last_message")
        self.friend_time_last_message.setStyleSheet(u"color:#65676b;\n"
"font-size:12px;\n"
"")

        self.gridLayout.addWidget(self.friend_time_last_message, 0, 2, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout)


        self.verticalLayout_10.addWidget(self.friend_chat_card)

        self.widget_2 = QWidget(self.user_chat_view)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")

        self.verticalLayout_10.addWidget(self.widget_2)


        self.verticalLayout_5.addWidget(self.user_chat_view)


        self.horizontalLayout_3.addWidget(self.chat_sidebar)

        self.chat_content = QWidget(self.chat_container)
        self.chat_content.setObjectName(u"chat_content")
        self.chat_content.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.chat_content)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.chat_nav_user = QWidget(self.chat_content)
        self.chat_nav_user.setObjectName(u"chat_nav_user")
        self.chat_nav_user.setMinimumSize(QSize(0, 80))
        self.chat_nav_user.setMaximumSize(QSize(16777215, 80))
        self.chat_nav_user.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.chat_nav_user)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.friend_chat_acrtive = QWidget(self.chat_nav_user)
        self.friend_chat_acrtive.setObjectName(u"friend_chat_acrtive")
        self.friend_chat_acrtive.setMaximumSize(QSize(16777215, 56))
        self.horizontalLayout_7 = QHBoxLayout(self.friend_chat_acrtive)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.friend_avt_active = QLabel(self.friend_chat_acrtive)
        self.friend_avt_active.setObjectName(u"friend_avt_active")
        self.friend_avt_active.setMinimumSize(QSize(32, 32))
        self.friend_avt_active.setMaximumSize(QSize(32, 32))
        self.friend_avt_active.setStyleSheet(u"border-image: url(:/image/image/avt.jpg);\n"
"max-width:32px;\n"
"max-height:32px;\n"
"min-width:32px;\n"
"min-height:32px;\n"
"border-radius:16px")

        self.horizontalLayout_7.addWidget(self.friend_avt_active)

        self.frame_2 = QFrame(self.friend_chat_acrtive)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.friend_chat_name_active = QLabel(self.frame_2)
        self.friend_chat_name_active.setObjectName(u"friend_chat_name_active")
        self.friend_chat_name_active.setStyleSheet(u"font-size:16px;\n"
"font-weight:500;")

        self.verticalLayout_8.addWidget(self.friend_chat_name_active)

        self.friend_on_active = QLabel(self.frame_2)
        self.friend_on_active.setObjectName(u"friend_on_active")
        self.friend_on_active.setStyleSheet(u"color:#65676b;\n"
"font-size:12px")
        self.friend_on_active.setTextFormat(Qt.AutoText)
        self.friend_on_active.setScaledContents(True)
        self.friend_on_active.setWordWrap(False)
        self.friend_on_active.setIndent(-1)
        self.friend_on_active.setOpenExternalLinks(False)
        self.friend_on_active.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_8.addWidget(self.friend_on_active)


        self.horizontalLayout_7.addWidget(self.frame_2)


        self.horizontalLayout_12.addWidget(self.friend_chat_acrtive)

        self.frame_3 = QFrame(self.chat_nav_user)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QPushButton {\n"
"	border-radius:26px;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:#f5f5f5\n"
"}\n"
"")
        self.horizontalLayout_13 = QHBoxLayout(self.widget)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.on_phone_call = QPushButton(self.widget)
        self.on_phone_call.setObjectName(u"on_phone_call")
        self.on_phone_call.setMinimumSize(QSize(52, 52))
        self.on_phone_call.setMaximumSize(QSize(52, 52))
        self.on_phone_call.setCursor(QCursor(Qt.PointingHandCursor))
        self.on_phone_call.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/icon-phone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.on_phone_call.setIcon(icon6)
        self.on_phone_call.setIconSize(QSize(32, 32))

        self.horizontalLayout_13.addWidget(self.on_phone_call)

        self.on_video_call = QPushButton(self.widget)
        self.on_video_call.setObjectName(u"on_video_call")
        self.on_video_call.setMinimumSize(QSize(52, 52))
        self.on_video_call.setMaximumSize(QSize(52, 52))
        self.on_video_call.setCursor(QCursor(Qt.PointingHandCursor))
        self.on_video_call.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/icon-video-call.png", QSize(), QIcon.Normal, QIcon.Off)
        self.on_video_call.setIcon(icon7)
        self.on_video_call.setIconSize(QSize(32, 32))

        self.horizontalLayout_13.addWidget(self.on_video_call)

        self.on_info_chat = QPushButton(self.widget)
        self.on_info_chat.setObjectName(u"on_info_chat")
        self.on_info_chat.setMinimumSize(QSize(52, 52))
        self.on_info_chat.setMaximumSize(QSize(52, 52))
        self.on_info_chat.setCursor(QCursor(Qt.PointingHandCursor))
        self.on_info_chat.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/icon-info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.on_info_chat.setIcon(icon8)
        self.on_info_chat.setIconSize(QSize(32, 32))

        self.horizontalLayout_13.addWidget(self.on_info_chat)


        self.horizontalLayout_8.addWidget(self.widget, 0, Qt.AlignRight)


        self.horizontalLayout_12.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.chat_nav_user)

        self.chat_main_content = QWidget(self.chat_content)
        self.chat_main_content.setObjectName(u"chat_main_content")
        self.widget_4 = QWidget(self.chat_main_content)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 70, 801, 81))
        self.friend_avt_2 = QLabel(self.widget_4)
        self.friend_avt_2.setObjectName(u"friend_avt_2")
        self.friend_avt_2.setGeometry(QRect(10, 45, 32, 32))
        self.friend_avt_2.setMinimumSize(QSize(32, 32))
        self.friend_avt_2.setMaximumSize(QSize(32, 32))
        self.friend_avt_2.setStyleSheet(u"border-image: url(:/image/image/avt.jpg);\n"
"max-width:32px;\n"
"max-height:32px;\n"
"min-width:32px;\n"
"min-height:32px;\n"
"border-radius:16px")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 0, 71, 36))
        self.label.setStyleSheet(u"padding:4px 12px;\n"
"background:#fff;\n"
"border:1px solid #c4c4c4;\n"
"border-radius:18px;\n"
"font-size:12px")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 40, 101, 36))
        self.label_2.setStyleSheet(u"padding:4px 12px;\n"
"background:#fff;\n"
"border:1px solid #c4c4c4;\n"
"border-radius:18px;\n"
"font-size:12px")
        self.widget_5 = QWidget(self.chat_main_content)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 200, 801, 371))
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(720, 0, 70, 36))
        self.label_5.setStyleSheet(u"padding:4px 12px;\n"
"background:#f5f5f5;\n"
"border-radius:16px;\n"
"font-size:12px")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(710, 40, 80, 36))
        self.label_6.setStyleSheet(u"padding:4px 12px;\n"
"background:#f5f5f5;\n"
"border-radius:16px;\n"
"font-size:12px")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(315, 80, 470, 290))
        self.label_7.setStyleSheet(u"background-image: url(:/image/image/auth-apppng.png);\n"
"\n"
"border-radius:16px")
        self.friend_time_last_message_2 = QLabel(self.chat_main_content)
        self.friend_time_last_message_2.setObjectName(u"friend_time_last_message_2")
        self.friend_time_last_message_2.setGeometry(QRect(10, 30, 791, 31))
        self.friend_time_last_message_2.setStyleSheet(u"color:#65676b;\n"
"font-size:12px;\n"
"")
        self.friend_time_last_message_2.setAlignment(Qt.AlignCenter)
        self.friend_time_last_message_3 = QLabel(self.chat_main_content)
        self.friend_time_last_message_3.setObjectName(u"friend_time_last_message_3")
        self.friend_time_last_message_3.setGeometry(QRect(10, 160, 791, 31))
        self.friend_time_last_message_3.setStyleSheet(u"color:#65676b;\n"
"font-size:12px;\n"
"")
        self.friend_time_last_message_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.chat_main_content)

        self.chat_input = QWidget(self.chat_content)
        self.chat_input.setObjectName(u"chat_input")
        self.chat_input.setMinimumSize(QSize(0, 80))
        self.chat_input.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_9 = QHBoxLayout(self.chat_input)
        self.horizontalLayout_9.setSpacing(12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(12, 0, 12, 0)
        self.on_send_heart = QPushButton(self.chat_input)
        self.on_send_heart.setObjectName(u"on_send_heart")
        self.on_send_heart.setMinimumSize(QSize(44, 44))
        self.on_send_heart.setMaximumSize(QSize(44, 44))
        self.on_send_heart.setCursor(QCursor(Qt.PointingHandCursor))
        self.on_send_heart.setStyleSheet(u"border:none;\n"
"border-radius:44px")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/icons8-heart-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.on_send_heart.setIcon(icon9)
        self.on_send_heart.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.on_send_heart)

        self.on_send_image = QPushButton(self.chat_input)
        self.on_send_image.setObjectName(u"on_send_image")
        self.on_send_image.setMinimumSize(QSize(44, 44))
        self.on_send_image.setMaximumSize(QSize(44, 44))
        self.on_send_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.on_send_image.setStyleSheet(u"border:none;\n"
"border-radius:44px")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icon/icons8-image-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.on_send_image.setIcon(icon10)
        self.on_send_image.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.on_send_image)

        self.chat_input_input = QLineEdit(self.chat_input)
        self.chat_input_input.setObjectName(u"chat_input_input")
        self.chat_input_input.setMinimumSize(QSize(0, 44))
        self.chat_input_input.setStyleSheet(u"border-radius: 22px;\n"
"background-color:#f2f2f2;")

        self.horizontalLayout_9.addWidget(self.chat_input_input)

        self.on_send_message = QPushButton(self.chat_input)
        self.on_send_message.setObjectName(u"on_send_message")
        self.on_send_message.setMinimumSize(QSize(44, 44))
        self.on_send_message.setMaximumSize(QSize(44, 44))
        self.on_send_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.on_send_message.setStyleSheet(u"border:none;\n"
"border-radius:44px")
        icon11 = QIcon()
        icon11.addFile(u":/icon/icon/icons8-enter-mac-key-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.on_send_message.setIcon(icon11)
        self.on_send_message.setIconSize(QSize(36, 36))

        self.horizontalLayout_9.addWidget(self.on_send_message)


        self.verticalLayout_7.addWidget(self.chat_input)


        self.horizontalLayout_3.addWidget(self.chat_content)


        self.horizontalLayout_5.addWidget(self.chat_container)

        self.stackedWidget.addWidget(self.chat_page)
        self.member_page = QWidget()
        self.member_page.setObjectName(u"member_page")
        self.horizontalLayout_11 = QHBoxLayout(self.member_page)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.member_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.member_page)
        self.todo_pager = QWidget()
        self.todo_pager.setObjectName(u"todo_pager")
        self.horizontalLayout_10 = QHBoxLayout(self.todo_pager)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(self.todo_pager)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.todo_pager)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_content)


        self.hboxLayout.addWidget(self.container)

        MainWindow.setCentralWidget(self.style)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GapiChat", None))
        self.chat_link.setText("")
        self.member_link.setText("")
        self.todo_list_link.setText("")
        self.user_btn.setText("")
        self.chat__sidebar_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Chat</span></p></body></html>", None))
        self.on_new_message.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm (Ctrl + K)", None))
        self.friend_avt.setText("")
        self.friend_name.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ea1i T\u01b0\u1edbng Gi\u00e1p", None))
        self.friend_last_message.setText(QCoreApplication.translate("MainWindow", u"H\u00f4m nay l\u00e0 th\u1ee9 m\u1ea5y ch\u1eafc ch\u1eafn l\u00e0 th\u1ee9 2", None))
        self.friend_time_last_message.setText(QCoreApplication.translate("MainWindow", u"2 ng\u00e0y", None))
        self.friend_avt_active.setText("")
        self.friend_chat_name_active.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ea1i T\u01b0\u1edbng Gi\u00e1p", None))
        self.friend_on_active.setText(QCoreApplication.translate("MainWindow", u"Ho\u1ea1t \u0111\u1ed9ng 6p tr\u01b0\u1edbc", None))
        self.on_phone_call.setText("")
        self.on_video_call.setText("")
        self.on_info_chat.setText("")
        self.friend_avt_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"How are you?", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"I'm fine", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"And you?", None))
        self.label_7.setText("")
        self.friend_time_last_message_2.setText(QCoreApplication.translate("MainWindow", u"Th\u00e1ng 7 12, 2022 7:23 chi\u1ec1u", None))
        self.friend_time_last_message_3.setText(QCoreApplication.translate("MainWindow", u"Th\u00e1ng 7 16, 2022 4:12 s\u00e1ng", None))
        self.on_send_heart.setText("")
        self.on_send_image.setText("")
        self.chat_input_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm (Ctrl + K)", None))
        self.on_send_message.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:72pt; font-weight:600; color:#ff5500;\">MEMBER PAGE</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:72pt; font-weight:600; color:#ff5500;\">TODO PAGE</span></p></body></html>", None))
    # retranslateUi

