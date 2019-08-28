import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'items.sqlite3')


def connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    # Use v efficient Row DS from sqlite that allows easy dict access on query return
    con.row_factory = sqlite3.Row
    return con


tables = {
    "t_items": """
    CREATE TABLE ITEMS (
        item_id INTEGER PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        desc VARCHAR(255),
        price VARCHAR(20) NOT NULL,
        category_id VARCHAR(30) NOT NULL,
        images_dir VARCHAR(255) NOT NULL,
        posted INTEGER);
    """
}


def create_tables():
    for x in tables:
        connect().cursor().execute(tables.get(x))


def drop_table(name):
    connect().cursor().execute("DROP TABLE {}".format(name))


def select_all(name):
    return connect().cursor().execute("SELECT * FROM {}".format(name)).fetchall()


if __name__ == '__main__':
    print(select_all("ITEMS"))
