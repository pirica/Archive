#!/usr/bin/python3

from requests import get
import base64

# Gets the splash for the game
def get_splash(version, type="mobileBgImg"):
    # NOTE: Expected to fail again in the future
    endpoint = 'https://www.fortnite.com/?_data=routes%2F_index'
    buffer = get(get(endpoint).json()['hero'][0]['backgroundImage']).content
    
    # Encode and return it
    return 'data:image/png;base64,' + str(base64.b64encode(buffer)).split('\'')[1].split('\'')[0]