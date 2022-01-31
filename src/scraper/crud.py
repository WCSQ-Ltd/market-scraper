import typing
from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs

from scraper.database import SessionLocal
from scraper.models import Item
from scraper.utils import build_bdo_codex_item_url


def list_items(db: SessionLocal) -> typing.List[Item]:
    db_items = db.query(Item).all()
    return db_items


def create_item(db: SessionLocal, data: dict) -> Item:
    db_item = Item(**data)
    db.add(db_item)
    db.commit()
    return db_item


def get_item_by_game_id(db: SessionLocal, item_game_id: str) -> Item:
    db_item = db.query(Item).filter(Item.game_id == item_game_id)
    if db_item.count() > 0:
        return db_item.first()
    raise Exception('Item not found.')


def serialize_item_list(item_list: list) -> list:
    """
    Converts item list from API response format to a more readable list of dictionaries
    """
    items = []
    for item in item_list:
        time_to_list_dt = datetime.fromtimestamp(item[3])
        time_to_list_str = time_to_list_dt.strftime('%m/%d/%Y, %H:%M:%S')
        data = {
            'item_id': item[0],
            'item_level': item[1],
            'time_to_list': time_to_list_str,
        }
        items.append(data)
    return items


def get_or_create_item_name_from_bdocodex(db: SessionLocal, item_game_id: str) -> Item:
    item = None
    url = build_bdo_codex_item_url(item_game_id)
    resp = requests.get(url)
    if resp.status_code == 200:
        # Found, save in db
        soup = bs(resp.text, 'html')
        title = soup.select_one('span[class^="item_title"]').text.strip()

        try:
            # This may look like it's redundant usage from `humanize_hits`, but this fn might get
            # used on other fns, so we'll still check for item saved in the db
            item = get_item_by_game_id(db, item_game_id)
            # update item name
            item.name = title
            db.commit()
        except Exception:
            # TODO: bruh this really needs to be a better exception
            # Save as a new item
            item = Item(name=title, game_id=item_game_id)
            db.add(item)
            db.commit()
    return item


def humanize_hits(db, hits: list) -> list:
    """
    Make item hits more readable for humans. Add item name into data.
    """
    items = []
    hits = serialize_item_list(hits)
    for item in hits:
        item_game_id = item['item_id']
        try:
            db_item = get_item_by_game_id(db, item_game_id)
            item['name'] = db_item.name
            items.append(item)
        except Exception:
            db_item = get_or_create_item_name_from_bdocodex(db, item_game_id)
            # Item not found in db, fetch from bdocodex
            item['name'] = db_item.name
            items.append(item)
    return items


def find_watchlist_hits(waiting_list: list, watchlist: dict) -> list:
    hits = []
    watchlist = watchlist['watchlist']
    for waiting_item in waiting_list:
        wait_id = waiting_item[0]
        wait_level = waiting_item[1]
        time_to_list = waiting_item[3]
        time_to_list_dt = datetime.fromtimestamp(time_to_list)

        match = next(
            (item for item in watchlist if wait_id == item['itemID'] and wait_level == item['min_level']),
            None
        )
        if match:
            hits.append(waiting_item)
    return hits
