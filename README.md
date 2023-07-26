## GreenatomTest

This repository provides solutions to: trainee tasks, advanced DE/backend tasks. By going to the [InternTest](https://github.com/spacefellow/GABackendTest/tree/master/InternTest) folder you can familiarize yourself with the solution to the intern task. The [src](https://github.com/spacefellow/GABackendTest/tree/master/src) folder contains the solution of the advanced task. A [link](https://drive.google.com/file/d/1x7IG94MWkaOZ_38GR5pGioUArwFsOXDX/view?usp=sharing) to the database schema is also attached.

### Set Up the app in Windows

>Download the code
```
$ git clone https://github.com/spacefellow/GABackendTest
Create .dbenv and .dev_env files in root folder
$ cd GABackendTest
```

>.dev_env contains
```
SECRET_KEY=some secret key
```

>.dbenv contains
```
DB_DRIVER=postgresql
DB_CONNECTOR=asyncpg
DB_USER=user
DB_PASS=pass
DB_HOST=localhost
DB_PORT=5432
DB_NAME=db_name
```

>Install modules VENV
```
$ python -m venv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```

>Start the app
```
Create database 'db_name' in PostgreSQL
$ alembic init migrations
$ alembic revision --autogenerate -m "initial"
$ alembic upgrade head
$ uvicorn main:app --reload
```

At this point, the app runs at http://127.0.0.1:8000/

### Start the app in Docker

>Download the code
```
$ git clone https://github.com/spacefellow/GABackendTest
Create .dbenv and .dev_env files in root folder
$ cd GABackendTest
```

>.dev_env contains
```
SECRET_KEY=some secret key
```

>.dbenv contains
```
DB_DRIVER=postgresql
DB_CONNECTOR=asyncpg
DB_USER=user
DB_PASS=pass
DB_HOST=database
DB_PORT=5432
DB_NAME=db_name
```

>Make docker images
```
$ docker-compose build
$ docker-compose up -d
```

>Create database in db container
```
$ docker-compose exec -it database psql --host database -U
$ CREATE DATABASE db_name;
```

>Create alembic migrations in the backend_container and load data into the database
```
$ docker-compose exec -it backend bash
$ alembic upgrade HEAD/revision_id
$ python base_functions.py
```

At this point, the app runs at http://localhost:8000/

### OpenAPI documentation

```
This application implements swagger for documenting endpoints.
The documentation can be accessed via the url http://.../docs
```
