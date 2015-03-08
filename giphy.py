import requests
import random

search_url = 'http://api.giphy.com/v1/gifs/search'
api_key = 'dc6zaTOxFJmzC'  

def search(query):
	payload = {'q':query, 'api_key':api_key, 'rating': 'pg'}
	r = requests.get(search_url, params=payload)
	items = r.json()['data']
	i = random.randint(0, len(items) - 1)
	return items[i]['embed_url']