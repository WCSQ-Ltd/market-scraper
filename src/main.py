import json
import time
import discord

from scraper.api import get_item_waiting_list
from scraper.database import create_session
from scraper.crud import list_items, find_watchlist_hits, humanize_hits
from scraper.models import Item
from scraper.notification import notify_channel_of_hits, notify_channel_heartbeat
from scraper.settings import SCRAPE_SLEEP_SECONDS, HEARTBEAT_RUN_COUNT_DIVISOR


def fetch_waiting_list(db, watchlist: dict) -> None:
    """
    Fetch waiting list and check for matches in the watchlist
    """
    waiting_list = get_item_waiting_list()
    if len(waiting_list) > 0:
        hits = find_watchlist_hits(waiting_list, watchlist)
        if len(hits) > 0:
            hits = humanize_hits(db, hits)
            notify_channel_of_hits(hits)


if __name__ == '__main__':
    # initialize database
    db = create_session()

    f = open('watchlist.json')
    watchlist = json.load(f)

    run_count = 0
    while True:
        fetch_waiting_list(db, watchlist)

        if run_count % HEARTBEAT_RUN_COUNT_DIVISOR:
            # Send heartbeat
            notify_channel_heartbeat(run_count)

        print(f'Scrape complete. Sleeping for {SCRAPE_SLEEP_SECONDS} seconds.')
        time.sleep(SCRAPE_SLEEP_SECONDS)
