import pytest
import src.console.login as login
from src.catalog.category import Category
from faker import Faker

@pytest.fixture
def access_token():
    response = login.login_console('superadmin@kickavenue.com', 'loremipsum').json()
    return response['data']['access_token']

def test_create_category(access_token):
    category = Category(access_token)
    responseCreateCategory = category.create_category()
    bodyResponseCreateCategory = responseCreateCategory.json()
    bodyResponseDataCreateCategory = bodyResponseCreateCategory['Data']
    idCategory = bodyResponseDataCreateCategory['id']
    assert responseCreateCategory.status_code == 201
    assert type(bodyResponseCreateCategory['Code']) == int
    assert type(bodyResponseCreateCategory['Status']) == str
    assert type(bodyResponseCreateCategory['Data']) == dict
    assert type(bodyResponseCreateCategory['Message']) == str
    assert type(bodyResponseDataCreateCategory['id']) == int
    assert type(bodyResponseDataCreateCategory['name']) == str
    assert type(bodyResponseDataCreateCategory['sequence']) == int
    assert type(bodyResponseDataCreateCategory['is_active']) == bool
    assert bodyResponseCreateCategory['Status'] == 'success'
    assert bodyResponseCreateCategory['Message'] == 'Created'
    assert bodyResponseDataCreateCategory['id'] == idCategory