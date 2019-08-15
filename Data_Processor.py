import os
from Utilities import bcolors
import json
import Config
from ebaysdk.trading import Connection

def print_listings():
	print(bcolors.WARNING + f"\nFound {len(Config.subfolders)} possible listings\n")
	for x in Config.subfolders:
		print(bcolors.HEADER + "    + " + x)
	print("")

def start_listing():
	for item in Config.subfolders:
		print(bcolors.WHITE)
		data = populate_data_list(item)
		if(Config.debug):
			print(f"\n\n{data}")
		save_to_json(data, item)
		print(bcolors.OKGREEN + "\nSuccessfully saved item data!\n\n")

def populate_data_list(item):
	data = {}
	data["title"] = str(input(f"Enter title for listing: [{item}]:   ") or item)
	data["description"] = str(input(f"Enter description for listing: [{Config.default_desc[:20]}...]  ") or Config.default_desc)
	data["price"] = str(input("Enter price:   "))	
	data["category_id"] = categories_picker(data["title"])
	data["images"] = get_images(item)
	return data



def get_images(directory):
	return [os.path.join(Config.listing_directory+"/"+directory+"/"+img) for img in os.listdir(Config.listing_directory +"/"+directory) if img.endswith(".jpg") or img.endswith(".png")]
        
def save_to_json(data, directory):
	save_loc = Config.listing_directory + "/" + directory
	with open(save_loc + "/item_data.json", 'w') as output:
		if(Config.debug):
			print(f"\nSaving JSON file to {save_loc}")
		json.dump(data, output)

def categories_picker(query_string):
	print(bcolors.WARNING + "\n\nRequesting Suggested Categories....\n")
	query = {
	    "Query": query_string
	}    

	api = Connection(config_file="ebay.yaml", debug=False, siteid=3)
	res = api.execute('GetSuggestedCategories', query).dict()
	categories = res["SuggestedCategoryArray"]["SuggestedCategory"]

	for x in categories:
	    print(bcolors.HEADER + "    + " + x["Category"]["CategoryName"] + bcolors.OKGREEN + "\t(" + x["Category"]["CategoryID"] + ")")

	return str(input("\nEnter Category number: "))
    

def start():
	print_listings()
	start_listing()

	





