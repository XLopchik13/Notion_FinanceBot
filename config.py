import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    NOTION_TOKEN: str
    BOT_TOKEN: str
    DATABASE_ID: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "", ".env")
    )


settings = Settings()

headers = {
    "Authorization": "Bearer " + settings.NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}
