import requests

url = "https://newsapiraygorodskijv1.p.rapidapi.com/getArticles"

payload = ""
headers = {
    'x-rapidapi-host': "NewsAPIraygorodskijV1.p.rapidapi.com",
    'x-rapidapi-key': "d2ce6e0d15mshd755d80bc442ebcp16ffbfjsnbd6469d9b520",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)