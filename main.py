from site_parser.category import CategoryParser
from site_parser.product import ProductParser
import settings


def main() -> None:
    category_parser = CategoryParser()
    product_parser = ProductParser()

    categories = category_parser.get_categories(
        url=settings.catalog_url
    )
    for category in categories:
        products = product_parser.get_category_products(
            category_url=category['href']
        )
        print(products)
    # print(categories)


main()

