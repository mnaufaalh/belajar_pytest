import pytest
import src.console.login as login
from src.catalog.brand import Brand

def test_create_brand():
    bodyResponseLogin = login.login_console('superadmin@kickavenue.com', 'loremipsum').json()
    accessToken = bodyResponseLogin['data']['access_token']
    brand = Brand(accessToken)
    responseCreateBrand = brand.create_brand()
    bodyResponseCreateBrand = responseCreateBrand.json()
    responseMessageCreateBrand = bodyResponseCreateBrand['Message']
    assert responseCreateBrand.status_code == 201
    assert responseMessageCreateBrand == 'Created'

def test_get_brand():
    bodyResponseLogin = login.login_console('superadmin@kickavenue.com', 'loremipsum').json()
    accessToken = bodyResponseLogin['data']['access_token']
    brand = Brand(accessToken)
    bodyResponseCreateBrand = brand.create_brand().json()
    idBrand = bodyResponseCreateBrand['Data']['id']
    responseUpdateBrand = brand.update_brand(idBrand)
    bodyResponseUpdateBrand = responseUpdateBrand.json()
    responseMessageUpdateBrand = bodyResponseUpdateBrand['Message']
    assert responseUpdateBrand.status_code == 200
    assert responseMessageUpdateBrand == 'Success'
