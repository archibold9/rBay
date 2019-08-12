from General import Item
import Poster
import Data_Processor
import Config
import os
from Utilities import bcolors

# Clear the top of the window
print(bcolors.CLEAR_SCREEN + bcolors.WHITE)
Config.listing_directory = input("Enter relative location of ebay listings:  ")
Config.subfolders = [dI for dI in os.listdir(Config.listing_directory) 
						if os.path.isdir(os.path.join(Config.listing_directory,dI))]

# Data_Processor.start()

i1 = Item("Incomplete/Audi_A-LINE_Rim_Tyre/item_data.json")

Poster.list(i1)