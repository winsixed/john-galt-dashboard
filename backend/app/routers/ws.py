from fastapi import APIRouter, WebSocket
import aioredis
from app.config import Settings

router = APIRouter()

@router.websocket("/ws/inventory")
async def inventory_ws(ws: WebSocket):
    await ws.accept()
    redis = await aioredis.create_redis_pool(Settings().REDIS_URL)
    res = await redis.subscribe("inventory_channel")
    ch = res[0]
    try:
        while await ch.wait_message():
            msg = await ch.get_json()
            await ws.send_json(msg)
    finally:
        await redis.unsubscribe("inventory_channel")
        await ws.close()
