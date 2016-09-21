from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_tables import Address, Base, Person

import cauldron_server

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

def write():
  print('writing')
  cauldron_server.add_person.delay('adding person lolol')

def read():
  session = DBSession()
  persons = session.query(Person).all()
  print('%d persons' % len(persons))
  addresses = session.query(Address).all()
  print('%d addresses' % len(addresses))

write()
write()
read()
read()
write()
read()
