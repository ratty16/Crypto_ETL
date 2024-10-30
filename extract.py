import requests

def extract_data():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return {'currency': 'Bitcoin', 'price': data['bitcoin']['usd']}
