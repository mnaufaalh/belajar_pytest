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
            name: self.fake.name()
            is_active: self.fake.boolean()
        }
        response = requests.post(
            f'{baseUrl}/catalog-service/v1/category/create',
            headers = self.headers,
            json = payloadData
            )
        return response

    