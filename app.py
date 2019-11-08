from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask,request,jsonify

Base = declarative_base()

class Product(Base):
    __tablename__  = 'dbo.products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

engine = create_engine('sqlite:///foo.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
product = Product()
session.add(product)
allProducts = len(session.query(Product).all())
session.commit()

session.close();