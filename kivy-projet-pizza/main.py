 
from xmlrpc.client import Boolean

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import (BooleanProperty, NumericProperty, ObjectProperty,
                            StringProperty)
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

from http_client import HttpClient
from models import Pizza
from storage_manager import StorageManager


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    prix = NumericProperty()
    ingredients = StringProperty()
    vegetarienne = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        HttpClient().get_pizzas(self.on_server_data, self.on_server_error)
    
    def on_parent(self, widget, parent):
        pizza_dict = StorageManager().load_data("pizzas")
        if pizza_dict:
            self.recycleView.data = pizza_dict

    def on_server_data(self, pizza_dict):
        self.recycleView.data= pizza_dict
        StorageManager().save_data("pizzas", pizza_dict)
    
    def on_server_error(self, error):
        print("Erreur : "+error)
        self.error_str = error

class PizzaApp(App):
    pass


PizzaApp().run()

