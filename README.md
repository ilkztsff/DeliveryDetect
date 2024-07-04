<div align="center">
    <a href="https://github.com/ilkztsff/DeliveryDetect/blob/dev/LICENSE">
      <img src="https://img.shields.io/github/license/ilkztsff/DeliveryDetect?label=License&color=purple&style=for-the-badge">
    </a>
    <a href="https://github.com/ilkztsff/DeliveryDetect/blob/dev/pyproject.toml">
      <img src="https://img.shields.io/badge/python-3.11.9-purple?style=for-the-badge">
    </a>
    <a href="https://github.com/ilkztsff/DeliveryDetect/actions/workflows/check.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/ilkztsff/DeliveryDetect/check.yml?branch=dev&style=for-the-badge&label=linter&color=purple">
    </a>
    <img src="https://img.shields.io/codeclimate/coverage/ilkztsff/DeliveryDetect?style=for-the-badge&label=coverage&color=purple">
</div>

<h1 align="center">DeliveryDetect</h1>


## ✍ About

Telegram bot for free couriers and customers


## 🛠 Build commands

Required to have `git`, `make`, `python`, `docker` и `docker-compose` installed

Download project from GitHub
```bash
git clone https://github.com/ilkztsff/DeliveryDetect/
```
<br>

Build docker container
```bash
make build
```
<br>

Run project
```bash
make start
```
<br>

Run project in background mode
```bash
make up
```
<br>

Stop all containers
```bash
make stop
```
<br>

Remove all containers and data
```bash
make rm
```
<br>

Generate postgres database revision
```bash
make revision
```
<br>

Upgrade database(use `head` as a revision name for latest one)
```bash
make upgrade revision=<revision name>
```
<br>

Downgrade database
```bash
make downgrade revision=<revision name>
```
<br>

Install dependencies
```bash
make install
```
<br>

Update dependencies
```bash
make update
```
<br>

Lint the project
```bash
make lint
```
<br>

Run *black*
```bash
make fix
```
<br>

Run all tests
```bash
make test
```
<br>

See test coverage
```bash
make coverage
```
<br>


## 🖥 Enviromental variables

All required enviromental variables are below. Examples [here](https://github.com/ilkztsff/DeliveryDetect/blob/dev/.env.example)

- `HOST` - server host

- `BOT_TOKEN` - telegram bot token, get it from [@BotFather](https://t.me/BotFather)

- `WEB_SERVER_URL` - url of a web server for getting updates from telegram

- `REDIS_HOST` - host for connecting to redis

- `REDIS_PORT` - port for redis database

- `REDIS_PASSWORD` - password for redis database

- `POSTGRES_PORT` - port for postgres database

- `POSTGRES_USER` - username for postgres database

- `POSTGRES_PASSWORD` - password for postgres database

- `POSTGRES_DB` - name for postgres database


## 💿 [Dependencies](https://github.com/ilkztsff/DeliveryDetect/blob/dev/pyproject.toml)

- **[aiogram](https://pypi.org/project/aiogram/) - 3.8.0**

- **[fastapi](https://pypi.org/project/fastapi/) - 0.111.0**

- **[asyncpg](https://pypi.org/project/asyncpg/) - 0.29.0**

- **[sqlalchemy](https://pypi.org/project/sqlalchemy/) - 2.0.31**

- **[redis](https://pypi.org/project/redis/) - 5.0.7**

- **[alembic](https://pypi.org/project/alembic/) - 1.13.2**

- **[python-dotenv](https://pypi.org/project/python-dotenv/) - 1.0.1**

- **[uvicorn](https://pypi.org/project/uvicorn/) - 0.30.1**

- **[mypy](https://pypi.org/project/mypy/) - 1.10.1**

- **[flake8](https://pypi.org/project/flake8/) - 7.1.0**

- **[coverage](https://pypi.org/project/coverage/) - 7.5.4**

- **[pytest](https://pypi.org/project/pytest/) - 8.2.2**

- **[pytest-asyncio](https://pypi.org/project/pytest-asyncio/) - 0.23.7**

- **[pytest-dependency](https://pypi.org/project/pytest-dependency/) - 0.6.0**

- **[black](https://pypi.org/project/black/) - 24.4.2**

