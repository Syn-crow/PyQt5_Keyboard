import xml.etree.ElementTree as ET
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Key(QPushButton):
    
    def __init__(self, text, command,sText,sCommand,signal):
        super(Key, self).__init__()
        #s corespond au parametre une fois 'shifted'
        self.signal = signal
        self.text = text
        self.sText = sText
        self.command = command
        self.sCommand = sCommand
    
        self.shifted = False
        
        self.setCommand(self.command,self.text)
        self.setText(self.text)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def changeShift(self):
        self.shifted = not self.shifted
        if self.shifted == True:
            self.setText(self.sText)
            self.setCommand(self.sCommand,self.sText)
        else:
            try:
                self.setText(self.text)
                self.setCommand(self.command,self.text)
                print('done deshift')
            except Exception as e:
                print(e)

    def setCommand(self,command,text):
        try:
            if isinstance(command,str):
                try:
                    self.clicked.disconnect() 
                except Exception:
                    pass
                self.clicked.connect(lambda: self.signal.emit(text))
            else:
                try:
                    self.clicked.disconnect() 
                except Exception:
                    pass
                self.clicked.connect(command)
        except Exception as e:
            print(e)

class VirtualKeyboard(QWidget):
    
    #sigKeyButtonClicked = pyqtSignal() code original contient cette ligne, n'est jamais utilisee. celle utilisee appartient a une autre classe
    sigInputString = pyqtSignal(str)

    def __init__(self, layout='azerty.xml'):
        super(VirtualKeyboard, self).__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.setFocusPolicy(Qt.ClickFocus)

        self.setGeometry(200,400,900,500)

        self.globalLayout = QVBoxLayout(self)
        self.importKeyboardLayout(layout)

    def importKeyboardLayout(self,layout):
        ''' 
        build the keyboard using external layout file, both display and command
        input: Layout , the name of the .xml file contaigning the layout it should be formated as follow:
        <row>
          <key>
              <default display="ヂ" />                
          </key>
          <key>
              <default display="Ӫ" />                
          </key>
          <key width="1500">
              <default display="Ω" />                
          </key>
          <space width="1500" />
          <key fill="true">
              <default display="⠿" />                
          </key>
        </row>

        return: nothing
        '''      
        tree = ET.parse(layout)
        root = tree.getroot()
        self.rows = []
        for child in root[1]:
            if child.tag == 'row':
                rowi = QHBoxLayout()
                for grandChild in child:
                    if grandChild.tag == 'key':
                        display = grandChild.find('default').get('display')
                        if grandChild.find('default').get('action')!=None:
                            command = 'Command not supported'
                            if grandChild.find('default').get('action') == 'modifier:shift':
                                command = self.shift
                            print(grandChild.find('default').get('action'))
                        else:
                            command = display
                        
                        if grandChild.find('shifted') == None:
                            sdisplay = display
                            scommand = command
                        else:
                            sdisplay = grandChild.find('shifted').get('display')
                            scommand = grandChild.find('shifted').get('action')
                            if scommand == None:
                                scommand = sdisplay
                        
                        keyi = Key(display,command,sdisplay,scommand,self.sigInputString)
                        rowi.addWidget(keyi)
                self.globalLayout.addLayout(rowi)
                    
                    
    def leaveEvent(self, event):
        print("Mouse Left")
        self.hide()
        super(VirtualKeyboard, self).enterEvent(event)

    def shift(self):
        try:
            index = self.globalLayout.count()
            while(index >= 1):
                rowi = self.globalLayout.itemAt(index-1).layout()
                index_row = rowi.count()
                while(index_row >= 1):
                    rowi.itemAt(index_row-1).widget().changeShift()
                    index_row-=1
                index -=1
        except Exception as e:
            print(e)

    

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    win = VirtualKeyboard()
    win.show()
    app.exec_()        
        
