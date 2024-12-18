# common functions

import requests

from functools import cache
from credentials.spotify import CLIENT_ID, CLIENT_SECRET

BASE_URL = 'https://api.spotify.com/v1/'
AUTH_URL = 'https://accounts.spotify.com/api/token'

def save_contents(filename, contents):
    with open(filename, 'w') as _file:
        _file.write(contents)

def get_contents(filename):
    with open(filename, 'r') as _file:
        contents = _file.readlines()
    return contents

@cache
def get_access_token(id, secret):
    auth_response = requests.post(AUTH_URL,
    {   
        'grant_type': 'client_credentials',
        'client_id': id,
        'client_secret': secret
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def spotify_request(request):
    headers = { 'Authorization':
                'Bearer {token}'.format(token = get_access_token(CLIENT_ID, CLIENT_SECRET)) }
    return requests.get(request, headers = headers).json()

