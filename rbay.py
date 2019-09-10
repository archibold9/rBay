from item import Item
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
