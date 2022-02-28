from tests import CLIENT

from datetime import timedelta
from random import choice


def test_channel_by_id(channel_id: str='UCuAXFkgsw1L7xaCfnd5JJOw') -> None:
    """
        Prints out information about a channel by its ID.
    """

    channel = CLIENT.get_channel_by_id(channel_id)

    video_id =  channel.uploaded_videos[0].url.removeprefix('/watch?v=')
    likes = CLIENT.get_video(video_id).likes

    print(f"Total likes for last video of {channel.name}: {likes}")



def test_channel_by_name(channel_name: str='SusanWojcicki') -> None:
    """
        Prints out information about a channel by its ID.
    """

    channel = CLIENT.get_channel_by_name(channel_name)

    print(f"""
        Channel ID: {channel.id}
        Name: {channel.name}
        Description: {channel.description}
        Subscriber count: {channel.subscriber_count}
    """)



def test_get_watchtime_trending() -> None:
    """
        Prints out the total watchtime for recent videos of a random trending channel 
    """

    trending_channel_id = choice(CLIENT.get_trending('SK')).uploader_url.removeprefix('/channel/')
    trending_channel = CLIENT.get_channel_by_id(trending_channel_id)


    total_watchtime = timedelta(milliseconds=0)

    for video in trending_channel.uploaded_videos:
        total_watchtime += video.duration

    print(f"Total watchtime for recent {len(trending_channel.uploaded_videos)} videos of {trending_channel.name} (https://youtube.com/channel/{trending_channel.id}): {total_watchtime}")



if __name__ == '__main__':
    test_channel_by_name()
    test_channel_by_id()
    test_get_watchtime_trending()
