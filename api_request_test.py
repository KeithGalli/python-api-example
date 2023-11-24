import requests
import json

base_url = 'https://kg-book-review-api.onrender.com/all_reviews'

params = {'max_records': 3, 'sort': 'DESC'}
# body = {'book': 'The Alchemist', 'rating': 7.2, 'notes': 'A classic!'}

response = requests.get(base_url, params=params)

print(response.json())
