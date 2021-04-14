# FastAPI Project

### Create Virtual
```sh
virtualenv -p python3 venv
source env/bin/active
```

### Install requirements
```sh
sudo apt install python3-pip
pip3 install -r requirements.txt 
```

### Migrations
```sh
alembic init alembic
alembic revision --autogenerate -m "Added initial tables"
alembic upgrade head
```

### Run app (DEV)
```sh
uvicorn main:app --reload
```

### Docs Api
http://localhost:8000/docs
http://localhost:8000/redoc

