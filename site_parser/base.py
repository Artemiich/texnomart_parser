import requests
from bs4 import BeautifulSoup
import settings


class BaseParser:
    host: str = settings.host
    page_num: int = 1

    def get_html(self, url: str) -> str:
        html = requests.get(url)
        html.raise_for_status()
        return html.text

    def get_soup(self, url: str) -> BeautifulSoup:
        html = self.get_html(url)
        return BeautifulSoup(html, 'html.parser')


