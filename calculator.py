import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    def calc(self,event):
        if event:
            try:
                self.display.text = str(eval(event))
            except:
                self.display.text = "Error"

    def undo(self):
        undo = self.display.text
        if len(undo):
            new_text = undo[:-1]
            self.display.text = (new_text)
class calculator(App):
    def build(self):
        return MyGridLayout()
calculator().run()
