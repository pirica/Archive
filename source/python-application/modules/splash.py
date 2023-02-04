#!/usr/bin/python3

from requests import get
import base64

# Gets the splash for the game
def get_splash(version, type="mobileBgImg"):
    # The endpoint
    endpoint = 'https://www.epicgames.com/fortnite/en-US/api/cms/home'
    # Request the api with the id and type
    buffer = get(get(endpoint).json()['carousel']['slides'][0]['background']['desktopImage']).content

    # Encode and return it
    return 'data:image/png;base64,' + str(base64.b64encode(buffer)).split('\'')[1].split('\'')[0]
