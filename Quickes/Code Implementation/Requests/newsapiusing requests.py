import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd
import numpy as np
import time

languages={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}


def get_articles(file):
    article_results=[]

    for i in range(len(file)):
        article_dict = {}
        article_dict['title']=file[i]['title']
        article_dict['author']=file[i]['author']
        article_dict['source']=file[i]['source']
        article_dict['description']=file[i]['description']
        article_dict['content']=file[i]['content']
        article_dict['pub_date']=file[i]['publishedAt']
        article_dict['url']=file[i]['url']
        article_dict['photo_url']=file[i]['urlToImage']

        article_results.append(article_dict)

    return article_results

url='https://newsapi.org/v2/everything?'

api_key='deb16b6cdde14e63be41830980b7d40e'

perameters={
    'q':'indian news',
    'pagesize':100,
    'apiKey' : api_key,
    'language' : 'en',
    'from' : '2020-06-10'
}

response=requests.get(url,params=perameters)
response_json,ls,title,photo,url = response.json(),[],[],[],[]
"""for _ in get_articles(response_json['articles']):
        print(_)"""

for _ in get_articles(response_json['articles']):

        n,ll=3,[]    
        url.append(_['url'])
        photo.append(_['photo_url'])
        title.append(_['title'])
        
print(url)
print("==============")
print(photo)
print("==============")
print(title)