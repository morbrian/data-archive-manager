from flask import url_for
from flask_restx import Api 

from .darchman import api as darchman

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