import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()

def get_page_texts(page):    
    http = urllib3.PoolManager()
    page_url = 'https://www.belasmensagens.com.br/bom-dia/page/{}/'.format(page)
    response = http.request('GET', page_url)
    soup = BeautifulSoup(response.data, 'html.parser')

    title = soup.find_all('div', attrs={'class': 'grid-item'})
    collection = []
    for grid in title:
        bom_dia = grid.find('p')
        if bom_dia is not None and bom_dia.text.strip() != 'Bom dia!':
            collection.append(bom_dia.text.strip().replace('\n', ' '))
    return collection
def get_all_texts():
    collection = []
    for i in range(4):
        page_content = get_page_texts(i+1)
        print(page_content)
        collection.append(page_content)