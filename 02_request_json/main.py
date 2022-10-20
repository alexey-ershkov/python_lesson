import requests
import json

LIMIT = 10

resp = requests.get('''https://jsonplaceholder.typicode.com/posts?_limit={}'''.format(LIMIT));

print(json.dumps(resp.json(), indent=2))
