from aiogram import Bot, Dispatcher

from app.handlers.add_spendings import router as add_router
from app.handlers.show_spendings import router as show_router
from app.handlers.start_router import router as start_router
from config import settings


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(add_router)
dp.include_router(show_router)


if __name__ == "__main__":
    dp.run_polling(bot)
