# main.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from auction import Base, Auction
from dao import GenericDAO

# Створення двигуна та сесії
engine = create_engine('sqlite:///new_auction.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Використання GenericDAO для таблиці auctions
auction_dao = GenericDAO(session, Auction)
# auction = auction_dao.create(auction_date='2023-01-01', auction_time='12:00', location='Some Location', features='Some Features')
auction = auction_dao.get(1)
print(auction.auction_id)

# # Використання GenericDAO для таблиці persons
# person_dao = GenericDAO(session, Person)
# person = person_dao.create(full_name='John Doe', date_of_birth='1990-01-01', address='Some Address', phone_number='123-456-7890')
# print(person.person_id)
#
# # Використання GenericDAO для таблиці items
# item_dao = GenericDAO(session, Item)
# item = item_dao.create(auction_id=auction.auction_id, lot_number=1, start_price=100.0, short_description='Item Description', sale_price=150.0, seller_id=person.person_id, buyer_id=None)
# print(item.item_id)
