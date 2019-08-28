import os
from Utilities import bcolors
import json
import Config
from ebaysdk.trading import Connection

def print_listings():
	print(bcolors.WARNING + "\nFound {} possible listings\n".format(len(Config.subfolders)))
	for x in Config.subfolders:
		print(bcolors.HEADER + "    + " + x)
	print("")

def start_listing():
	for item in Config.subfolders:
		print(bcolors.WHITE)
		data = populate_data_list(item)
		if(Config.debug):
			print("\n\n{}".format(data))
		save_to_json(data, item)
		print(bcolors.OKGREEN + "\nSuccessfully saved item data!\n\n")

def populate_data_list(item):
	data = {}
	data["title"] = str(raw_input("Enter title for listing: [{}]:   ".format(item)) or item)
	data["description"] = str(raw_input("Enter description for listing: [{}...]  ".format(Config.default_desc[:20])) or Config.default_desc)
	data["price"] = str(raw_input("Enter price:   "))	
	data["category_id"] = categories_picker(data["title"])
	data["images"] = get_images(item)
	data["posted"] = "false"
	return data



def get_images(directory):
	return [os.path.join(Config.listing_directory+"/"+directory+"/"+img) for img in os.listdir(Config.listing_directory +"/"+directory) if img.endswith(".jpg") or img.endswith(".png")]
        
def save_to_json(data, directory):
	save_loc = Config.listing_directory + "/" + directory
	with open(save_loc + "/item_data.json", 'w') as output:
		if(Config.debug):
			print("\nSaving JSON file to {}".format(save_loc))
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

	return str(raw_input("\nEnter Category number: "))
    

def start():
	print_listings()
	start_listing()

	





