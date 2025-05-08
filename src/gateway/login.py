import requests
from dotenv import load_dotenv
import os

load_dotenv('.staging.env')
baseUrl: str = os.getenv('BASE_URL_MARKETPLACE')

def login_marketplace(email, password):
    body = {
        "email": email,
        "password": password
    }
    response = requests.post(f'{baseUrl}/auth/login', json = body)
    bodyResponse = response.json()
    return bodyResponse