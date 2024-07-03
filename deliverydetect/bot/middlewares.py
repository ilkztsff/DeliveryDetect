from aiogram.enums import ChatType
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import TelegramObject

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
