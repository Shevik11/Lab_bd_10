from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'

    person_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255))
    date_of_birth = Column(Date)
    address = Column(String(255))
    phone_number = Column(String(20))
    buyer_id = Column(Integer)
    seller_id = Column(Integer)
