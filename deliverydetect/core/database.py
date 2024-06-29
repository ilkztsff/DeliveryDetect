from sqlalchemy.ext.asyncio import create_async_engine
from redis import Redis

from deliverydetect.core.settings import DATABASE_URL, REDIS_HOST, REDIS_PASSWORD, REDIS_PORT


redis = Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
engine = create_async_engine(DATABASE_URL)
