from datetime import datetime

import requests
from typing import Dict, List

from app.utils import select_color
from config import headers, settings


class NotionClient:
    def __init__(self, database_id: str):
        self.database_id = database_id

    @staticmethod
    def add_expense(name: str, price: float, category: str):
        url = 'https://api.notion.com/v1/pages'

        data = {
            "Name": {"title": [{"text": {"content": name}}]},
            "Price": {"number": price},
            "Category": {"multi_select": [{"name": category}]}
        }

        payload = {"parent": {"database_id": settings.DATABASE_ID}, "properties": data}
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response

    @staticmethod
    def get_expenses() -> List[Dict]:
        url = f'https://api.notion.com/v1/databases/{settings.DATABASE_ID}/query'
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        results = response.json().get("results", [])

        return [
            {
                "properties": result["properties"],
            }
            for result in results
        ]
