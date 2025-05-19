import pytest
import src.console.login as login
from src.catalog.category import Category
from faker import Faker


@pytest.fixture
def access_token():
    response = login.login_console(
        'superadmin@kickavenue.com', 'loremipsum').json()
    return response['data']['access_token']


def test_create_category(access_token):
    category = Category(access_token)
    responseCreateCategory = category.create_category()
    bodyResponseCreateCategory = responseCreateCategory.json()
    responseMessageCreateCategory = bodyResponseCreateCategory['Message']
    assert responseCreateCategory.status_code == 201
    assert responseMessageCreateCategory == 'Created'


def test_update_category(access_token):
    category = Category(access_token)
    bodyResponseCreateCategory = category.create_category().json()
    idCategory = bodyResponseCreateCategory['Data']['id']
    responseUpdateCategory = category.update_category(idCategory)
    bodyResponseUpdateCategory = responseUpdateCategory.json()
    responseMessageUpdateCategory = bodyResponseUpdateCategory['Message']
    assert responseUpdateCategory.status_code == 200
    assert responseMessageUpdateCategory == 'Success'


def test_get_category(access_token):
    fake = Faker()
    category = Category(access_token)
    responseGetCategory = category.get_category()
    bodyResponseGetCategory = responseGetCategory.json()
    bodyContentGetCategory = bodyResponseGetCategory['Data']['content']
    pageSize = bodyResponseGetCategory['Data']['pageSize']
    selectedCategory = bodyContentGetCategory[fake.random_int(
        max=pageSize - 1)]
    assert responseGetCategory.status_code == 200
    assert bodyResponseGetCategory['Message'] == 'Success'
    assert type(bodyResponseGetCategory['Data']) == dict
    assert type(bodyContentGetCategory) == list
    assert type(selectedCategory) == dict
    assert type(selectedCategory['id']) == int
    assert type(selectedCategory['name']) == str
    assert type(selectedCategory['sequence']) == int
    assert type(selectedCategory['is_active']) == bool


def test_get_category_detail(access_token):
    category = Category(access_token)
    bodyReposneCreateCategory = category.create_category().json()
    idCategory = bodyReposneCreateCategory['Data']['id']
    nameCategory = bodyReposneCreateCategory['Data']['name']
    isActiveCategory = bodyReposneCreateCategory['Data']['is_active']
    responseGetCategoryDetail = category.get_category_detail(idCategory)
    bodyResponseGetCategoryDetail = responseGetCategoryDetail.json()
    bodyResponseDataGetCategoryDetail = bodyResponseGetCategoryDetail['Data']
    assert responseGetCategoryDetail.status_code == 200
    assert type(bodyResponseGetCategoryDetail) == dict
    assert type(bodyResponseDataGetCategoryDetail['id']) == int
    assert type(bodyResponseDataGetCategoryDetail['name']) == str
    assert type(bodyResponseDataGetCategoryDetail['is_active']) == bool
    assert bodyResponseDataGetCategoryDetail['id'] == idCategory
    assert bodyResponseDataGetCategoryDetail['name'] == nameCategory
    assert bodyResponseDataGetCategoryDetail['is_active'] == isActiveCategory


def test_delete_category(access_token):
    category = Category(access_token)
    bodyResponseCreateCategory = category.create_category().json()
    idCategory = bodyResponseCreateCategory['Data']['id']
    responseDeleteCategory = category.delete_category(idCategory)
    assert responseDeleteCategory.status_code == 204
    responseGetCategoryDetail = category.get_category_detail(idCategory)
    bodyResponseGetDeleteCategoryDetail = responseGetCategoryDetail.json()
    assert responseGetCategoryDetail.status_code == 404
    assert type(bodyResponseGetDeleteCategoryDetail['Code']) == int
    assert type(bodyResponseGetDeleteCategoryDetail['Status']) == str
    assert type(bodyResponseGetDeleteCategoryDetail['Data']) == dict
    assert type(bodyResponseGetDeleteCategoryDetail['Message']) == str
    assert bodyResponseGetDeleteCategoryDetail['Code'] == 101005
    assert bodyResponseGetDeleteCategoryDetail['Status'] == 'error'
    assert bodyResponseGetDeleteCategoryDetail['Data'] == {}
    assert bodyResponseGetDeleteCategoryDetail['Message'] == 'Your requested Item is not found'
