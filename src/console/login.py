import requests
from dotenv import load_dotenv
import os

load_dotenv('.staging.env')
baseUrl: str = os.getenv('BASE_URL_CONSOLE')

def login_console(email, password):
    body = {
        "email": email,
        "password": password
    }
    response = requests.post(f'{baseUrl}/console-service/v1/auth/login', json = body)
    return response

