"""
This script runs the SpaceApp application using a development server.
"""

from os import environ
from SpaceApp import app

if __name__ == '__main__':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    HOST = environ.get('HOST', '0.0.0.0')
    try:
        #PORT = int(environ.get('SERVER_PORT', '5555'))
        PORT = int(environ.get('PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)
