import json
import discord

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
