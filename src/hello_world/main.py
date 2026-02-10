""" Entry Point for App """

import functions_framework

@functions_framework.http
def hello_http(request):
    """
    Args:
        request: A Flash/Django style request object.
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
