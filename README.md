# Project
PoC for PostgresSQL Notify/Listen functionality.

For local setup you'll have to have a docker installed. Run these commands on root level:
```
docker-compose up

# or --build for force rebuild the images
docker-compose up --build
```
Destroy setup:
```
docker-compose down
```

# Functionality
[postgres](postgres) - runs database with migrations scripts. Migration contains table and trigger which NOTIFIES the event.

[publisher](publisher) - connects to db and does the INSERT to table periodically.

[listener](listener) - connects to db and LISTENS to events published by trigger.

 NOTIFY/LISTEN works as a "fanout to queues". Each event listener receives same message that was published.

# Cons
- If `listener` is down the events are lost. There is no queue in this functionality.
- The triggers must be manually set onto table to NOTIFY the event.
