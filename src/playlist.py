import json
import os
import datetime

import isodate
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class PlayList:
    api_key: str = os.getenv('YouTube-API')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_playlist):
        self.id_playlist = id_playlist
        playlist_videos = PlayList.youtube.playlistItems().list(playlistId=self.id_playlist,
                                                                part='contentDetails',
                                                                maxResults=50,
                                                                ).execute()
        self.title = playlist_videos['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.id_playlist

    def total_duration(self):
        playlist_videos = PlayList.youtube.playlistItems().list(playlistId=self.id_playlist,
                                                                part='snippet, contentDetails',
                                                                maxResults=50,
                                                                ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = PlayList.youtube.videos().list(part='contentDetails,statistics',
                                                        id=','.join(video_ids)
                                                        ).execute()

        duration = datetime.timedelta(minutes=0)
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)
        return duration

    def show_best_video(self):
        playlist_videos = PlayList.youtube.playlistItems().list(playlistId=self.id_playlist,
                                                                part='snippet, contentDetails',
                                                                maxResults=50,
                                                                ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = PlayList.youtube.videos().list(part='contentDetails,statistics',
                                                        id=','.join(video_ids)
                                                        ).execute()
        like_count = 0
        id_video = 'id'
        for video in video_response['items']:
            if like_count < int(video['statistics']['likeCount']):
                like_count = int(video['statistics']['likeCount'])
                id_video = video['id']
        return "https://youtu.be/" + id_video
