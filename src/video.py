import json
import os
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Video:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YouTube-API')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_video):
        self.id_video = id_video
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=id_video
                                               ).execute()
        # printj(video_response)
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.url: str = 'https://www.youtube.com/watch?v=' + self.id_video
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']





class PLVideo(Video):
    pass

