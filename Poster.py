from ebaysdk.trading import Connection
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# URGENT TODO add support for images
def list(item):
    api = Connection(config_file="ebay.yaml", debug=True, siteid=3)
    request = {
        "Item": {
            "Title": f"{item.title}",
            "Country": "GB",
            "Location": "England",
            "Site": "UK",
            # This is new, used, etc 3000 is 'used'
            # TODO add an option to specify this for parts etc
            "ConditionID": "3000",
            "PaymentMethods": "PayPal",
            "PayPalEmailAddress": "tomsturgeon8@gmail.com",
            "PrimaryCategory": {
                "CategoryID": f"{item.category_id}",
            },
            "Description": f"{item.description}",
            "ListingDuration": "Days_10",
            "StartPrice": f"{item.price}",
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
    if(Config.debug):
        res = api.execute("VerifyAddItem", request)
    else:
        res = api.execute("AddItem", request)


    

