from General import Item
import Poster
import Data_Processor
import Config
import os
from Utilities import bcolors
from ebaysdk.trading import Connection

# Clear the top of the window
print(bcolors.CLEAR_SCREEN + bcolors.WHITE)

# TODO
options = {"Prepare", "List"}

def init():
	Config.listing_directory = input("Enter relative location of ebay listings:  ")
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

		ans = input("\n\nReady to list? [Yy/Nn]")

		if(ans.lower() == "y"):
			i.setPosted()
			Poster.list(i)
		else:
			continue

init()
prep_items()
post_items()



