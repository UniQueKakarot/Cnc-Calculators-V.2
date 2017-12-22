import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()

import cuttingspeed
import spiral
import ra

class MainBody(BoxLayout):
    pass


class CncCalculators(App):
    def build(self):
        return MainBody()


CncCalculators().run()