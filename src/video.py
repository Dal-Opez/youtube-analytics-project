import os
from googleapiclient.discovery import build

api_key: str = os.environ['YT_API_KEY']


class Video:
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=self.video_id).execute()
        self.title = video_response["items"][0]["snippet"]["title"]
        self.url = 'https://www.youtube.com/watch?v=' + self.video_id
        self.viewCount = video_response["items"][0]["statistics"]["viewCount"]
        self.likeCount = video_response["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
