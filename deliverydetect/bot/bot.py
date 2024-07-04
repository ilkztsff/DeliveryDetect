from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from fastapi import FastAPI, APIRouter

from contextlib import asynccontextmanager

from deliverydetect.core.settings import WEBHOOK_URL, WEBHOOK_PATH, BOT_TOKEN
from deliverydetect.core.database import redis
from deliverydetect.bot.handlers import courier_rt, customer_rt
from deliverydetect.bot.keyboards import choose_role_ikb
from deliverydetect.bot.middlewares import PrivateChatsMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    dp.message.middleware(PrivateChatsMiddleware())
    dp.include_routers(courier_rt, customer_rt)
    await bot.set_webhook(WEBHOOK_URL)
    yield
    await redis.aclose()
    await bot.delete_webhook(drop_pending_updates=True)


app = APIRouter(lifespan=lifespan)
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@app.post(f'/{WEBHOOK_PATH}')
async def telegram_webhook(request: dict):
    update = types.Update(**request)
    await dp.feed_update(bot, update)


@dp.message(Command('start'))
async def start(msg: types.Message):
    await msg.reply('Кто вы?', reply_markup=choose_role_ikb)
