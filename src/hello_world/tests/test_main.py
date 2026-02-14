
""" Test Module """

import pytest
from hello_world import main

@pytest.fixture
def client():
    """Create a Flask test client for the app."""
    main.app.config['TESTING'] = True
    with main.app.test_client() as client:
        yield client

def test_hello_http_with_json_name(client):
    """
    Method to test with JSON object
    """
    response = client.post('/', json={"name": "Alice"})
    assert "Hello, Alice!" in response.text

def test_hello_http_with_args_name(client):
    """
    Test with URL arguments (e.g. ?name=Bob)
    """
    response = client.get('/?name=Bob')
    assert "Hello, Bob!" in response.text

def test_hello_http_default(client):
    """
    Test with no data
    """
    response = client.get('/')
    assert "Hello, World!" in response.text

def test_hello_http(client):
    """
    Test another JSON payload
    """
    response = client.post('/', json={"name": "CI/CD"})
    assert "Hello, CI/CD!" in response.text
