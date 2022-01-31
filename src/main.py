import json

from scraper.api import get_item_listings, get_item_listed_count_by_level
from scraper.database import create_session
from scraper.crud import list_items
from scraper.models import Item


def fetch_waiting_list(db):
    pass


if __name__ == '__main__':
    # initialize database
    db = create_session()

    f = open('watchlist.json')

    # watchlist = json.load(f)
    # found_list = []
    # for item in watchlist['watchlist']:
    #     data = get_item_listings(item['itemID'])
    #     cnt = get_item_listed_count_by_level(data.json(), item['min_level'], item['max_level'])
    #     if cnt > 0:
    #         found_list.append(f'{cnt} listings found for {item["name"]}')

    # for item in found_list:
    #     print(item)
