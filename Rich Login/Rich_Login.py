# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rich_Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(405, 284)
        Form.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(118, 80, 163, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit::hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QLineEdit::focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 56);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 148, 163, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit::hover {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QLineEdit::focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 56);\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(164, 54, 72, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(161, 161, 161);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(164, 124, 67, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(161, 161, 161);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Username"))
        self.label_2.setText(_translate("Form", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
