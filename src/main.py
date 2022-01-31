import json

from scraper.api import get_item_listings, get_item_listed_count_by_level
from scraper.database import create_schema, create_session


if __name__ == '__main__':
    # initialize database
    create_schema()
    db = create_session()

    f = open('watchlist.json')

    watchlist = json.load(f)
    found_list = []
    for item in watchlist['watchlist']:
        data = get_item_listings(item['itemID'])
        cnt = get_item_listed_count_by_level(data.json(), item['min_level'], item['max_level'])
        if cnt > 0:
            found_list.append(f'{cnt} listings found for {item["name"]}')

    for item in found_list:
        print(item)
