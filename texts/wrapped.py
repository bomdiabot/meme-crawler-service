import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()

class Source(object):

    def __init__(self, url=None, wrap_element=None, wrap_selector=None, element=None):
        if url is None or wrap_element is None or wrap_selector is None or element is None:
            raise ValueError('Page, element and selector are obrigatory')
        else:
            self.url = url
            self.wrap_element = wrap_element
            self.wrap_selector = wrap_selector
            self.element = element

    def get_page_texts(self, page):    
        http = urllib3.PoolManager()
        page_url = self.url.format(page)
        response = http.request('GET', page_url)
        soup = BeautifulSoup(response.data, 'html.parser')

        title = soup.find_all(self.wrap_element, attrs=self.wrap_selector)
        collection = []
        for grid in title:
            bom_dia = grid.find(self.element)
            if bom_dia is not None and bom_dia.text.strip() != 'Bom dia!':
                collection.append(bom_dia.text.strip().replace('\n', ' '))
        return collection
    def get_all_texts(self):
        collection = []
        for i in range(4):
            page_content = self.get_page_texts(i+1)
            print(page_content)
            collection.append(page_content)