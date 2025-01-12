from .base import BaseParser


class ProductParser(BaseParser):
    def get_category_products(self, category_url: str):
        soup = self.get_soup(url=category_url)
        wrapper = soup.find('div', class_='products-box')
        products = wrapper.find_all('div', class_='product-item-wrapper')
        result = []
        for product in products:
            name = product.find('a', class_='product-name').get_text(strip=True)
            price = product.find('div', class_='product-price__current').get_text(strip=True)
            link = self.host + product.find('a', class_='product-name')['href']
            try:
                img = product.find('img', class_='product-image')['src']
            except:
                img = ''
            result.append({
                'name': name,
                'price': price,
                'link': link,
                'img': img
            })
        return result
