import requests
import json

base_url = 'http://127.0.0.1:5000/review'

# params = {'max_records': 3, 'sort': 'DESC'}
body = {'book': 'The Great Gatsby', 'rating': 7.0, 'notes': 'A classic!'}

response = requests.post(base_url, json=body)

# print(response.json())