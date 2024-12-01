def select_color(category: str) -> str:
    category_colors = {
        "Инвестиции и вклады": "Brown",
        "Жилье": "Pink",
        "Продукты": "Green",
        "Кафе и рестораны": "Green",
        "Тарифы и подписки": "Orange",
        "Коммунальные платежи": "Orange",
        "Транспорт": "Yellow",
        "Красота и здоровье": "Red",
        "Одежда": "Purple",
        "Учеба и хобби": "Purple",
        "Развлечения": "#Blue",
        "Переводы людям": "Blue",
        "Прочее": "Light gray",
    }

    return category_colors.get(category, 'Light gray')


if __name__ == "__main__":
    print(select_color("Прочее"))
