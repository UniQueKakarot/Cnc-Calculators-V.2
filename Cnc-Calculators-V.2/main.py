""" This is the entry module to the Cnc-Calculator GUI application """

#import os
#os.environ["KIVY_VIDEO"] = "ffpyplayer"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.lang import Builder

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()

from Moduler import cuttingspeed


class MainBody(BoxLayout):
    """ Main body for the GUI application """
    pass


class CncCalculators(App):
    """ Root class for the GUI application """
    def build(self):
        Builder.load_file("CncCalculators.kv")
        return MainBody()


CncCalculators().run()
