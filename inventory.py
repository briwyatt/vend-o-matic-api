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
