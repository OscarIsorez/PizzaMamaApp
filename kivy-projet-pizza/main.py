 
from xmlrpc.client import Boolean
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.lang import Builder
from models import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    prix = NumericProperty()
    ingredients = StringProperty()
    vegetarienne = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza("4 fromages", "brie, bleu,mozzarela, emmental", 10.6, True),
            Pizza("3 fromages", "brie, bleu,mozzarela, emmental", 10.6, True),
            Pizza("2 fromages", "brie, bleu,mozzarela, emmental", 10.6, True)
            ]


    def on_parent(self, widget, parent):
        self.recycleView.data = [pizza.get_dictionnary() for pizza in self.pizzas] 

class PizzaApp(App):
    pass


PizzaApp().run()

