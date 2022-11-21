from flask import abort, make_response

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


# import sqlite3
# conn = sqlite3.connect("inventory.db")
# cur = conn.cursor()
# cur.execute("SELECT * FROM item")


# inventory = cur.fetchall()
# for item in inventory:
#     print(item)




# import sqlite3
# conn = sqlite3.connect("inventory.db")
# inventory = [
#     "1, 'Pepsi', '5'",
#     "2, 'Sprite', '5'",
#     "3, 'Fanta', '5'",
# ]
# for item_data in inventory:
#     insert_cmd = f"INSERT INTO item VALUES ({item_data})"
#     conn.execute(insert_cmd)


# SELECT * FROM item;



def read_all():
    inventory_list = list(INVENTORY.values())
    return [d['quantity'] for d in inventory_list if 'quantity' in d]


def read_one(brand_name):
    inventory_list = list(INVENTORY.values())
    for d in inventory_list:
        if d["brand_name"] == brand_name:
            return d["quantity"]

def update(brand_name, item):
    if brand_name in INVENTORY:
        INVENTORY[brand_name]["quantity"] = item.get("quantity", INVENTORY[brand_name]["quantity"])
        return INVENTORY[brand_name]
    else:
        abort(
            404,
            f"Item with brand name {brand_name} is out of stock"
        )