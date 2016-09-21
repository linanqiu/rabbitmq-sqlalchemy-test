import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_tables import Address, Base, Person

import cauldron_server

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

def write():
  print('writing')
  cauldron_server.add_person.delay()

def read():
  persons = cauldron_server.all_person()
  print('%d persons' % len(persons))
  addresses = cauldron_server.all_address()
  print('%d addresses' % len(addresses))

while(True):
  read()
  time.sleep(1)
