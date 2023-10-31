import scrapetube
from yt_concate.settings import API_KEY

print(API_KEY)
def get_video_id(channel_id):
    base_video_url = 'https://www.youtube.com/watch?v='
    videos = scrapetube.get_channel(channel_id)

    for video in videos:
        video1 = video['videoId']
        url = base_video_url + video1
        print(url)

CHANNEL_ID = 'UCZd4BcnCEHzfrWoMKRaxPTQ'
# get_video_id(CHANNEL_ID)
