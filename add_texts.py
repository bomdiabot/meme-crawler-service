from getpass import getpass
from texts.wrapped import Source as WrappedSource
from texts.unwrapped import Source as UnwrappedSource
from client import Client

def main():
    user = input('Memedata username: ')
    password = getpass('Memedata password: ')
    cli = Client(user, password)

    tag = input('Tag (bomdia/boatarde/boanoite): ')
    page_name = input('Page name: ')
    url = input('Source url(Add curly braces to the page index): ')
    pages = input('Number of pages to scrape: ')
    wrapped = input('Wrapped (y/n): ')
    element_class = input('Element class: ')

    if wrapped == 'n':
        element = input('Element: ')
        source = UnwrappedSource(url, element, element_class)
    else:
        source = WrappedSource(url, element_class)
    
    

    texts = source.get_all_texts(int(pages))
    print(texts)
    proceed = input('Proceed? (y/n) ')
    if proceed == 'y':
        confirmation = input('Are you sure? (y/n) ')
        if confirmation == 'y':
            for page in texts:
                for text in page:
                    cli.post_text(text, page_name, tag)            
    else:
        print('ok')



if __name__ == "__main__":
    main()