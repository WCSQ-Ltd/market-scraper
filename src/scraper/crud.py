import typing

from scraper.database import SessionLocal
from scraper.models import Item


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
