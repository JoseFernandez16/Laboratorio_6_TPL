from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
 
class Pestaña(Popup):
    pass
 
 
class MyRelativeLayout(RelativeLayout):
 
    def open_popup(self):
        pops = Pestaña()
        pops.open()
 

class PopUpWindow(App):
    def build(self):
 
        return MyRelativeLayout()
 
if __name__ == "__main__":
    window = PopUpWindow()
    window.run()