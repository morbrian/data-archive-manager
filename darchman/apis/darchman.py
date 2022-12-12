from flask_restx import Namespace, Resource
from flask import request, make_response, json
from mediator.mediator import create_mediator
from config.config import config
from .models import meta_model_template, snapshot_request_model_template, restore_request_model_template

api = Namespace('darchman', description='Data Archive Manager Interface')

snapshot_request = api.model('snapshot_request', snapshot_request_model_template)
restore_request = api.model('restore_request', restore_request_model_template)
meta_model = api.model('meta_model', meta_model_template)

def get_active_services():
    config_data = config.get_config_data()
    return ", ".join(config_data['active_services'])

def get_mediator(service_name):
    config_data = config.get_config_data()
    return create_mediator(
        service_name,
        config_data[service_name]['service_url'],
        config_data['darchman']['base_folder']
    )

@api.route('/<string:service_name>/snapshot')
@api.doc(params={'service_name': get_active_services()})
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
@api.doc(params={'service_name': get_active_services()})
class DarchmanSnapshot(Resource):
    @api.doc('darchman_fetch_snapshot')
    def get(self, service_name, uuid):
        """Fetch content for a snapshot of service data"""
        mediator = get_mediator(service_name)
        result = mediator.fetch_snapshot(uuid)
        if result is None:
            api.abort(404, 'uuid not found')
        return result


@api.route('/<string:service_name>/diff')
@api.doc(params={'service_name': get_active_services()})
class DarchmanDiff(Resource):
    @api.doc('darchman_fetch_snapshot')
    @api.doc(params={
        'uuid1': {'description': 'Uuid of first content'},
        'uuid2': {'description': 'Uuid of second content'}
    })
    @api.produces(['text/html'])
    def get(self, service_name):
        """Produce HTML diff of the snapshot content for two uuids"""
        uuid1 = request.args.get('uuid1')
        uuid2 = request.args.get('uuid2')
        mediator = get_mediator(service_name)
        result =  mediator.diff_snapshot_contents(uuid1, uuid2)
        if result is None:
            api.abort(404, 'uuid not found')
        response = make_response(result)
        response.headers['Content-Type'] = 'text/html'
        return response
    

@api.route('/<string:service_name>/history')
@api.doc(params={'service_name': get_active_services()})
class DarchmanHistory(Resource):
    @api.doc('darchman_history')
    @api.marshal_with(meta_model)
    def get(self, service_name):
        """List meta-data for past snapshots"""
        mediator = get_mediator(service_name)
        result = mediator.history()
        return result


@api.route('/<string:service_name>/restore')
@api.doc(params={'service_name': get_active_services()})
class DarchmanRestore(Resource):
    @api.doc('darchman_restore')
    @api.doc(body=restore_request)
    def post(self, service_name, uuid):
        """Restore identified snapshot content to service"""
        # TODO: enhance our restore capabilities with migrators and other modifiers
        data = json.loads(request.data)
        mediator = get_mediator(service_name)
        stored = mediator.restore_snapshot_to_service(data.get('uuid'))
        if stored is None:
            api.abort(500, 'storage operation anomaly')
        return stored
