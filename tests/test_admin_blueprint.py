from flask import request

def assert_protected(response):
    assert response.status_code == 302
    assert 'Location' in response.headers
    assert response.headers['Location'] == request.host_url + 'login'

def test_admin_overview(client):
    with client as c:
        response = c.get('/admin/')
        assert_protected(response)

    client.post('/login', data=dict(passcode='mypasscode'))
    assert client.get('/admin/').status_code == 200

def test_admin_users(client):
    with client as c:
        response = c.get('/admin/users')
        assert_protected(response)

        response = c.post('/admin/users', data=dict(action='add', name='user'))
        assert_protected(response)
    
    client.post('/login', data=dict(passcode='mypasscode'))
    assert client.get('/admin/users').status_code == 200
    
    response = c.post('/admin/users', data=dict(action='add', name='user'))
    assert response.status_code == 200

def test_admin_categories(client):
    with client as c:
        response = c.get('/admin/categories')
        assert_protected(response)
        
        response = c.post('/admin/categories',\
                data=dict(action='add', name='name'))
        assert_protected(response)
    
    client.post('/login', data=dict(passcode='mypasscode'))
    assert client.get('/admin/categories').status_code == 200
    
    response = c.post('/admin/categories', data=dict(action='add', name='name'))
    assert response.status_code == 200
