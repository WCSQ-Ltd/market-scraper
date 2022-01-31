import json

from scraper.api import get_item_waiting_list
from scraper.database import create_session
from scraper.crud import list_items, find_watchlist_hits, humanize_hits
from scraper.models import Item
from scraper.notification import notify_user_of_hits


def fetch_waiting_list(db, watchlist: dict) -> None:
    """
    Fetch waiting list and check for matches in the watchlist
    """
    waiting_list = get_item_waiting_list()
    if len(waiting_list) > 0:
        hits = find_watchlist_hits(waiting_list, watchlist)
        if len(hits) > 0:
            hits = humanize_hits(db, hits)
            notify_user_of_hits(hits)



if __name__ == '__main__':
    # initialize database
    db = create_session()

    f = open('watchlist.json')
    watchlist = json.load(f)

    fetch_waiting_list(db, watchlist)

    # found_list = []
    # for item in watchlist['watchlist']:
    #     data = get_item_listings(item['itemID'])
    #     cnt = get_item_listed_count_by_level(data.json(), item['min_level'], item['max_level'])
    #     if cnt > 0:
    #         found_list.append(f'{cnt} listings found for {item["name"]}')

    # for item in found_list:
    #     print(item)
