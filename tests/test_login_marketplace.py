import pytest
import src.gateway.login as login


def test_valid_account():
    response = login.login_marketplace(
        'dummytesting2506@gmail.com', 'Test1234!')
    bodyResponse = response.json()
    responseMessage = bodyResponse['Message']
    accessToken = bodyResponse['Data']['access_token']
    assert response.status_code == 200
    assert responseMessage == 'Success'
    assert 'access_token' in bodyResponse['Data']
    assert isinstance(accessToken, str)


def test_invalid_password():
    response = login.login_marketplace(
        'dummytesting2506@gmail.com', 'invalid_password')
    bodyResponse = response.json()
    responseMessage = bodyResponse['Message']
    assert response.status_code == 401
    assert responseMessage == 'Your requested Item is not found'


def test_email_doesnt_exists():
    response = login.login_marketplace(
        'emailDoesntExist@gmail.com', 'Test1234!')
    bodyResponse = response.json()
    responseMessage = bodyResponse['Message']
    assert response.status_code == 401
    assert responseMessage == 'Your requested Item is not found'
