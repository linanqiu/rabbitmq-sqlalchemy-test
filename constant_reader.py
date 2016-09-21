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
  persons = cauldron_server.all_person.delay()
  print('%d persons' % len(persons.get()))
  addresses = cauldron_server.all_address.delay()
  print('%d addresses' % len(addresses.get()))

def read_nondb():
  nondb = cauldron_server.non_db_task.delay()
  print(nondb.get())

while(True):
  read()
  # time.sleep(1)
