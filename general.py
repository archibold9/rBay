import db
import config
import poster


class Item:
    def __init__(self, title=None, desc=config.default_desc, price=None, category_id=None, images=None, posted=False):
        self.title = title
        self.desc = desc
        self.price = price
        self.category_id = category_id
        self.images = images
        self.posted = posted

    def __str__(self):
        return self.title

    def save(self):
        data = (self.title, self.price, self.category_id, self.images, self.posted)
        q_save = """
            INSERT INTO ITEMS (title, price, category_id, images_dir, posted)
            VALUES(?, ?, ?, ?, ?);
        """
        con = db.connect()
        cur = con.cursor().execute(q_save, data)
        con.commit()
        return cur.lastrowid

    def post(self):
        poster.list_item(self, "")


if __name__ == '__main__':
    i = Item(title="Merc ECU", desc="Bla bla bla", price="39.99", category_id="61525", images="a/directory/of/images", posted=False)
    i.post()
