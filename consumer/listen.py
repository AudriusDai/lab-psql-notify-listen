from pgnotify import await_pg_notifications
import time

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'

db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)

time.sleep(3)

for notification in await_pg_notifications(
        db_string,
        ['myEvent']):

    print(notification.channel)
    print(notification.payload)