
import os
import yaml

CONFIG_FILE = os.environ.get('DARCHMAN_CONFIG', default='./darchman.yaml')

class Config:
    def __init__(self, config_file=CONFIG_FILE):
        with open(CONFIG_FILE) as config_file:
            config_data = yaml.safe_load(config_file)
        self.config_data = config_data
    
    def get_config_data(self):
        return self.config_data

config = Config()