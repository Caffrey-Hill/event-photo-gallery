from io import BytesIO

from flask import request

def assert_protected(response):
    assert response.status_code == 302
    assert 'Location' in response.headers
    assert response.headers['Location'] == request.host_url + 'login'

def test_failed_login(client):
    with client as c:
        response = c.post('/login', data=dict(passcode='mywrongpasscode'),\
                follow_redirects=True)
        assert request.path == '/login'

def test_login(client):
    with client as c:
        response = c.post('/login', data=dict(passcode='mypasscode'),\
                follow_redirects=True)
        assert request.path == '/'

def test_admin_redirect(client):
    with client as c:
        response = c.get('/admin', follow_redirects=True)
        assert request.path == '/login'

def test_gallery(client):
    with client as c:
        response = c.get('/')
        assert_protected(response)

    client.post('/login', data=dict(passcode='mypasscode'))
    response = client.get('/')
    assert response.status_code == 200

def test_download(client):

    with client as c:
        response = c.get('/download')
        assert_protected(response)
        
    client.post('/login', data=dict(passcode='mypasscode'))
    response = client.get('/download')
    assert response.status_code == 200

def test_upload(client):

    with client as c:
        response = c.post('/upload', data=dict(file=(BytesIO(b'Hello'),\
                'hello.txt'), category='1'))
        assert_protected(response)
        
    client.post('/login', data=dict(passcode='mypasscode'))
    with client as c:
        response = c.post('/upload', data=dict(file=(BytesIO(b'Hello'),\
            'hello.txt'), category='1'))
        assert response.headers['Location'] == request.host_url
        with c.session_transaction() as session:
            flash_message = dict(session['_flashes']).get('message')
            assert flash_message == 'Photo(s) uploaded.'
