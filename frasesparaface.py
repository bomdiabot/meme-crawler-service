import urllib3
from bs4 import BeautifulSoup
import json
import requests

api_url = 'http://35.226.124.10:7310'

def login(user, password):
    payload = {'username': user, 'password': password}
    r = requests.post(api_url + '/auth/login', data=payload)
    access_token = r.json()['access_token']
    return access_token

def get_texts(page):    
    http = urllib3.PoolManager()
    page_url = 'https://www.frasesparaface.com.br/frases-bom-dia/{}/'.format(page)
    response = http.request('GET', page_url)
    soup = BeautifulSoup(response.data, 'html.parser')

    title = soup.find_all('span', attrs={'class': 'phrase-title'})
    collection = []
    for bom_dia in title:
        collection.append(bom_dia.text.strip())
    return collection
