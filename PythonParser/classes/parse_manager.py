import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver


class NoAccessError(Exception):
    pass


class SimpleParser:
    def __init__(self):
        self.ua = UserAgent(min_percentage=2.1)
        self.random_ua = self.ua.random
        self.request_headers = {
            'user-agent': self.random_ua
        }

    def parse(self, url):
        return BeautifulSoup(requests.get(url, headers=self.request_headers).text, 'html.parser')

    @staticmethod
    def get_status(self, url):
        return requests.get(url).status_code


class SmartParser(SimpleParser):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Firefox()

    def parse(self, url):
        self.driver.get(url)

        html = self.driver.page_source

        soup = BeautifulSoup(html)
        return soup


class ParseManager:
    def __init__(self):
        self.simple_parser = SimpleParser()
        self.smart_parser = SmartParser()

    def parse(self, url, date=None):
        status = 0
        soup = None
        if date is not None:
            date = date.replace('.', '').replace('-', '')
            url = f'https://web.archive.org/web/{date}/{url}'
        while not status:
            try:
                soup = self.simple_parse(url)
                status = 1
            except:
                try:
                    soup = self.smart_parse(url)
                    status = 1
                except Exception as ex:
                    print(ex)

        return soup

    def simple_parse(self, url):
        return self.simple_parser.parse(url)

    def smart_parse(self, url):
        return self.smart_parser.parse(url)
