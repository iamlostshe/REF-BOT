'Скрипт запуска бота'

from os import getenv
import asyncio

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
from loguru import logger

from handlers import routers
from utils import db

# Загружаем TOKEN из .env
load_dotenv()
TOKEN = getenv('TOKEN')

# Инициализируем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main() -> None:
    'Запуск бота'

    # Подключаем файл под логи
    logger.add('log.log')

    # Подключаем роутеры
    for r in routers:
        logger.info('Include router: {} ...', r.name)
        dp.include_router(r)

    # Проверяем наличае бд
    await db.check_db()

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
