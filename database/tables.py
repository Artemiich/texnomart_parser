from database import db

# categories
# id
# title
# pages_quantity


def create_categories_table():
    connection, cursor = db.connect_db('../texnomart.db')
    sql = """
        drop table if exists categories;
        create table if not exists categories(
            category_id integer primary key autoincrement,
            title text unique,
            pages_quantity integer
        );
    """
    cursor.executescript(sql)
    connection.commit()


def create_products_table():
    connection, cursor = db.connect_db('../texnomart.db')
    sql = """
    drop table if exists products;
    create table if not exists products(
        product_id integer primary key autoincrement,
        title text unique,
        price text,
        link text,
        img text,
        category_id integer references categories(category_id)
    );
    """
    cursor.executescript(sql)
    connection.commit()


def create_tables():
    create_categories_table()
    create_products_table()


create_tables()
# products
# id
# title
# price
# link
# img
# category_id

# Написать функцию для добавления продуктов в БД
