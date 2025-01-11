import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.handlers import router
import json
from dotenv import load_dotenv
import os
import time

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    while True:
        try:
            logging.info("Запуск бота...")
            asyncio.run(main())
        except Exception as e:
            logging.error(f"Ошибка: {e}")
            time.sleep(5)  # Задержка перед перезапуском
        except KeyboardInterrupt:
            logging.info("Выход из программы.")
            break