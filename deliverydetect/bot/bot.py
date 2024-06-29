from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI, APIRouter

from contextlib import asynccontextmanager

from deliverydetect.core.settings import WEBHOOK_URL, WEBHOOK_PATH, BOT_TOKEN
from deliverydetect.bot.handlers import courier_rt, customer_rt


@asynccontextmanager
async def lifespan(app: FastAPI):
    dp.include_routers(courier_rt, customer_rt)
    await bot.set_webhook(WEBHOOK_URL)
    yield


app = APIRouter(lifespan=lifespan)
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@app.post(f'/{WEBHOOK_PATH}')
async def telegram_webhook(request: dict):
    update = types.Update(**request)
    await dp.feed_update(bot, update)
