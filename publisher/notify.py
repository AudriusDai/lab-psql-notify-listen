
import time
import random
from sqlalchemy import create_engine

print('Starting publisher!')
time.sleep(3)  # workaround alert! need to wait for db to bootup

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'

print('Connecting to db.')
db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

print('Working..')
while True:
    db.execute(f"INSERT INTO public.order(name, description, created_on) VALUES ('The name', 'Description it is!', '2004-10-19 10:23:54')")
    print('Record inserted.')
    time.sleep(0.5)
    