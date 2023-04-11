import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YouTube-API')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = "вДудь"
        self.description = "Здесь задают вопросы"
        self.url = "https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA"
        self.subscriberCount = "10300000"
        self.videoCount = "163"
        self.viewCount = "1925259492"

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, file_name) -> None:
        channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        with open(file_name, 'w') as f:
            json.dump(channel, f)


