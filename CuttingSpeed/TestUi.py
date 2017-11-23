import kivy
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import StringProperty
kivy.require("1.10.0")


class MainFrame(TabbedPanel):

    res_speed = StringProperty()
    res_feed = StringProperty()

    def calc(self):

        spindel_rpm = self.spindel()
        mill_feed = self.feed(spindel_rpm)

        spindel_rpm = round(spindel_rpm, 0)
        mill_feed = round(mill_feed, 0)

        spindel_rpm = int(spindel_rpm)
        mill_feed = int(mill_feed)

        self.results(spindel_rpm, mill_feed)

    def spindel(self):
        try:

            cs = self.txt1.text
            cs = cs.replace(',', '.')
            cs = float(cs)

            md = self.txt2.text
            md = md.replace(',', '.')
            md = float(md)

            rpm = (cs * 1000) / (3.14 * md)
        except ValueError:
            rpm = 0
            print("Could not calculate RPM!")

        return rpm

    def feed(self, spindel_rpm):
        try:

            nt = self.txt3.text
            nt = nt.replace(',', '.')
            nt = float(nt)

            ft = self.txt4.text
            ft = ft.replace(',', '.')
            ft = float(ft)

            feed_rate = ft * spindel_rpm * nt

        except ValueError:
            feed_rate = 0
            print("Could not calculate feedrate!")

        return feed_rate

    def feedback(self, value):
        if value == 1:

            self.popup1.open()

        else:

            self.popup2.open()

    def results(self, speed, feed):

        self.res_speed = str(speed)
        self.res_feed = str(feed)

        pass


class SimpleKivy(App):
    def build(self):
        return MainFrame()


test = SimpleKivy()
test.run()
