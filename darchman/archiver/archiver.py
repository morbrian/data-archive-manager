import json
import pathlib
from datetime import datetime
import uuid
import hashlib
from werkzeug.utils import secure_filename

class Archiver:
    def __init__(self, service_name, base_folder):
        self.service_name=service_name
        self.base_folder='{}/{}'.format(base_folder, service_name)
        pathlib.Path(self.base_folder).mkdir(parents=True, exist_ok=True)

    def get_data_hash(self, data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    def get_base_name(self, uuid, stamp):
        return secure_filename('{}_{}_{}'.format(uuid, self.service_name, stamp))

    def get_data_filename(self, base_name):
        return '{}/{}.json'.format(self.base_folder, base_name)

    def get_meta_filename(self, base_name):
        return '{}/{}.meta'.format(self.base_folder, base_name)

    def build_meta(self, data, label=None):
        timestamp = datetime.now().isoformat()
        stamp = timestamp if label is None else '{}_{}'.format(timestamp, label)
        identity = str(uuid.uuid4())
        return {
            'uuid': identity,
            'type': self.service_name,
            'datetime': timestamp,
            'base_name': self.get_base_name(identity, stamp),
            'data_hash': self.get_data_hash(data),
            'label': label
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

    def store_data(self, data, label=None):
        data_str = '{}\n'.format(json.dumps(data))
        meta = self.build_meta(data_str, label)
        base_name = meta['base_name']

        data_filename = self.get_data_filename(base_name)
        self.write_data_str(pathlib.Path(data_filename), data_str)

        meta_filename = self.get_meta_filename(base_name)
        meta_str = '{}\n'.format(json.dumps(meta))
        self.write_data_str(pathlib.Path(meta_filename), meta_str)

        return meta
    
    def retrieve_data(self, uuid):
        matched_list = list(pathlib.Path(self.base_folder).glob('{}*.json'.format(uuid)))
        count = len(matched_list)
        if count == 1:
            content = json.loads(self.read_data_str(matched_list[0]))
            return content
        elif count > 1:
            raise Exception('multiple matching ids')
        else:
            return None
    
    def list_meta(self):
        all_meta = pathlib.Path(self.base_folder).glob('*.meta')
        meta_files = [f for f in all_meta if f.is_file()]
        meta_contents = [json.loads(self.read_data_str(f)) for f in meta_files]

        return list(meta_contents)