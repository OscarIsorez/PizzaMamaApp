import json

class StorageManager:
    def load_data(self, data_name):
        file_name= self.get_data_name(data_name)
        try:
            file = open(file_name, "r")
            data = file.read()
            file.close()
        except:
            return None
        return json.loads(data)

    def save_data(self, data_name, data_content):
        file_name = self.get_data_name(data_name)
        data_str = json.dumps(data_content)
        file = open(file_name, "w")
        file.write(data_str)
        file.close()
        return json.loads(data_str)

    def get_data_name(self, data_name):
        return data_name + ".json"