from flask import abort

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

def create(item):
    brand_name = item.get("brand_name")
    quantity = item.get("quantity")
    if brand_name and quantity not in INVENTORY:
        INVENTORY[brand_name] = {
            "brand_name": brand_name,
        }
        return INVENTORY[brand_name], 201
    else:
        abort(
            406,
            f"Inventory item with name {brand_name} already exists",
        )

def read_one(brand_name):
    inventory_list = list(INVENTORY.values())
    for d in inventory_list:
        if d["brand_name"] == brand_name:
            return d["quantity"]
