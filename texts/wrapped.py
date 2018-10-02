import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()

class Source(object):

    def __init__(self, url=None, wrap_class=None):
        if url is None or wrap_class is None:
            raise ValueError('Page, element and selector are obrigatory')
        else:
            self.url = url
            self.wrap_class = wrap_class

    def get_page_texts(self, page):    
        http = urllib3.PoolManager()
        page_url = self.url.format(page)
        response = http.request('GET', page_url)
        soup = BeautifulSoup(response.data, 'html.parser')

        title = soup.find_all('div', {'class': self.wrap_class})
        collection = []
        for grid in title:
            bom_dia = grid.find('p')
            if bom_dia is not None and bom_dia.text.strip() != 'Bom dia!':
                collection.append(bom_dia.text.strip().replace('\n', ' '))
        return collection
    def get_all_texts(self, n):
        collection = []
        for i in range(n):
            page_content = self.get_page_texts(i+1)
            collection.append(page_content)
        return collection