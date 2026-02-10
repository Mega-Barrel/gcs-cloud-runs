""" Test Module """
from unittest.mock import Mock
from hello_world import main

def test_hello_http_with_json_name():
    """
    Method to test with JSON object
    """
    request = Mock(get_json=Mock(return_value={"name": "Alice"}), args=None)
    response = main.hello_http(request)
    assert "Hello, Alice!" in response

def test_hello_http_with_args_name():
    """
    Mock a Request object with URL arguments (e.g. ?name=Bob)
    """
    request = Mock(get_json=Mock(return_value=None), args={"name": "Bob"})
    response = main.hello_http(request)
    assert "Hello, Bob!" in response

def test_hello_http_default():
    """
    Mock a Request object with no data
    """
    request = Mock(get_json=Mock(return_value=None), args={})
    response = main.hello_http(request)
    assert "Hello, World!" in response

def test_hello_http():
    """
    Mock a Request object with data
    """
    request = Mock()
    request.get_json.return_value = {"name": "CI/CD"}
    request.args = {}

    response = main.hello_http(request)
    assert "Hello, CI/CD!" in response
