from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

INVENTORY = {
    "Pepsi": {
        "name": "Pepsi",
        "quantity": 5,
        "timestamp": get_timestamp(),
    },
    "Dr. Pepper": {
        "name": "Dr. Pepper",
        "quantity": 5,
        "timestamp": get_timestamp(),
    },
    "Mountain Dew": {
        "name": "Mountain Dew",
        "quantity": 5,
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return list(INVENTORY.values())