from ebaysdk.trading import Connection

def list(item):
#    api = Connection(config_file="ebay.yaml", domain="api.sandbox.ebay.com", debug=True)
    request = {
        "Item": {
            "Title": f"{item.title}",
            "Country": "UK",
            "Location": "UK",
            "Site": "UK",
            "ConditionID": "1000",
            "PaymentMethods": "PayPal",
            "PayPalEmailAddress": "tomsturgeon8@gmail.com",
            "PrimaryCategory": {"CategoryID": f"{item.category_id}"},
            "Description": f"{item.description}",
            "ListingDuration": "Days_10",
            "StartPrice": f"{item.price}",
            "Currency": "GBP",
            "ReturnPolicy": {
                "ReturnsAcceptedOption": "ReturnsAccepted",
                "RefundOption": "MoneyBack",
                "ReturnsWithinOption": "Days_30",
                "Description": "If you are not satisfied, return the keyboard.",
                "ShippingCostPaidByOption": "Buyer"
            },
            "ShippingDetails": {
                "ShippingServiceOptions": {
                    "FreeShipping": "True",
                    "ShippingService": "USPSMedia"
                }
            },
            "DispatchTimeMax": "3"
        }
    }

    print(request)
    # api.execute("AddItem", request)
