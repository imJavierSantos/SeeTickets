# See Tickets

## How to run the app
You should run the app and the database with the docker compose.
```
docker-compose build
docker-compose up
```

You should run this script to create the database and insert the data
```
cat ./scripts.sql | docker exec -i postgres psql -U postgres
```

After this, you are ready tu run the flask app.

http://localhost:5001/



