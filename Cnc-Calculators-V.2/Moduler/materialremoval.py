from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

from Moduler.customwidgets import MyLabel

Builder.load_string(
"""
<MaterialRemoval>:
    cols: 1
    padding: 10
    spacing: 7
    
    # text input id's
    ap: ap
    ae: ae
    feed: feed
    
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Depth of cut: "
            
        TextInput:
            id: ap
            hint_text: "ap"
            multiline: False
            write_tab: False
            on_text_validate: root.calc()
            
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Width of cut: "
            
        TextInput:
            id: ae
            hint_text: "ae"
            multiline: False
            write_tab: False
            on_text_validate: root.calc()
            
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Feedrate: "
            
        TextInput:
            id: feed
            hint_text: "mm/m"
            multiline: False
            write_tab: False
            on_text_validate: root.calc()
            
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Button:
            text: "Calculate"
            on_press: root.calc()
            
    Label:
    
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        MyLabel:
            text: "Material Removal Rate:"
            font_size: 20
            bcolor: [1, 1, 1, 0.15]
            
        MyLabel:
            text: root.res_mrr
            font_size: 20
            bcolor: [1, 1, 1, 0.15]


"""
)


class MaterialRemoval(GridLayout):
    
    res_mrr = StringProperty()
    
    def calc(self):
        
        result = self.mrrcalc()
        self.results(result)
    
    def mrrcalc(self):
        
        """ Getting the values and doing the calculation """
        
        try:
            ap = self.ap.text
            ap = ap.replace(',', '.')
            ap = float(ap)
        except ValueError:
            pass
        
        try:
            ae = self.ae.text
            ae = ae.replace(',', '.')
            ae = float(ae)
        except ValueError:
            pass
        
        try:
            feed = self.feed.text
            feed = feed.replace(',', '.')
            feed = float(feed)
        except ValueError:
            pass
        
        # doing the calculation
        try:
            mrr = (ap * ae * feed) / 1000
        except (ValueError, TypeError):
            mrr = "Please input values"
        
        return mrr

    def results(self, result):
        
        """ Updating the UI label with the result """
        
        result = str(result)
        result = (result + ' cm³/min')
        
        self.res_mrr = str(result)