# david_rrhh_project

## 1- Create a env

    python -m venv env

## 2- activate env

    source env/bin/activate
  
## 3- Install requirements

    pip install -r requirements/common.txt

## 4- load env variables (example vars)

    export DB_NAME=rrhh_admin
    export DB_USER=postgres
    export DB_PASSWORD=postgres
    export DB_HOST=localhost
    export DB_PORT=5432

## 5- Migrate Database

    python manage.py makemigrations
    python manage.py migrate

## 6- Create superuser

    python manage.py createsuperuser

## 7- runserver

    python manage.py runserver 0.0.0.0:8000

