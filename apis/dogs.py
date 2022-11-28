from flask_restx import Namespace, Resource, fields
from flask import request, json
from mediator.mediator import create_mediator
from .models import meta_model_template, snapshot_request_model_template

service_name = 'dogs'
api = Namespace(service_name, description='Dogs archive interface')

snapshot_request = api.model('snapshot_request', snapshot_request_model_template)
meta_model = api.model('meta_model', meta_model_template)

@api.route('/snapshot')
class DogsSnapshot(Resource):
    @api.doc('dogs_snapshot')
    @api.doc(body=snapshot_request)
    @api.marshal_with(meta_model)
    def post(self):
        """Store a snapshot of service data"""
        data = json.loads(request.data)
        mediator = create_mediator(service_name)
        result = mediator.snapshot(data.get('label'))
        return result
    

@api.route('/history')
class DogsHistory(Resource):
    @api.doc('dogs_history')
    @api.marshal_with(meta_model)
    def get(self):
        """Store a snapshot of service data"""
        mediator = create_mediator(service_name)
        result = mediator.history()
        return result
