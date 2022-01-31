import requests

from .settings import MARKET_URL, HEADERS
from .constants import ITEM_LIST_PATH, WAITHING_LIST_PATH


def get_item_waiting_list():
    waiting_path = f'{MARKET_URL}{WAITHING_LIST_PATH}'
    resp = requests.post(waiting_path)
    return resp


def get_item_listings(item_id: str):
    listings_path = f'{MARKET_URL}{ITEM_LIST_PATH}'
    data = {
        'mainKey': item_id,
        'keyType': 0,
    }

    resp = requests.post(listings_path, headers=HEADERS,  data=data)
    return resp


def get_item_listed_count_by_level(listings: dict, min_level: int, max_level: int) -> int:
    listings = listings['resultMsg']
    listings = listings.split('|')

    current_stock_idx = 4
    min_lvl_idx = 1
    max_lvl_idx = 2

    listings = [[int(s) for s in data.split('-') if len(s)] for data in listings]
    try:
        match = next(data for data in listings if data[min_lvl_idx] == min_level and data[max_lvl_idx] == max_level)
        return match[current_stock_idx]
    except StopIteration:
        return 0
