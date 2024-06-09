# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tooltip.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(220, 30)
        Form.setMinimumSize(QSize(220, 30))
        self.label_layout = QVBoxLayout(Form)
        self.label_layout.setSpacing(0)
        self.label_layout.setObjectName(u"label_layout")
        self.label_layout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {		\n"
"	background-color: rgb(12, 12, 13);	\n"
"	color: rgb(230, 230, 230);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	border-radius: 8px;\n"
"}")

        self.label_layout.addWidget(self.label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"ToolTip", None))
    # retranslateUi

