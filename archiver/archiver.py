import json
import pathlib
from datetime import datetime
import uuid
import hashlib

class Archiver:
    def __init__(self, service_name, base_folder='./mydata'):
        self.service_name=service_name
        self.base_folder='{}/{}'.format(base_folder, service_name)
        pathlib.Path(self.base_folder).mkdir(parents=True, exist_ok=True)

    def get_data_hash(self, data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    def get_base_name(self, stamp):
        return '{}_{}'.format(self.service_name, stamp)

    def get_data_filename(self, base_name):
        return '{}/{}.json'.format(self.base_folder, base_name)

    def get_meta_filename(self, base_name):
        return '{}/{}.meta'.format(self.base_folder, base_name)

    def build_meta(self, data):
        stamp = datetime.now().isoformat()
        return {
            'uuid': str(uuid.uuid4()),
            'type': self.service_name,
            'datetime': stamp,
            'base_name': self.get_base_name(stamp.replace(':', '-')),
            'data_hash': self.get_data_hash(data)
        }

    def write_data_str(self, path, data_str):
        """data_str is the string form of the data, not the raw json object"""
        path.write_text(data_str, encoding='UTF-8')
        # with path.open('w', encoding='UTF-8') as target:
        #     target.write(data_str)

    def read_data_str(self, path):
        return path.read_text(encoding='UTF-8')
        # with path.open(encoding='UTF-8') as source:
        #     return source.read_text()

    def store_data(self, data):
        data_str = '{}\n'.format(json.dumps(data))
        meta = self.build_meta(data_str)
        base_name = meta['base_name']

        data_filename = self.get_data_filename(base_name)
        self.write_data_str(pathlib.Path(data_filename), data_str)

        meta_filename = self.get_meta_filename(base_name)
        meta_str = '{}\n'.format(json.dumps(meta))
        self.write_data_str(pathlib.Path(meta_filename), meta_str)

        return meta
    
    def retrieve_data(self, uuid):
        return 'TODO'
    
    def list_meta(self):
        all_meta = pathlib.Path(self.base_folder).glob('*.meta')
        meta_files = [f for f in all_meta if f.is_file()]
        meta_contents = [json.loads(self.read_data_str(f)) for f in meta_files]

        return list(meta_contents)