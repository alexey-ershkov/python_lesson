import requests

resp = requests.get('http://www.lyceum8.nnov.ru/')

file = open('index.html', 'w')
file.write(resp.text)
file.close()
