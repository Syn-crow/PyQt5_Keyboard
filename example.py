import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


from LineEdit import KLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line1 = KLineEdit(self)
        self.line2 = KLineEdit(self)

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
