from flask import abort

INVENTORY = {
    "Pepsi": {
        "name": "Pepsi",
        "quantity": 5,
    },
    "Dr. Pepper": {
        "name": "Dr. Pepper",
        "quantity": 5,
    },
    "Mountain Dew": {
        "name": "Mountain Dew",
        "quantity": 5,
    }
}

def read_all():
    inventory_list = list(INVENTORY.values())
    return [d['quantity'] for d in inventory_list if 'quantity' in d]

def create(item):
    name = item.get("name")
    quantity = item.get("quantity")
    if name and quantity not in INVENTORY:
        INVENTORY[name] = {
            "name": name,
        }
        return INVENTORY[name], 201
    else:
        abort(
            406,
            f"Inventory item with name {name} already exists",
        )