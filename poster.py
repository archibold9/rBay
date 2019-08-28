from ebaysdk.trading import Connection
from bs4 import BeautifulSoup
import config
import db


def get_items_from_db(already_posted=False):
    con = db.connect()
    cur = con.cursor()
    if already_posted:
        return cur.execute("SELECT * FROM ITEMS").fetchall()
    else:
        return cur.execute("SELECT * FROM ITEMS WHERE posted = 0").fetchall()


def list_item(item, images):
    api = Connection(config_file=config.yaml_location, debug=config.debug, siteid=config.site_id)
    request = {
        "Item": {
            "Title": "{}".format(item.title),
            "Country": "GB",
            "Location": "England",
            "Site": "UK",
            # This is new, used, etc 3000 is 'used'
            # TODO add an option to specify this for parts etc
            "ConditionID": "3000",
            "PaymentMethods": "PayPal",
            "PayPalEmailAddress": "tomsturgeon8@gmail.com",
            "PrimaryCategory": {
                "CategoryID": "{}".format(item.category_id),
            },
            "Description": "{}".format(item.desc),
            "ListingDuration": "Days_10",
            "StartPrice": "{}".format(item.price),
            "Currency": "GBP",
            "ReturnPolicy": {
                "ReturnsAcceptedOption": "ReturnsNotAccepted",
            },
            "ShippingDetails": {
                "ShippingServiceOptions": {
                    "FreeShipping": "True",
                    "ShippingService": "UK_RoyalMailSecondClassStandard"
                }
            },
            "DispatchTimeMax": "3"
        }
    }

    # If debug mode then only use verify add item else use real add item api call
    if config.debug:
        api.execute("VerifyAddItem", request)
    else:
        api.execute("AddItem", request)


if __name__ == '__main__':
    print(get_items_from_db()[0]['title'])
