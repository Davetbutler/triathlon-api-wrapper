import os
import requests

TRI_API_KEY = os.environ.get('TRI_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

if TRI_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. None, given here"
    )
session = requests.Session()
session.params = {}
session.params['api_key'] = TRI_API_KEY

from .tri import Athlete, AthleteListings