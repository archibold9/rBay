from ebaysdk.exception import ConnectionError

import db
import config
import poster
import config
from ebaysdk.trading import Connection
import glob
from PIL import Image


class Item:
    def __init__(self, title=None, desc=config.default_desc, price=None, category_id=None, img_dir=None, posted=False):
        self.title = title
        self.desc = desc
        self.price = price
        self.category_id = category_id
        self.img_dir = img_dir
        self.posted = posted
        self.image_url_arr = []

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

    def upload_images(self):
        for filename in glob.glob('{}*.jpg'.format(self.img_dir)):
            try:
                api = Connection(config_file=config.yaml_location, domain="api.ebay.com", debug=config.debug, siteid=config.site_id)

                # pass in an open file
                # the Requests module will close the file
                files = {'file': ('EbayImage', open(filename, 'rb'))}

                picture_data = {
                    "WarningLevel": "High",
                    "PictureName": "Item_img"
                }

                res = api.execute('UploadSiteHostedPictures', picture_data, files=files).dict()
                self.image_url_arr.append(res["SiteHostedPictureDetails"]["FullURL"])
            except ConnectionError as e:
                print(e)
                print(e.response.dict())


if __name__ == '__main__':
    i = Item(title="Merc ECU", desc="Bla bla bla", price="39.99", category_id="61525", img_dir="Incomplete/Mercedes "
                                                                                               "ECU E230/",
             posted=False)
    i.upload_images()
    i.post()

