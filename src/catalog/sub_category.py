import requests
import json
from faker import Faker
from dotenv import load_dotenv
import os

load_dotenv('.staging.env')
baseUrl: str = os.getenv('BASE_URL_CONSOLE')


class Sub_Category:
    def __init__(self, accessToken):
        self.fake = Faker()
        self.accessToken = accessToken
        self.headers = {
            'Authorization': f'Bearer {accessToken}'
        }

    def create_sub_category(self, parentId):
        payloadData = {
            'name': self.fake.name(),
            'is_active': self.fake.boolean(),
            'parent_id': parentId
        }
        response = requests.post(
            f'{baseUrl}/catalog-service/v1/sub-category/create',
            headers=self.headers,
            json=payloadData
        )
        return response

    def update_sub_category(self, parentId, idSubCategory):
        payloadData = {
            'name': self.fake.name(),
            'is_active': self.fake.boolean(),
            'parent_id': parentId
        }
        response = requests.put(
            f'{baseUrl}/catalog-service/v1/sub-category/update/{idSubCategory}',
            headers=self.headers,
            json=payloadData
        )
        return response

    def delete_sub_category(self, idSubCategory):
        response = requests.delete(
            f'{baseUrl}/catalog-service/v1/sub-category/delete/{idSubCategory}',
            headers=self.headers
        )
        return response
