import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

import keyboard2 as virtual_keyboard

class MyLineEdit(QLineEdit):
    def __init__(self,*args, **kwargs):
        try:
            super(MyLineEdit, self).__init__(*args, **kwargs)
       
            self.keyboard = virtual_keyboard.VirtualKeyboard()
            self.keyboard.sigInputString.connect(self.updateTXT)
            self.content = self.text()

        except Exception as e:
            print(e)
    def focusInEvent(self, event):
        print('focus in event')
        # do custom stuff
        self.parent().setFocus()
        self.keyboard.show()
        super(MyLineEdit, self).focusInEvent(event)
    def updateTXT(self,text):
        self.content+=text
        self.setText(self.content)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line1 = MyLineEdit(self)
        self.line2 = MyLineEdit(self)

        self.line1.move(80, 20)
        self.line1.resize(200, 32)
        self.nameLabel.move(20, 20)

        self.line1.move(80, 80)
        self.line1.resize(200, 32)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
