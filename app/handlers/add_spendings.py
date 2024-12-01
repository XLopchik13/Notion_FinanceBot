from aiogram import Router, F
from aiogram.types import Message
from datetime import datetime

from app.notion_client import NotionClient
from config import settings


notion_client = NotionClient(database_id=settings.DATABASE_ID)

router = Router()


@router.message(F.text.startswith("/add"))
async def add_expense(message: Message):
    try:
        parts = message.text.split(maxsplit=3)
        if len(parts) != 4:
            await message.answer(
                'Неверный формат команды. Используй: /add "название" "стоимость" "категория"'
            )
            return

        name, price, category = parts[1], float(parts[2]), parts[3]
        current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")

        notion_client.add_expense(name, price, category)

        await message.answer(
            f"Расход '{name}' на сумму {price} добавлен в категорию '{category}' с датой {current_date}"
        )
    except ValueError as v:
        await message.answer(f"Произошла ошибка: {v}")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
