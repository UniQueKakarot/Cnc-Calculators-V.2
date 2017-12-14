import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import cuttingspeed
import spiral

class MainBody(BoxLayout):
    pass


class CncCalculators(App):
    def build(self):
        return MainBody()


CncCalculators().run()