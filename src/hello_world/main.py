
""" Entry Point for App """

import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_http():
    """
    Returns:
        The text you want to send back to the user.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return f'Hello, {name}!'

if __name__ == "__main__":
    app.run(
        debug = True,
        host = '0.0.0.0',
        port = int(os.environ.get('PORT', 8080))
    )
