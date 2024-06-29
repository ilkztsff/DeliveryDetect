from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncEngine
from redis import Redis
import pytest

from deliverydetect.bot.bot import app
from deliverydetect.core.database import redis, engine


@pytest.fixture
def app_client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def redis_client() -> Redis:
    return redis


@pytest.fixture
def postgres_client() -> AsyncEngine:
    return engine
