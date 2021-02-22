
import time
import random

from sqlalchemy import create_engine

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'

time.sleep(3)

db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

def add_new_row():
    # Insert a new number into the 'numbers' table.
    db.execute(f"INSERT INTO public.order(name, description, created_on) VALUES ('The name', 'Description it is!', '2004-10-19 10:23:54')")
   

while True:
    add_new_row()
    time.sleep(0.25)