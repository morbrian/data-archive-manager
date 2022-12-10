import requests

class GenericAdapter:
    def __init__(self, service_name, service_url):
        self.service_name = service_name
        self.service_url = service_url
    
    def export_all(self):
        response = requests.get(self.service_url)
        response_json = response.json()
        return response_json
    
    def store_all(self, data):
        response = requests.put(self.service_url, json=data)
        response_json = response.json()
        return response_json
    
    def get(self, id):
        url_format = '{}/{}'.format(self.service_url, id)
        response = requests.get(url_format)
        response_json = response.json()
        return response_json
    
    def put(self, id, data):
        url_format = '{}/{}'.format(self.service_url, id)
        response = requests.put(url_format, json=data)
        response_json = response.json()
        return response_json
    
    def delete(self, id):
        url_format = '{}/{}'.format(self.service_url, id)
        response = requests.delete(url_format)
        response_json = response.json()
        return response_json
