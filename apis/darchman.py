from flask_restx import Namespace, Resource
from flask import request, json
from mediator.mediator import create_mediator
from config.config import config
from .models import meta_model_template, snapshot_request_model_template

api = Namespace('darchman', description='Data Archive Manager Interface')

snapshot_request = api.model('snapshot_request', snapshot_request_model_template)
meta_model = api.model('meta_model', meta_model_template)

def get_mediator(service_name):
    config_data = config.get_config_data()
    return create_mediator(
        service_name,
        config_data[service_name]['service_url'],
        config_data['darchman']['base_folder']
    )

@api.route('/<string:service_name>/snapshot')
class DarchmanSnapshot(Resource):
    @api.doc('darchman_snapshot')
    @api.doc(body=snapshot_request)
    @api.marshal_with(meta_model)
    def post(self, service_name):
        """Store a snapshot of service data"""
        data = json.loads(request.data)
        mediator = get_mediator(service_name)
        result = mediator.snapshot(data.get('label'))
        return result


@api.route('/<string:service_name>/snapshot/<string:uuid>')
class DarchmanSnapshot(Resource):
    @api.doc('darchman_fetch_snapshot')
    def get(self, service_name, uuid):
        """Fetch content for a snapshot of service data"""
        mediator = get_mediator(service_name)
        result = mediator.fetch_snapshot(uuid)
        if result is None:
            api.abort(404, 'uuid not found')
        return result
    

@api.route('/<string:service_name>/history')
class DarchmanHistory(Resource):
    @api.doc('darchman_history')
    @api.marshal_with(meta_model)
    def get(self, service_name):
        """Store a snapshot of service data"""
        mediator = get_mediator(service_name)
        result = mediator.history()
        return result

@api.route('/<string:service_name>/restore/<string:uuid>')
class DarchmanRestore(Resource):
    @api.doc('darchman_restore_snapshot')
    def get(self, service_name, uuid):
        """Restore identified snapshot content to service"""
        mediator = get_mediator(service_name)
        stored = mediator.restore_snapshot_to_service(uuid)
        if stored is None:
            api.abort(500, 'storage operation anomaly')
        return stored
