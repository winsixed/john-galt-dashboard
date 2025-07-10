import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.mark.asyncio
async def test_inventory_ws(client: TestClient):
    with client.websocket_connect("/ws/inventory") as ws:
        import aioredis
        redis = await aioredis.create_redis_pool("redis://redis:6379/0")
        await redis.publish_json("inventory_channel", {"name": "test", "count": 1, "timestamp": "now"})
        msg = ws.receive_json(timeout=5)
        assert msg["name"] == "test"
