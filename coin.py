from flask import abort, make_response

COIN = {
    "coin": 0
}

def get_coins():
    return COIN["coin"]

def get_coin_headers():
    return {
        "X-Coins": f'{get_coins()}'
    }

def update_coins(coins_added):
    coin_obj = COIN
    coin_obj['coin'] += coins_added


def delete(brand_name):
    if get_coins() >= 1:

        return make_response(
            f"{brand_name} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"no coins in machine"
        )
