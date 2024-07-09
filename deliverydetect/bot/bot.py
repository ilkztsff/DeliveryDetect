from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest
from fastapi import FastAPI, APIRouter

from contextlib import asynccontextmanager

from deliverydetect.core.settings import WEBHOOK_URL, WEBHOOK_PATH, BOT_TOKEN
from deliverydetect.core.database import redis
from deliverydetect.bot.handlers import courier_rt, customer_rt
from deliverydetect.bot.keyboards import choose_role_ikb
from deliverydetect.bot.middlewares import PrivateChatsMiddleware, FloodMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    dp.message.middleware(PrivateChatsMiddleware())
    dp.message.middleware(FloodMiddleware(redis, bot))
    dp.include_routers(courier_rt, customer_rt)
    await bot.set_webhook(WEBHOOK_URL)
    yield
    await redis.aclose()
    await bot.delete_webhook(drop_pending_updates=True)


app = APIRouter(lifespan=lifespan)
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@app.post(f'/{WEBHOOK_PATH}', include_in_schema=False)
async def telegram_webhook(request: dict):
    update = types.Update(**request)
    try:
        await dp.feed_update(bot, update)
    except TelegramBadRequest:
        pass


@dp.message(Command('start'))
async def start(msg: types.Message):
    await msg.reply('Кто вы?', reply_markup=choose_role_ikb)
