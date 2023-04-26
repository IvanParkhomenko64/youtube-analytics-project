import json
import os
import isodate
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import datetime

#from src.playlist import PlayList

if __name__ == '__main__':
    # pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    # assert pl.title == "Редакция. АнтиТревел"
    # assert pl.url == "https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb"
    #
    # duration = pl.total_duration
    # assert str(duration) == "3:41:01"
    # assert isinstance(duration, datetime.timedelta)
    # assert duration.total_seconds() == 13261.0
    #
    # assert pl.show_best_video() == "https://youtu.be/9Bv2zltQKQA"

    api_key: str = os.getenv('YouTube-API')
    youtube = build('youtube', 'v3', developerKey=api_key)

    id_playlist = 'PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'
    playlist_videos = youtube.playlistItems().list(playlistId=id_playlist,
                                                            part='snippet, contentDetails',
                                                            maxResults=50,
                                                            ).execute()


    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))




    playlists = youtube.playlists().list(channelId='UC1eFXmJNkjITxPFWTy6RsWg',
                                         part='contentDetails,snippet',
                                         maxResults=50,
                                         ).execute()

    #channel = youtube.playlists().list(id='PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb', part='snippet,statistics', maxResults=50).execute()

    #printj(playlist_videos)
    video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
    video_response = youtube.videos().list(part='contentDetails,statistics',
                                           id=','.join(video_ids)
                                           ).execute()
    printj(video_response)
    duration = datetime.timedelta(minutes=0)
    for video in video_response['items']:
        # YouTube video duration is in ISO 8601 format
        iso_8601_duration = video['contentDetails']['duration']
        duration += isodate.parse_duration(iso_8601_duration)
    print(duration)
