from flask import request
 
def test_login_and_logout(client):
    with client as c:
        response = c.post('/login', data=dict(passcode='mywrongpasscode'),\
                follow_redirects=True)
        assert request.path == '/login'

    with client as c:
        response = c.post('/login', data=dict(passcode='mypasscode'),\
                follow_redirects=True)
        assert request.path == '/'

    response = client.get('/')
    assert response.status_code == 200
    client.get('/logout')

    with client as c:
        response = c.post('/login', data=dict(passcode='mywrongpasscode'),\
                follow_redirects=True)
        assert request.path == '/login'



