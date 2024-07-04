build:
	poetry run docker-compose build

start:
	poetry run docker-compose up --force-recreate --remove-orphans

up:
	poetry run docker-compose up --force-recreate --remove-orphans -d

stop:
	poetry run docker-compose stop

rm:
	poetry run docker-compose rm
	sudo rm -rf db

revision:
	poetry run alembic revision --autogenerate -m $(name)

upgrade:
	poetry run alembic upgrade $(revision)

downgrade:
	poetry run alembic downgrade $(revision)

update:
	poetry update

lint:
	poetry run flake8
	poetry run mypy -p deliverydetect

fix:
	poetry run black deliverydetect

test:
	poetry run docker-compose -f docker-compose.test.yml up --remove-orphans -d
	poetry run pytest
	poetry run docker-compose -f docker-compose.test.yml stop

coverage:
	poetry run coverage report
