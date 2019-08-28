from ebaysdk.trading import Connection
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import Config
import json

# URGENT TODO add support for images
def list(item, images):
    api = Connection(config_file="ebay.yaml", debug=Config.debug, siteid=3)
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
            "Description": "{}".format(item.description),
            "ListingDuration": "Days_10",
            "StartPrice": "{}".format(item.price),
            "Currency": "GBP",
            "ReturnPolicy": {
                "ReturnsAcceptedOption": "ReturnsNotAccepted",
            },
            # "PictureDetails":{
            #     "PictureURL": "https://www.tomsturgeon.co.uk/img/test.jpeg"
            # },
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


    

