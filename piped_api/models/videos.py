import typing as t

from datetime import datetime, date, timedelta

from . import BasePipedModel


class Video(BasePipedModel):
    @property
    def title(self) -> str:
        """
            The title/name of the video
        """

        return self.data['title']


    @property
    def description(self) -> str:
        """
            The description of the video
        """

        return self.data['description']


    @property
    def upload_date(self) -> date:
        """
            The date the video was uploaded at.

            ### Note:
            Use `Video.data['uploadDate']` to get the raw string that was obtained from the API - this package
            automatically converts the raw string to a `datetime.date` object.
        """

        raw = self.data['uploadDate']

        return datetime.strptime(raw, r"%Y-%m-%d").date()


    @property
    def uploader(self) -> str:
        """
            The channel name of the author of the video
        """

        return self.data['uploader']


    @property
    def uploader_url(self) -> str:
        """
            The URI to the author's channel
        """

        return self.data['uploaderUrl']


    @property
    def uploader_avatar(self) -> str:
        """
            The URL to the video author's avatar image
        """

        return self.data['uploaderAvatar']


    @property
    def thumbnail_url(self) -> str:
        """
            The URL to the video's thumbnail image
        """

        return self.data['thumbnail']


    @property
    def hls(self) -> t.Optional[str]:
        """
            The hls manifest URL, to be used for Livestreams
        """

        return self.data['hls']


    @property
    def dash(self) -> t.Optional[str]:
        """
            The dash manifest URL for OTF streams
        """

        return self.data['dash']


    @property
    def lbry_id(self) -> str:
        """
            The lbry id of the video, if available. I assume this has something to do with https://lbry.com/
        """

        return self.data['lbryId']


    @property
    def uploader_verified(self) -> str:
        """
            Whether or not the channel that uploaded the video is verified by YouTube (badge)
        """

        return self.data['uploaderVerified']


    @property
    def duration(self) -> timedelta:
        """
            The duration of the video.

            ### Note:
            The original value from the API was in seconds (`Video.data['duration']`), but this package
            converts it to a `datetime.timedelta` object.
        """

        return timedelta(seconds=self.data['duration'])


    @property
    def views(self) -> int:
        """
            The number of views the video has received
        """

        return self.data['views']


    @property
    def likes(self) -> int:
        """
            The amount of likes the video has received. `-1` if hidden
        """

        return self.data['likes']


    @property
    def dislikes(self) -> int:
        """
            The amount of dislikes the video has received. `-1` if hidden

            ### Note:
            This is obsolete since YouTube did a tiny gigantical little big whoopsie with their like system and screwed it all up
            You can use awesome user-made projects such as https://returnyoutubedislike.com to obtain the dislike count
        """

        return self.data['dislikes']



    class Stream(BasePipedModel):
        """
            Either an audio or video stream of a video
        """

        @property
        def url(self) -> str:
            """
                The URL of the stream
            """

            return self.data['url']


        @property
        def format(self) -> str:
            """
                The format of the stream (`'M4A' or 'WEBMA_OPUS' or 'MPEG_4' or 'WEBM' or 'v3GPP'`
                
                No, I don't know how many are there or what does each mean
            """

            return self.data['format']


        @property
        def quality(self) -> str:
            """
                The standard quality we all know and love (e. g.: `'240p'` for video or `'128k'` for audio)
            """

            return self.data['quality']


        @property
        def mime_type(self) -> str:
            """
                If you come from web development (or other invidious area that works with these French mimes),
                then you already know what this is. If not, consider [checking the Mozilla documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)
            """

            return self.data['mimeType']


        @property
        def codec(self) -> str:
            """
                What is this? I don't know. A codec?
            """

            return self.data['codec']


        @property
        def video_only(self) -> bool:
            """
                Whether or not the stream is video only (AKA. muted video)
            """

            return self.data['videoOnly']


        @property
        def bitrate(self) -> int:
            """
                The bitrate of the stream
            """

            return self.data['bitrate']


        @property
        def init_start(self) -> int:
            """
                Not sure what this does, but it seems to be useful for creating dash streams
            """

            return self.data['initStart']


        @property
        def init_end(self) -> int:
            """
                Not sure what this does, but it seems to be useful for creating dash streams
            """

            return self.data['initEnd']


        @property
        def index_start(self) -> int:
            """
                Not sure what this does, but it seems to be useful for creating dash streams
            """

            return self.data['indexStart']


        @property
        def index_end(self) -> int:
            """
                Not sure what this does, but it seems to be useful for creating dash streams
            """

            return self.data['indexEnd']


        @property
        def width(self) -> int:
            """
                The width of the stream. `'0'` for audio streams (makes sense)
            """

            return self.data['width']


        @property
        def height(self) -> int:
            """
                The height of the stream. `'0'` for audio streams (makes sense)
            """

            return self.data['width']


        @property
        def fps(self) -> int:
            """
                Frames Per Second. This is usually `'0'` for audio and `'30'` or `'60'` for video
            """

            return self.data['fps']


    def get_streams(self, type: t.Literal['video', 'audio']='video') -> t.List[Stream]:
        """
            Get the streams of a video.

            ### Parameters:
            - `type` - The type of stream to get. Either `'video'` or `'audio'`
        """

        if type == 'video' or type == 'audio':
            return [self.Stream(stream_data) for stream_data in self.data[f"{type}Streams"]]

        raise ValueError('Invalid stream type. Must be either `video` or `audio`')



    class RelatedStream(BasePipedModel):
        """
            A related stream (e. g.: related video to the current one from the right sidebar, video related to/uploaded by a channel and trending video).
        """

        @property
        def url(self) -> str:
            """
                The URL to the related video
            """

            return self.data['url']
        

        @property
        def title(self) -> str:
            """
                The title of the related video
            """

            return self.data['title']
        

        @property
        def thumbnail(self) -> str:
            """
                The thumbnail URL of the related video
            """

            return self.data['thumbnail']
        

        @property
        def uploader_name(self) -> str:
            """
                The name of the channel that uploaded the related video
            """

            return self.data['uploaderName']
        

        @property
        def uploader_url(self) -> str:
            """
                The URL of the channel that uploaded the related video
            """

            return self.data['uploaderUrl']
        

        @property
        def uploader_avatar(self) -> str:
            """
                The URL of the channel's avatar
            """

            return self.data['uploaderAvatar']


        @property
        def uploaded_date(self) -> str:
            """
                The date the related video was uploaded (format: `'x y ago'`)
            """

            return self.data['uploadedDate']
        

        @property
        def short_description(self) -> t.Optional[str]:
            """
                The short description of the related video. As far as I know, this is always `None` - perhaps some unused YouTube feature?
            """

            return self.data['shortDescription']


        @property
        def duration(self) -> timedelta:
            """
                The duration of the related video.

                ### Note:
                The original value from the API was in seconds (`Video.data['duration']`), but this package
                converts it to a `datetime.timedelta` object.
            """

            return timedelta(seconds=self.data['duration'])


        @property
        def views(self) -> str:
            """
                The amount of views the related video has received
            """

            return self.data['views']


        @property
        def uploaded(self) -> datetime:
            """
                The date the related video was uploaded (as a `datetime.datetime` object).

                ### Note:
                The original value was in milliseconds since epoch (`Video.data['uploaded']`), but this package converts it to a `datetime.datetime` object.
            """

            return datetime.fromtimestamp(self.data['uploaded'] / 1000)


        @property
        def uploader_verified(self) -> bool:
            """
                Whether or not the channel that uploaded the related video is verified by YouTube (e. g.: has badge)
            """

            return self.data['uploaderVerified']



    @property
    def related_videos(self) -> t.List[RelatedStream]:
        """
            List of related streams
        """

        return [self.RelatedStream(video_data) for video_data in self.data['relatedStreams']]



    class Subtitle(BasePipedModel):
        @property
        def url(self) -> str:
            """
                The URL to the subtitle
            """

            return self.data['url']


        @property
        def mime_type(self) -> str:
            """
                If you come from web development (or other invidious area that works with these French mimes),
                then you already know what this is. If not, consider [checking the Mozilla documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)
            """

            return self.data['mimeType']


        @property
        def name(self) -> str:
            """
                The name of the language the captions are in
            """

            return self.data['name']


        @property
        def code(self) -> str:
            """
                The country code for the captions
            """

            return self.data['code']


        @property
        def auto_generated(self) -> bool:
            """
                Whether or not the captions are auto-generated by YouTube
            """

            return self.data['autoGenerated']



    @property
    def subtitles(self) -> t.List[Subtitle]:
        """
            A list of captions for the video
        """

        return [self.Subtitle(subtitle_data) for subtitle_data in self.data['subtitles']]


    @property
    def livestream(self) -> bool:
        """
            Whether or not the video is a livestream
        """

        return self.data['livestream']


    @property
    def proxy_url(self) -> str:
        """
            The base URL for Piped proxy
        """

        return self.data['proxyUrl']



    class Chapter(BasePipedModel):
        """
            A video chapter (or "section").

            YouTube displays a list of chapters, if there are timestamps in the description.
        """

        @property
        def title(self) -> str:
            """
                The title of the chapter
            """

            return self.data['title']


        @property
        def image(self) -> str:
            """
                The image URL for the chapter
            """

            return self.data['image']


        @property
        def start(self) -> timedelta:
            """
                The start time of the chapter

                ### Note:
                The original value from the API was in seconds, this package automatically converts it to `datetime.timedelta`
            """

            return timedelta(seconds=self.data['start'])



    @property
    def chapters(self) -> t.List[Chapter]:
        """
            A list of chapters for the video
        """

        return [self.Chapter(chapter_data) for chapter_data in self.data['chapters']]
