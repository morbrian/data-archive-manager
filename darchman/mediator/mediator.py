from archiver.archiver import Archiver
from adapter.generic_adapter import GenericAdapter

class Mediator:
    def __init__(self, adapter, archiver):
        self.adapter = adapter
        self.archiver = archiver
    
    def snapshot(self, label=None):
        data = self.adapter.export_all()
        meta = self.archiver.store_data(data, label)
        return meta
    
    def history(self):
        meta_list = self.archiver.list_meta()
        return meta_list
    
    def fetch_snapshot(self, uuid):
        content = self.archiver.retrieve_data(uuid)
        return content

    def restore_snapshot_to_service(self, uuid):
        data = self.fetch_snapshot(uuid)
        if data is None:
            raise Exception('snapshot for id "{}" not found'.format(uuid))
        # TODO: maybe check hash?
        stored = self.adapter.store_all(data)
        return stored


def get_adapter(service_name, service_url):
    return GenericAdapter(service_name, service_url)


def create_mediator(service_name, service_url, archiver_folder=None):
    adapter = get_adapter(service_name, service_url)
    archiver = Archiver(service_name, archiver_folder) if archiver_folder is not None else Archiver(service_name)
    return Mediator(adapter, archiver)
