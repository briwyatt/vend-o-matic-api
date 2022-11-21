from flask import abort, make_response
from coin import COIN, update_coins

INVENTORY = {
    "Pepsi": {
        "brand_name": "Pepsi",
        "quantity": 5,
    },
    "Sprite": {
        "brand_name": "Sprite",
        "quantity": 5,
    },
    "Fanta": {
        "brand_name": "Fanta",
        "quantity": 5,
    }
}



def read_all():
    inventory_list = list(INVENTORY.values())
    return [d['quantity'] for d in inventory_list if 'quantity' in d]


def read_one(brand_name):
    inventory_list = list(INVENTORY.values())
    for d in inventory_list:
        if d["brand_name"] == brand_name:
            return d["quantity"]

def update(brand_name, item):
    if brand_name in INVENTORY and COIN['coin'] >= 2:
        update_coins(-2)
        INVENTORY[brand_name]["quantity"] = item.get("quantity", INVENTORY[brand_name]["quantity"])
        return INVENTORY[brand_name]
    elif COIN['coin'] < 2:
        abort(
            403,
            f"number of coins for payment are insufficient"
            )
    else:
        abort(
            404,
            f"Item with brand name {brand_name} is out of stock"
        )