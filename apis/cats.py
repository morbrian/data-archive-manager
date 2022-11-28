from flask_restx import Namespace, Resource, fields
from flask import request, json
from mediator.mediator import create_mediator
from .models import meta_model_template, snapshot_request_model_template

service_name = 'cats'
api = Namespace(service_name, description='Cats archive interface')

snapshot_request = api.model('snapshot_request', snapshot_request_model_template)
meta_model = api.model('meta_model', meta_model_template)

@api.route('/snapshot')
class CatsSnapshot(Resource):
    @api.doc('cats_snapshot')
    @api.doc(body=snapshot_request)
    @api.marshal_with(meta_model)
    def post(self):
        """Store a snapshot of service data"""
        data = json.loads(request.data)
        mediator = create_mediator(service_name)
        result = mediator.snapshot(data.get('label'))
        return result


@api.route('/snapshot/<uuid>')
class CatsSnapshot(Resource):
    @api.doc('cats_fetch_snapshot')
    def get(self, uuid):
        """Fetch content for a snapshot of service data"""
        mediator = create_mediator(service_name)
        result = mediator.fetch_snapshot(uuid)
        if result is None:
            api.abort(404, 'uuid not found')
        return result
    

@api.route('/history')
class CatsHistory(Resource):
    @api.doc('cats_history')
    @api.marshal_with(meta_model)
    def get(self):
        """Store a snapshot of service data"""
        mediator = create_mediator(service_name)
        result = mediator.history()
        return result

@api.route('/restore/<uuid>')
class CatsRestore(Resource):
    @api.doc('cats_restore_snapshot')
    def get(self, uuid):
        """Restore identified snapshot content to service"""
        mediator = create_mediator(service_name)
        stored = mediator.restore_snapshot_to_service(uuid)
        if stored is None:
            api.abort(500, 'storage operation anomaly')
        return stored
