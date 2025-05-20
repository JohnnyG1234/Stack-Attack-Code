# pip install requests 
import requests


# https://api.dictionaryapi.dev/api/v2/entries/en/hello
# https://api.dictionaryapi.dev/api/v2/entries/en/<word>

url = 'https://api.dictionaryapi.dev/api/v2/entries/en/hello'

response = requests.request("GET", url)

print(response.json()[0]['word'])