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



if __name__ == '__main__':
    test_video()
