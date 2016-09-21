import time
import random

from celery import Celery

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_tables import Address, Base, Person

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

app = Celery(backend='rpc://', broker='amqp://')
app.config_from_object('celery_config')

session = DBSession()

@app.task
def add_person(message):
  new_person = Person(name='new person')
  session.add(new_person)
  new_address = Address(post_code='00000', person=new_person)
  session.add(new_address)
  session.commit()

@app.task
def all_person():
  session = DBSession()
  persons = session.query(Person).all()
  return persons

@app.task
def all_address():
  session = DBSession()
  addresses = session.query(Address).all()
  return addresses

@app.task
def non_db_task():
  return random.random()
