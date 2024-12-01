from datetime import datetime

from aiogram import Router, F
from aiogram.types import Message

from app.notion_client import NotionClient
from config import settings


notion_client = NotionClient(database_id=settings.DATABASE_ID)

router = Router()


@router.message(F.text.startswith("/view"))
async def view_expenses(message: Message):
    try:
        parts = message.text.split(maxsplit=1)
        if len(parts) != 2 or parts[1] not in {"date", "category", "price"}:
            await message.answer(
                "Неверный формат команды. Используй: /view [date|category|price]"
            )
            return

        sort_by = parts[1]
        expenses = notion_client.get_expenses()

        parsed_expenses = []
        for expense in expenses:
            properties = expense["properties"]

            date_obj = datetime.strptime(properties["Date"]["created_time"], "%Y-%m-%dT%H:%M:%S.%fZ")
            formatted_date = date_obj.strftime("%B %d, %Y %H:%M")

            parsed_expenses.append({
                "name": properties["Name"]["title"][0]["text"]["content"],
                "price": properties["Price"]["number"],
                "category": properties["Category"]["multi_select"][0]["name"],
                "date": formatted_date,
            })

        if sort_by == "date":
            parsed_expenses.sort(key=lambda x: x["date"], reverse=True)
        elif sort_by == "price":
            parsed_expenses.sort(key=lambda x: x["price"], reverse=True)
        elif sort_by == "category":
            parsed_expenses.sort(key=lambda x: x["category"])

        if not parsed_expenses:
            await message.answer("Нет добавленных расходов.")
            return

        result = "\n".join(
            [
                f'{i+1}. {e["name"]} – {e["price"]} рублей ({e["category"]}, {e["date"]})'
                for i, e in enumerate(parsed_expenses)
            ]
        )
        await message.answer(f"Список расходов:\n\n{result}")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
