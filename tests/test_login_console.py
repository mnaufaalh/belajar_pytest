import pytest
import src.console.login as login

def test_valid_account():
    response = login.login_console('superadmin@kickavenue.com', 'loremipsum')
    bodyResponse = response.json()
    responseMessage = bodyResponse['message']
    accessToken = bodyResponse['data']['access_token']
    assert response.status_code == 200
    assert responseMessage == 'Success'
    assert 'access_token' in bodyResponse['data']
    assert isinstance(accessToken, str)

def test_invalid_password():
    response = login.login_console('superadmin@kickavenue.com', 'invalid_password')
    bodyResponse = response.json()
    assert response.status_code == 400
    assert type(bodyResponse) == dict
    

def test_email_doesnt_exists():
    response = login.login_console('emailDoesntExist@gmail.com', 'Test1234!')
    bodyResponse = response.json()
    assert response.status_code == 400
    assert type(bodyResponse) == dict