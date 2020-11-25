import kivy
import traceback
import youtube_dl
from kivy.app import App
import subprocess
from kivy.uix.gridlayout import GridLayout

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
import pafy
import webbrowser
Builder.load_file('test.kv')


class MyGrid(Widget):
    
    name = ObjectProperty(None)
    

    def btn(self):

        
        import webbrowser
        webbrowser.open("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dtr%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=tr&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
       
        
    
   


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue" 
        return MyGrid()


if __name__ == "__main__":
    MainApp().run()