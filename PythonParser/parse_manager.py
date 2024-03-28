from multiprocessing import Process

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
import func_timeout

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
    def get_status(url):
        return requests.get(url).status_code


class SmartParser(SimpleParser):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Firefox()

    def parse(self, url):
        self.driver.get(url)

        html = self.driver.page_source

        soup = BeautifulSoup(html, 'html-parser')
        return soup

class ParseManager:
    def __init__(self):
        self.simple_parser = SimpleParser()
        self.smart_parser = SmartParser()
        self.soup = None
        self.status = False

    def run(self, url):
        try:
            self.soup = self.simple_parse(url)
            self.status = 1
        except:
            try:
                self.soup = self.smart_parse(url)
                self.status = 1
            except Exception as ex:
                print(ex)

    def get_status(self, url):
        return self.simple_parser.get_status(url)

    def parse(self, url, date=None):
        self.status = False
        self.soup = None
        if date is not None:
            date = date.replace('.', '').replace('-', '')
            url = f'https://web.archive.org/web/{date}/{url}'
        while not self.status:
            try:
                func_timeout.func_timeout(
                    120, self.run, args=[url]
                )
            except func_timeout.FunctionTimedOut:
                print('pizda, я завис')

        return self.soup

    def simple_parse(self, url):
        return self.simple_parser.parse(url)

    def smart_parse(self, url):
        return self.smart_parser.parse(url)