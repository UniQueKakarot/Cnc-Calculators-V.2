""" This is the entry module to the Cnc-Calculator GUI application """

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()

from Moduler import cuttingspeed

#Builder.load_file("CncCalculators.kv")


class MainBody(BoxLayout):
    """ Main body for the GUI application """
    pass


class CncCalculators(App):
    """ Root class for the GUI application """
    def build(self):
        #self.load_kv("CncCalculators.kv")
        return MainBody()

if __name__ == "__main__":
    CncCalculators().run()
