import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'resizable', False)

import cuttingspeed
import spiral
import ra

class MainBody(BoxLayout):
    pass


class CncCalculators(App):
    def build(self):
        return MainBody()


CncCalculators().run()