import requests

url = 'https://api.binance.com/api/v1/ping'

js = requests.get(url, headers=
{
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'})

print(js)
