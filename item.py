from sqlalchemy import Column, Integer, DECIMAL, Text, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    auction_id = Column(Integer, ForeignKey('auctions.auction_id'))
    lot_number = Column(Integer)
    start_price = Column(DECIMAL(10, 2))
    short_description = Column(Text)
    sale_price = Column(DECIMAL(10, 2))
    seller_id = Column(Integer)
    buyer_id = Column(Integer)

    auction = relationship('Auction')
    seller_index = Index('seller_index', seller_id)
    buyer_index = Index('buyer_index', buyer_id)
