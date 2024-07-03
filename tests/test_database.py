from redis import Redis


def test_redis_connection(redis_client: Redis) -> None:
    assert redis_client.ping()
    assert redis_client.set('foo', 'bar')
    assert redis_client.get('foo') == 'bar'
    assert redis_client.delete('foo')
    redis_client.close()
