from texts.data import wrapped_content, unwrapped_content
from texts.wrapped import Source as WrappedSource
from texts.unwrapped import Source as UnwrappedSource
from client import Client
import sys

def main():
    cli = Client(sys.argv[1], sys.argv[2])
    for item in wrapped_content:
        source = WrappedSource(item['url'], item['class'])
        texts = source.get_all_texts(item['pages'])
        for page in texts:
            for text in page:
                cli.post_text(text, item['name'])
        
    for item in unwrapped_content:
        source = UnwrappedSource(item['url'], item['element'], item['class'])
        source.get_all_texts(item['pages'])
        texts = source.get_all_texts(item['pages'])
        for page in texts:
            for text in page:
                cli.post_text(text, item['name'])

if __name__ == "__main__":
    main()