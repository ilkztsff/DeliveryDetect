FROM python:3.11.9

WORKDIR /deliverydetect

COPY . /deliverydetect/

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install


CMD ["poetry", "run", "uvicorn", "deliverydetect.bot.bot:app", "--host", "0.0.0.0", "--port", "8000", "--log-config=log_config.ini", "--log-level=debug", "--reload", "--reload-dir", "."]

EXPOSE 8000
