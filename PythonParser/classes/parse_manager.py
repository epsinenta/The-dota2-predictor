import requests
from bs4 import BeautifulSoup

class NoAccessError(Exception):
    pass


class SimpleParser:
    def parse(self, url):
        return BeautifulSoup(requests.get(url).text, 'html.parser')

    def get_status(self, url):
        return requests.get(url).status_code


class ParseManager:
    def __init__(self):
        self.simple_parser = SimpleParser()

    def parse(self, url, date=None):
        if date is not None:
            date = date.replace('.', '').replace('-', '')
            url = f'https://web.archive.org/web/{date}/{url}'
        if self.simple_parser.get_status(url) == 200:
            return self.simple_parser.parse(url)
        raise NoAccessError('No access to source')
