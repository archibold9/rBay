from general import Item
from utilities import b_colors
import config
from ebaysdk.trading import Connection

API = Connection(config_file=config.yaml_location, debug=config.debug, siteid=config.site_id)


def start():
    print("\nFound {} possible listings\n".format(len(config.subfolders)))
    for x in config.subfolders:
        print( "    + " + x)
    print("")
    for from_file in config.subfolders:
        create_item(from_file)


def create_item(from_file):
    title = str(raw_input("Enter title for listing: [{}]:   ".format(from_file)) or from_file)
    desc = str(
        raw_input("Enter description for listing: [{}...]  ".format(config.default_desc[:20])) or config.default_desc)
    price = str(raw_input("Enter price:   "))
    category = get_categories(title)
    images = config.parent_directory + "/" + from_file
    item = Item(title=title, desc=desc, price=price, category_id=category, images=images, posted=False)
    if item.save() is not None:
        print("Successfully added item to local database.")
    else:
        raise Exception("Something went wrong when adding to the database")


def get_categories(title):
    print("\n\nRequesting Suggested Categories....\n")
    query = {
        "Query": title
    }

    res = API.execute('GetSuggestedCategories', query).dict()
    categories = res["SuggestedCategoryArray"]["SuggestedCategory"]

    for x in categories:
        print("    + " + x["Category"]["CategoryName"] + "\t(" + x["Category"][
            "CategoryID"] + ")")

    return str(raw_input("\nEnter Category number: "))


if __name__ == '__main__':
    pass
