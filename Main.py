from General import Item
import Poster
import Data_Processor
import Config
import os
from Utilities import bcolors
from ebaysdk.trading import Connection
import requests
from xml.etree import ElementTree
from PIL import Image

# Clear the top of the window
print(bcolors.CLEAR_SCREEN + bcolors.WHITE)

# TODO
options = {"Prepare", "List"}

def init():
	Config.listing_directory = raw_input("Enter relative location of ebay listings:  ")
	Config.subfolders = [dI for dI in os.listdir(Config.listing_directory) 
							if os.path.isdir(os.path.join(Config.listing_directory,dI))]

def prep_items():
	Data_Processor.start()

def post_items():
	for x in Config.subfolders:	
		i = Item(Config.listing_directory + "/" + x + "/item_data.json")
		print(i)

		if(i.__dict__["posted"] == "true"):
				print(bcolors.WARNING + "This item may already be listed. Are you sure you want to continue?" )

		ans = raw_input("\n\nReady to list? [Yy/Nn]")

		if(ans.lower() == "y"):
			Poster.list(i, upload_images(i))
			i.setPosted()
		else:
			continue

def upload_images(item):
	api = Connection(config_file="ebay.yaml", domain="api.sandbox.ebay.com", debug=Config.debug, siteid=3)
	imgURLS = []
	count = 0
	for img in item.__dict__["images"]:
		print("Uploading images... {}/{}".format(count, len(item.__dict__["images"])))
		count += 1
		
		files = {
			"file" : (img, open(img, 'rb')),
		}

		pictureData = {
			"WarningLevel": "High",
			"PictureName": "an_image"
		}

		res = api.execute('UploadSiteHostedPictures', pictureData, files=files).dict()

		imgURLS.append(res["SiteHostedPictureDetails"]["FullURL"])

	return imgURLS

init()
# prep_items()
post_items()





