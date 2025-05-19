import requests
import json
from faker import Faker
from dotenv import load_dotenv
import os

load_dotenv('.staging.env')
baseUrl: str = os.getenv('BASE_URL_CONSOLE')


class Category:
    def __init__(self, accessToken):
        self.fake = Faker()
        self.accessToken = accessToken
        self.headers = {
            'Authorization': f'Bearer {accessToken}'
        }

    def create_category(self):
        payloadData = {
            'name': self.fake.name(),
            'is_active': self.fake.boolean()
        }
        response = requests.post(
            f'{baseUrl}/catalog-service/v1/category/create',
            headers=self.headers,
            json=payloadData
        )
        return response

    def update_category(self, idCategory):
        payloadData = {
            'name': self.fake.name(),
            'is_active': self.fake.boolean()
        }
        response = requests.put(
            f'{baseUrl}/catalog-service/v1/category/update/{idCategory}',
            headers=self.headers,
            json=payloadData
        )
        return response

    def get_category(self, params=None):
        if params == None:
            params = {
                'sortBy': 'updated_at,desc',
                'pageSize': 100,
                'type': 'CATEGORY'
            }
        response = requests.get(
            f'{baseUrl}/catalog-service/v1/category/get',
            headers=self.headers,
            params=params
        )
        return response

    def get_category_detail(self, idCategory):
        response = requests.get(
            f'{baseUrl}/catalog-service/v1/category/get/{idCategory}',
            headers=self.headers
        )
        return response

    def delete_category(self, idCategory):
        response = requests.delete(
            f'{baseUrl}/catalog-service/v1/category/delete/{idCategory}',
            headers=self.headers
        )
        return response
