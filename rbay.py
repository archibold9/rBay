from general import Item
import poster
import item_processor
import config
import os
import sys
from ebaysdk.trading import Connection
from PIL import Image


def init():
    # TODO change to absolute location
    config.listing_directory = raw_input("Enter relative location of ebay listings:  ")
    config.subfolders = [dI for dI in os.listdir(config.listing_directory)
                         if os.path.isdir(os.path.join(config.listing_directory, dI))]





# def upload_images(item):
#     api = Connection(config_file="ebay.yaml", domain="api.sandbox.ebay.com", debug=Config.debug, siteid=3)
#     img_urls = []
#     count = 0
#     for img in item.__dict__["images"]:
#         print("Uploading images... {}/{}".format(count, len(item.__dict__["images"])))
#         count += 1
#
#         files = {
#             "file": (img, open(img, 'rb')),
#         }
#
#         picture_data = {
#             "WarningLevel": "High",
#             "PictureName": "an_image"
#         }
#
#         res = api.execute('UploadSiteHostedPictures', picture_data, files=files).dict()
#
#         img_urls.append(res["SiteHostedPictureDetails"]["FullURL"])
#
#     return img_urls

if __name__ == '__main__':
    # User must have specified an argument
    if len(sys.argv) > 1:
        if sys.argv[1] == 'add':
            init()
            item_processor.start()
    else:
        print("""
            USAGE: python rbay <action>
            
            <actions> = {add, list}
        """)
