import typing as t

from tests import CLIENT
from datetime import datetime


def test_video(video_id: str='dQw4w9WgXcQ') -> None:
    """
        Prints out information about a video.
    """

    video = CLIENT.get_video(video_id)
    short_description = video.description[:100].replace('\n', '')

    print(f"""
        Video ID: {video_id}
        Title: {video.title}
        Description: {short_description}...
        Views: {video.views}

        Uploaded by: {video.uploader}
        Uploaded on: {video.upload_date} ({datetime.now().year - video.upload_date.year} years ago)

        Duration: {video.duration}
        FPS: {video.get_streams('video')[0].fps}
    """)



def test_trending(country_codes: t.List[str]=['US', 'SK', 'CN']) -> None:
    """
        Prints out trending videos for a specific country.
    """

    for country_code in country_codes:
        videos = CLIENT.get_trending(country_code)

        # Nothing ever trends in China's YouTube:
        if country_code == 'CN':
            assert len(videos) == 0
            print("\nYes, empty list works.")

        for video in videos:
            print(f"{video.uploader_name} >> {video.title} ({video.views} views)")



def test_get_audio(video_id: str='dQw4w9WgXcQ') -> None:
    """
        Prints out the first audio stream URL for a video.
    """

    video = CLIENT.get_video(video_id)
    audio_stream = video.get_streams('audio')[0]

    print(f"Audio stream URL: {audio_stream.url} ({audio_stream.mime_type})")



if __name__ == '__main__':
    test_video()
    test_trending()
    test_get_audio()
