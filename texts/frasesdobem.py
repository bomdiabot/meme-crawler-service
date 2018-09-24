import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()

def get_page_texts(page):    
    http = urllib3.PoolManager()
    page_url = 'https://www.frasesdobem.com.br/frases-de-bom-dia/page/{}/'.format(page)
    response = http.request('GET', page_url)
    soup = BeautifulSoup(response.data, 'html.parser')

    title = soup.find_all('p', attrs={'class': 'frase'})
    collection = []
    for bom_dia in title:
        collection.append(bom_dia.text.strip())
    return collection
def get_all_texts():
    collection = []
    for i in range(4):
        page_content = get_page_texts(i+1)
        print(page_content)
        collection.append(page_content)