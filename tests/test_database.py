from redis import Redis
import pytest


@pytest.mark.asyncio
async def test_redis_connection(redis_client: Redis) -> None:
    assert await redis_client.ping()
    assert await redis_client.set('foo', 'bar')
    assert await redis_client.get('foo') == 'bar'
    assert await redis_client.delete('foo')
    await redis_client.aclose()
