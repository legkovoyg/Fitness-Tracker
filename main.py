import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv
import os
import keyboards.keyboards as kb
import handlers.handlers as hrs
import random

load_dotenv()
bot = Bot(os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # type: ignore


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await hrs.dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
