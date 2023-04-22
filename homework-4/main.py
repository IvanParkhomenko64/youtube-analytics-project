import json
import os
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

from src.video import Video, PLVideo

api_key: str = os.getenv('YouTube-API')
youtube = build('youtube', 'v3', developerKey=api_key)
video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id='9lO06Zxhu88'
                                       ).execute()

if __name__ == '__main__':
    # Создаем два экземпляра класса
   #video1 = Video('9lO06Zxhu88')  # '9lO06Zxhu88' - это id видео из ютуб
    #video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    #assert str(video1) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
   #assert str(video2) == 'Пушкин: наше все?'
    print(json.dumps(video_response, indent=2, ensure_ascii=False))



