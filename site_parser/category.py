from .base import BaseParser
import bs4
import settings
from database.db import insert_category

CategoriesData = list[dict[str, str | int]]


# отдает список
# в списке есть словари
# ключи словаря это строки
# значения словаря это строки или цифры


class CategoryParser(BaseParser):
    def get_categories(self, url: str) -> CategoriesData:
        categories_soup = self.get_soup(url)

        wrapper = categories_soup.find('div', class_='category__wrap')

        categories: list[bs4.BeautifulSoup] = wrapper.find_all('div', class_='category__item')

        result = []

        for category in categories:
            title = category.find('h2').get_text(strip=True)
            href = category.find('a', class_='category__link')['href']
            pages_quantity = self.get_category_pages_quantity(
                category_url=self.host + href
            )
            insert_category(title, pages_quantity)
            result.append({  # https://texnomart.uz/ru/katalog/tehnika-dlya-kuhni/
                "title": title,
                "href": self.host + href,
                "pages_quantity": pages_quantity
            })
            print(f'У категории "{title} {pages_quantity} страниц"')
        return result

    def get_category_products_soup(self, category_url: str) -> bs4.BeautifulSoup:
        pass

    def get_category_pages_quantity(self, category_url: str) -> int:
        soup = self.get_soup(url=category_url)
        pagination = soup.find('div', class_='pagination')
        items = pagination.find_all('span')
        if not items:
            return 0
        return int(items[-2].get_text(strip=True))
