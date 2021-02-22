from pgnotify import await_pg_notifications
import time

print('Starting listener!')
time.sleep(3) # workaround alert! need to wait for db to bootup

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'

print('Connecting to db.')
db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)

print('Getting the events..')
for notification in await_pg_notifications(
        db_string,
        ['myEvent']):
    print(f'Got the event via channel {notification.channel}. {notification.payload}')
    time.sleep(1) # pretending to work on in (put to queue or api call)
    print('Event handled.')