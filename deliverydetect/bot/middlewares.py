from aiogram import Bot
from aiogram.enums import ChatType
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import TelegramObject

from redis.asyncio import Redis

from typing import Callable, Awaitable, Union, Dict, Any


class PrivateChatsMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Union[Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], None]:

        if event.model_dump()['chat']['type'] != ChatType.PRIVATE:
            return None

        return await handler(event, data)


class FloodMiddleware(BaseMiddleware):
    def __init__(self, redis: Redis, bot: Bot) -> None:
        self.redis = redis
        self.bot = bot

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:

        event_model = event.model_dump()

        try:
            user = event_model['from_user']['id']
        except KeyError:
            return None

        check = await self.redis.get('user')

        if check is None:
            await self.redis.set(user, 1, 5)
            return await handler(event, data)
        elif int(check) == 1:
            await self.redis.set(user, 0, 1)
            return await self.bot.send_message(text='Не спамить!! Вы заблокированы на 5 секунд', chat_id=int(event_model['chat']['id']))
        else:
            return None
