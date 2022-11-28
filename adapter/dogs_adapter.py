import requests

dev_base_url = 'http://localhost:5000/dogs'

class DogsAdapter:
    def __init__(self, base_url=dev_base_url):
        self.service_name = 'dogs'
        self.base_url = base_url
    
    def export_all(self):
        response = requests.get(self.base_url)
        response_json = response.json()
        return response_json
    
    def store_all(self, data):
        response = requests.put(self.base_url, json=data)
        response_json = response.json()
        return response_json
    
    def get(self, id):
        url_format = '{}/{}'.format(self.base_url, id)
        response = requests.get(url_format)
        response_json = response.json()
        return response_json
    
    def put(self, id, data):
        url_format = '{}/{}'.format(self.base_url, id)
        response = requests.put(url_format, json=data)
        response_json = response.json()
        return response_json
    
    def delete(self, id):
        url_format = '{}/{}'.format(self.base_url, id)
        response = requests.delete(url_format)
        response_json = response.json()
        return response_json
