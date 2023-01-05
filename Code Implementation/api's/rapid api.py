import requests

url = "https://covid-19-data.p.rapidapi.com/help/countries"

querystring = {"format":"json"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "d2ce6e0d15mshd755d80bc442ebcp16ffbfjsnbd6469d9b520"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

for _ in  response:
    for k in _:
        print(k)