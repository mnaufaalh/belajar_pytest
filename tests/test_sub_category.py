import pytest
import src.console.login as login
from src.catalog.sub_category import Sub_Category
from src.catalog.category import Category
from faker import Faker


@pytest.fixture
def access_token():
    response = login.login_console(
        'superadmin@kickavenue.com', 'loremipsum'
    ).json()
    return response['data']['access_token']


def test_create_sub_category(access_token):
    fake = Faker()
    category = Category(access_token)
    sub_category = Sub_Category(access_token)
    bodyResponseGetCategory = category.get_category().json()
    pageSizeResponseGetCategory = bodyResponseGetCategory['Data']['pageSize']
    selectedCategory = bodyResponseGetCategory['Data']['content'][fake.random_int(
        max=pageSizeResponseGetCategory - 1)]
    idSelectedCategory = selectedCategory['id']
    responseCreateSubCategory = sub_category.create_sub_category(
        idSelectedCategory)
    bodyResponseCreateSubCategory = responseCreateSubCategory.json()
    responseMessageCreateSubCategory = bodyResponseCreateSubCategory['Message']
    assert responseCreateSubCategory.status_code == 201
    assert responseMessageCreateSubCategory == 'Created'


def test_update_sub_category(access_token):
    fake = Faker()
    sub_category = Sub_Category(access_token)
    category = Category(access_token)
    bodyResponseGetSubCategory = category.get_category().json()
    pageSize = bodyResponseGetSubCategory['Data']['pageSize']
    selectedCategory = bodyResponseGetSubCategory['Data']['content'][fake.random_int(
        max=pageSize - 1)]
    idSelectedCategory = selectedCategory['id']
    bodyResponseCreateSubCategory = sub_category.create_sub_category(
        idSelectedCategory).json()
    idSubCategory = bodyResponseCreateSubCategory['Data']['id']
    responseUpdateSubCategory = sub_category.update_sub_category(
        idSelectedCategory, idSubCategory)
    bodyResponseUpdateSubCategory = responseUpdateSubCategory.json()
    responseMessageUpdateSubCategory = bodyResponseUpdateSubCategory['Message']
    assert responseUpdateSubCategory.status_code == 200
    assert responseMessageUpdateSubCategory == 'Success'


def test_delete_sub_category(access_token):
    fake = Faker()
    sub_category = Sub_Category(access_token)
    category = Category(access_token)
    bodyResponseGetCategory = category.get_category().json()
    pageSizeResponseGetCategory = bodyResponseGetCategory['Data']['pageSize']
    selectedCategory = bodyResponseGetCategory['Data']['content'][fake.random_int(
        max=pageSizeResponseGetCategory - 1)]
    idSelectedCategory = selectedCategory['id']
    bodyResponseCreateCategory = sub_category.create_sub_category(
        idSelectedCategory).json()
    idSubCategory = bodyResponseCreateCategory['Data']['id']
    responseDeleteSubCategory = sub_category.delete_sub_category(idSubCategory)
    assert responseDeleteSubCategory.status_code == 204
    responseGetDeletedSubCategory = category.get_category_detail(idSubCategory)
    bodyResponseGetDeletedSubCategory = responseGetDeletedSubCategory.json()
    assert responseGetDeletedSubCategory.status_code == 404
    assert type(bodyResponseGetDeletedSubCategory['Code']) == int
    assert type(bodyResponseGetDeletedSubCategory['Status']) == str
    assert type(bodyResponseGetDeletedSubCategory['Data']) == dict
    assert type(bodyResponseGetDeletedSubCategory['Message']) == str
    assert bodyResponseGetDeletedSubCategory['Code'] == 101005
    assert bodyResponseGetDeletedSubCategory['Status'] == 'error'
    assert bodyResponseGetDeletedSubCategory['Data'] == {}
    assert bodyResponseGetDeletedSubCategory['Message'] == 'Your requested Item is not found'
