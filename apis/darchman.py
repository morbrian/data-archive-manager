from flask_restx import Namespace, Resource, fields


api = Namespace('darchman', description='Data Archive Manager Service')

# there's not exactly a model yet
# darchman = api.model('Cat', {
#     'id': fields.String(required=True, description='The cat identifier'),
#     'name': fields.String(required=True, description='The cat name'),
# })

darchman = api

@api.route('/')
class DataArchiveManager(Resource):
    @api.doc('history')
    # @api.marshal_list_with(cat)
    def get(self):
        '''tbd api'''
        return 'TBD - Darchman API'


# TODO
# management api should at least be able to display
# * which services we support
# * ability to manage configuration of services
#     * backup folder
#     * URL enpoints for services
#        (which might be behind private network, and not accessible to gui, but admin knows correct url)
# * summary statistics over all services
#     * disk usage
#     * last backup date
# other stuff....
#
# all of this is less important than the individual service archivers
#