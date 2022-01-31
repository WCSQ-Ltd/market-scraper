import sqlalchemy as db

from scraper.database import Base


class Item(Base):
    __tablename__ = 'scraper_item'

    id = db.Column(db.Integer, primary_key=True)

    game_id = db.Column(db.String)
    name = db.Column(db.String)
