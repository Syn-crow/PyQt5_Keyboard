from PyQt5.QtWidgets import QLineEdit
import keyboard as virtual_keyboard


class KLineEdit(QLineEdit):
    def __init__(self,*args, **kwargs):
        try:
            super(KLineEdit, self).__init__(*args, **kwargs)
       
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
