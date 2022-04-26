from kivy.network.urlrequest import UrlRequest
import json
class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = "https://oscarpizzamama.herokuapp.com/api/Get_Pizzas"


        def data_received(req, result):
            data = json.loads(result)
            pizza_dict = []
            for dico in data:
                pizza_dict.append(dico["fields"])
            if on_complete:
                on_complete(pizza_dict)

        def data_error(req, error):
            if on_error:
                on_error("Erreur : "+str(error))
        def data_failure(req, result):
            print("Data failure")
            if on_error:
                on_error("Erreur serveur : "+str(req.resp_status))

        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)