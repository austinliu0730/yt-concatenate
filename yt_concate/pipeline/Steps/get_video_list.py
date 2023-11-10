import scrapetube

from yt_concate.pipeline.Steps.step import Step, StepException


class GetVideoList(Step):
    def process(self, data, inputs):
        if 'channel_id' not in inputs:
            raise StepException("在輸入中缺少 'channel_id'")

        channel_id = inputs['channel_id']
        base_video_url = 'https://www.youtube.com/watch?v='
        video_list = []

        try:
            videos = scrapetube.get_channel(channel_id)
        except KeyError:
            raise StepException("擷取影片ID時出錯")

        for video in videos:
            video_id = video.get('videoId')
            if video_id:
                url = base_video_url + video_id
                video_list.append(url)

        print(f"總影片數量：{len(video_list)}")

        return video_list
