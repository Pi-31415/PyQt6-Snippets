import requests

CURRENCYLAYER_API_KEY = "put your API key here"

r = requests.get('http://apilayer.net/api/live?access_key='+CURRENCYLAYER_API_KEY+
                 '&currencies=USD,AUD,CAD,XAU,BTC&format=1')

response = r.json()

print(response['quotes']['USDBTC'])
