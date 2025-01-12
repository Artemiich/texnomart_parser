import sqlite3


def connect_db(db_name) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor


def insert_category(title, pages_quantity):
    connection, cursor = connect_db('texnomart.db')
    sql = 'insert into categories(title, pages_quantity) values (?,?) on conflict (title) do nothing;'
    cursor.execute(sql, (title, pages_quantity))
    connection.commit()

# написать функцию для получения category_id по title
# получить айди категории через фильтрацию по названию категории
# отдать одно значение, .fetchone()
# get_category_id(title)