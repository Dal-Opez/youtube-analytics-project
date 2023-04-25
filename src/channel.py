import os
import json
from googleapiclient.discovery import build

api_key: str = os.environ['YT_API_KEY']

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = channel["items"][0]["snippet"]["title"]
        self.description = channel["items"][0]["snippet"]["description"]
        self.url = channel["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        self.subscriberCount = channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = channel["items"][0]["statistics"]["videoCount"]
        self.viewCount = channel["items"][0]["statistics"]["viewCount"]

    @property
    def channel_id(self):
        return self.channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # создаем специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def to_json(self, file_path):
        dump_dict = {"channel_id": self.__channel_id,
                     "title": self.title,
                     "description": self.description,
                     "customUrl": self.url,
                     "subscriberCount": self.subscriberCount,
                     "video_count": self.video_count,
                     "viewCount": self.viewCount}
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(dump_dict, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=api_key)

