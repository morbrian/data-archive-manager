from archiver.archiver import Archiver
from adapter.cats_adapter import CatsAdapter
from adapter.dogs_adapter import DogsAdapter

class Mediator:
    def __init__(self, adapter, archiver):
        self.adapter = adapter
        self.archiver = archiver
    
    def snapshot(self):
        data = self.adapter.export_all()
        meta = self.archiver.store_data(data)
        return meta
    
    def history(self):
        meta_list = self.archiver.list_meta()
        return meta_list


def get_adapter(service_name, url):
    match service_name:
        case 'cats':
            return CatsAdapter(base_url=url) if url is not None else CatsAdapter()
        case 'dogs':
            return DogsAdapter(base_url=url) if url is not None else DogsAdapter()


def create_mediator(service_name, service_url, archiver_folder):
    adapter = get_adapter(service_name, service_url)
    archiver = Archiver(service_name, archiver_folder) if archiver_folder is not None else Archiver(service_name)
    return Mediator(adapter, archiver)
