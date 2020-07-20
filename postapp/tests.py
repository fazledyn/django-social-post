from django.test import TestCase

import requests
import json
# Create your tests here.

if __name__ == '__main__':
    
    req_data = {
        'username': 'dyn',
        'password1': 'dyn888888',
        'password2': 'dyn888888'
    }

    r = requests.post('http://localhost:8000/api/create_user/', data=req_data)
    print(r)
    print("\nRequest sent successfully !")
