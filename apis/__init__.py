from flask import url_for
from flask_restx import Api 

from .darchman import api as darchman
from .cats import api as cats
from.dogs import api as dogs

api = Api(
    title='Data Archive Manager Service',
    version='1.0',
    description='Data Archive Manager Service',
    # All API metadatas
)
@property
def specs_url(self):
    return url_for(self.endpoint('specs'), _external=False)

api.add_namespace(darchman)
api.add_namespace(cats)
api.add_namespace(dogs)