import json
import os
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


# from googleapiclient.errors import HttpError

class HttpError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Некорректный id'


class Video:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YouTube-API')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_video):
        self.id_video = id_video
        try:
            video_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                        id=id_video
                                                        ).execute()
            if not video_response['items']:  # проверка на пустой словарь
                raise HttpError
        except HttpError:
            self.video_title = self.url = self.view_count = self.like_count = None
        else:
            video_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                        id=id_video
                                                        ).execute()
            # printj(video_response)
            self.video_title: str = video_response['items'][0]['snippet']['title']
            self.url: str = 'https://www.youtube.com/watch?v=' + self.id_video
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_title


class PLVideo(Video):
    def __init__(self, id_video, id_playlist) -> None:
        super().__init__(id_video)
        self.id_playlist = id_playlist
