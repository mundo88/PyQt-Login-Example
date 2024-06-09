from ..ui.widgets.dropdownMenuUi import Ui_Form

from PyQt5 import QtWidgets,QtGui,QtCore


class UserDropdownMenu(QtWidgets.QWidget,Ui_Form):
    def __init__(self, parent=None,shadow=True): 
        super(UserDropdownMenu, self).__init__(parent)
        self.parent = parent
        self.shadow = shadow
                
        self.setupUi(self)
        self.initMenu()
        self.setVisible(False)
        self.setStyleSheet("border-radius:4px")

    def initMenu(self):
        self.setObjectName("form_user_dropdown")        

        self.menu_y = self.parent.height() - self.height() - 44 
        self.menu_x = 44
        self.move(self.menu_x, self.menu_y)
        
        if self.shadow:
            self.setShadow()
        

    def setShadow(self):
        self.shadowEffect = QtWidgets.QGraphicsDropShadowEffect(
            self,
            blurRadius=16,
            color=QtGui.QColor(180, 180, 180),
            offset=QtCore.QPointF(0, 0)
            )
        self.setGraphicsEffect(self.shadowEffect)


    def onShow(self):
        self.setVisible(not self.isVisible())