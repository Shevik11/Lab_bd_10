# auction.py
from sqlalchemy import Column, Integer, Date, Time, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Auction(Base):
    __tablename__ = 'auctions'

    auction_id = Column(Integer, primary_key=True, autoincrement=True)
    auction_date = Column(Date)
    auction_time = Column(Time)
    location = Column(String(255))
    features = Column(Text)
