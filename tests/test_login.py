import pytest
import src.gateway.login as login

def test_valid_account():
    result = login.login_marketplace('dummytesting2506@gmail.com', 'Test1234!')
    responseMessage = result['Message']
    accessToken = result['Data']['access_token']
    assert responseMessage == 'Success'
    assert 'access_token' in result['Data']
    assert isinstance(accessToken, str)

def test_invalid_password():
    result = login.login_marketplace('dummytesting2506@gmail.com', 'invalid_password')
    responseMessage = result['Message']
    assert responseMessage == 'Your requested Item is not found'

def test_email_doesnt_exists():
    result = login.login_marketplace('emailDoesntExist@gmail.com', 'Test1234!')
    responseMessage = result['Message']
    assert responseMessage == 'Your requested Item is not found'
    