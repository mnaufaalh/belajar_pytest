import requests
import json
from faker import Faker
from dotenv import load_dotenv
import os

load_dotenv('.staging.env')
baseUrl: str = os.getenv('BASE_URL_CONSOLE')

class Brand:
    def __init__(self, accessToken):
        self.fake = Faker()
        self.accessToken = accessToken
        self.headers = {
            'Authorization': f'Bearer {accessToken}'
        }

    def create_brand(self):
        filePath = os.path.abspath('./assets/image/image.png')
        payloadData = {
            'description': self.fake.sentence(),
            'is_active': self.fake.boolean(),
            'is_partner': self.fake.boolean(),
            'name': self.fake.name()
        }
        with open(filePath, 'rb') as f:
            files = {
                'logo_image': ('image.png', f, 'image/png'),
                'background_image': ('image.png', f, 'image/png')
            }
            data = {
                'payload': json.dumps(payloadData)
            }
            response = requests.post(
                f'{baseUrl}/catalog-service/v1/brand/create', 
                headers=self.headers,
                files=files, 
                data=data
            )
        return response

    def update_brand(self, idBrand):
        filePath = os.path.abspath('./assets/image/image.png')
        payloadData = {
            'description': self.fake.sentence(),
            'is_active': self.fake.boolean(),
            'is_partner': self.fake.boolean(),
            'name': self.fake.name()
        }
        with open(filePath, 'rb') as f:
            files = {
                'logo_image': ('image.png', f, 'image/png'),
                'background_image': ('image.png', f, 'image/png')
            }
            data = {
                'payload': json.dumps(payloadData)
            }
            response = requests.put(
                f'{baseUrl}/catalog-service/v1/brand/update/{idBrand}', 
                headers=self.headers,
                files=files, 
                data=data
            )
        return response

    def get_brand(self, params=None) :
        if params == None:
            params = {
                'sortBy': 'updated_at,desc',
                'pageSize': 100
            }
        response = requests.get(
            f'{baseUrl}/catalog-service/v1/brand/get',
            headers = self.headers,
            params = params
        )
        return response

    def get_brand_detail(self, idBrand) :
        response = requests.get(f'{baseUrl}/catalog-service/v1/brand/get/{idBrand}', headers = self.headers)
        return response

    def delete_brand(self, idBrand) : 
        response = requests.delete(f'{baseUrl}/catalog-service/v1/brand/delete/{idBrand}', headers = self.headers)
        return response