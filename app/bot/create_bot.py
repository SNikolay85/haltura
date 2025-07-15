from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import NEW_TBOT, ADMIN_ID

bot = Bot(token=NEW_TBOT, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def start_bot():
    try:
        await bot.send_message(ADMIN_ID, f'Я запущен🥳.')
    except:
        pass


async def stop_bot():
    try:
        await bot.send_message(ADMIN_ID, 'Бот остановлен. За что?😔')
    except:
        pass
