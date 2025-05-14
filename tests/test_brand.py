import pytest
import src.console.login as login
from src.catalog.brand import Brand
from faker import Faker

@pytest.fixture
def access_token():
    response = login.login_console('superadmin@kickavenue.com', 'loremipsum').json()
    return response['data']['access_token']

def test_create_brand(access_token):
    brand = Brand(access_token)
    responseCreateBrand = brand.create_brand()
    bodyResponseCreateBrand = responseCreateBrand.json()
    responseMessageCreateBrand = bodyResponseCreateBrand['Message']
    assert responseCreateBrand.status_code == 201
    assert responseMessageCreateBrand == 'Created'

def test_update_brand(access_token):
    brand = Brand(access_token)
    bodyResponseCreateBrand = brand.create_brand().json()
    idBrand = bodyResponseCreateBrand['Data']['id']
    responseUpdateBrand = brand.update_brand(idBrand)
    bodyResponseUpdateBrand = responseUpdateBrand.json()
    responseMessageUpdateBrand = bodyResponseUpdateBrand['Message']
    assert responseUpdateBrand.status_code == 200
    assert responseMessageUpdateBrand == 'Success'

def test_get_brand(access_token):
    fake = Faker()
    brand = Brand(access_token)
    responseGetBrand = brand.get_brand()
    bodyResponse = responseGetBrand.json()
    bodyContent = bodyResponse['Data']['content']
    pageSize = bodyResponse['Data']['pageSize']
    selectedBrand = bodyContent[fake.random_int(max = pageSize - 1)]
    assert responseGetBrand.status_code == 200 
    assert bodyResponse['Message'] == 'Success'
    assert type (bodyResponse['Data']) == dict
    assert type (bodyContent) == list
    assert type (selectedBrand) == dict
    assert type (selectedBrand['id']) == int
    assert type (selectedBrand['name']) == str
    assert type (selectedBrand['background_image']) == str
    assert type (selectedBrand['logo_image']) == str
    assert type (selectedBrand['description']) == str
    assert type (selectedBrand['is_partner']) == bool
    assert type (selectedBrand['is_active']) == bool

def test_get_brand_detail(access_token):
    brand = Brand(access_token)
    bodyResponseCreateBrand = brand.create_brand().json()
    idBrand = bodyResponseCreateBrand['Data']['id']
    nameBrand = bodyResponseCreateBrand['Data']['name']
    backgroundImageBrand = bodyResponseCreateBrand['Data']['background_image']
    logoImageBrand = bodyResponseCreateBrand['Data']['logo_image']
    descriptionBrand = bodyResponseCreateBrand['Data']['description']
    isPartnerBrand = bodyResponseCreateBrand['Data']['is_partner']
    isActiveBrand = bodyResponseCreateBrand['Data']['is_active']
    responseGetBrandDetail = brand.get_brand_detail(idBrand)
    bodyResponseGetBrandDetail = responseGetBrandDetail.json()
    bodyResponseDataGetBrandDetail = bodyResponseGetBrandDetail['Data']
    assert responseGetBrandDetail.status_code == 200
    assert type(bodyResponseGetBrandDetail) == dict
    assert type(bodyResponseDataGetBrandDetail['id']) == int
    assert type(bodyResponseDataGetBrandDetail['name']) == str
    assert type(bodyResponseDataGetBrandDetail['background_image']) == str
    assert type(bodyResponseDataGetBrandDetail['logo_image']) == str
    assert type(bodyResponseDataGetBrandDetail['description']) == str
    assert type(bodyResponseDataGetBrandDetail['is_partner']) == bool
    assert type(bodyResponseDataGetBrandDetail['is_active']) == bool
    assert (bodyResponseDataGetBrandDetail['id']) == idBrand
    assert (bodyResponseDataGetBrandDetail['name']) == nameBrand
    assert (bodyResponseDataGetBrandDetail['background_image']) == backgroundImageBrand
    assert (bodyResponseDataGetBrandDetail['logo_image']) == logoImageBrand
    assert (bodyResponseDataGetBrandDetail['description']) == descriptionBrand
    assert (bodyResponseDataGetBrandDetail['is_partner']) == isPartnerBrand
    assert (bodyResponseDataGetBrandDetail['is_active']) == isActiveBrand
    
def test_delete_brand(access_token):
    brand = Brand(access_token)
    bodyResponseCreateBrand = brand.create_brand().json()
    idBrand = bodyResponseCreateBrand['Data']['id']
    responseDeleteBrand = brand.delete_brand(idBrand)
    assert responseDeleteBrand.status_code == 204
    responseGetDeletedBrandDetail = brand.get_brand_detail(idBrand)
    bodyResponseGetDeletedBrandDetail = responseGetDeletedBrandDetail.json()
    assert responseGetDeletedBrandDetail.status_code == 404
    assert type(bodyResponseGetDeletedBrandDetail['Code']) == int
    assert type(bodyResponseGetDeletedBrandDetail['Status']) == str
    assert type(bodyResponseGetDeletedBrandDetail['Data']) == dict
    assert type(bodyResponseGetDeletedBrandDetail['Message']) == str
    assert bodyResponseGetDeletedBrandDetail['Code'] == 101005
    assert bodyResponseGetDeletedBrandDetail['Status'] == 'error'
    assert bodyResponseGetDeletedBrandDetail['Data'] == {}
    assert bodyResponseGetDeletedBrandDetail['Message'] == 'Your requested Item is not found'
