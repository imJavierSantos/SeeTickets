from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float

engine = create_engine('postgresql://postgres:postgres@localhost:5438/postgres')
Base = declarative_base(metadata=MetaData(schema='see_tickets'))


class Fee(Base):
    __tablename__ = 'fee'

    id = Column(Integer(), primary_key=True)
    value = Column(Float(), nullable=False)
    currency = Column(String(50), nullable=False)


class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer(), primary_key=True)
    name = Column(String(150), nullable=False)
    fee_id = Column(Integer(), ForeignKey('Fee.id'))


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    name = Column(String(150), nullable=False)
    fee_id = Column(Integer(), ForeignKey('Fee.id'))


class EventProduct(Base):
    __tablename__ = 'event_product'

    event_id = Column(Integer(), ForeignKey('Events.id'), primary_key=True)
    product_id = Column(Integer(), ForeignKey('Products.id'), primary_key=True)


Session = sessionmaker(engine)
session = Session()