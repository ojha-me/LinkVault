# Makefile for LinkVault backend

.PHONY: install run migrate superuser test # phony targets tells make that there are not files in future there wont be any conflicts 

install:
	poetry install

run:
	poetry run python manage.py runserver

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

superuser:
	poetry run python manage.py createsuperuser

test:
	poetry run python manage.py test