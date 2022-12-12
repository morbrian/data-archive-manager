from flask_restx import fields

snapshot_request_model_template = {
    'label': fields.String(required=False, description='Supplemental label for snapshot'),
}

restore_request_model_template = {
    'uuid': fields.String(required=True, description='Uuid of snapshot to be restored.'),
}

meta_model_template = {
    'uuid': fields.String(required=True, description='Meta data unique id'),
    'type': fields.String(required=True, description='Service name where data came from'),
    'datetime': fields.String(required=True, description='Date-time when data was exported from service'),
    'base_name': fields.String(required=True, description='Base-name of file on disk in archiver'),
    'data_hash': fields.String(required=True, description='sha256sum of datafile at the time when persisted to disk'),
    'label': fields.String(required=False, description='Optional supplemental label appended to file base_name to help find it later'),
}