import typing as t

from . import BasePipedModel
from .videos import Video



class NextPageChannel(BasePipedModel):
    """
        Represents a channel obtained via the `nextpage` endpoint.

        This model contains only `nextpage` and `relatedStreams`. It's a parent for `Channel`.
    """

    @property
    def nextpage(self) -> str:
        """
            A JSON encoded string to be passed to the `'nextpage'` endpoint(s) when
            obtaining paginated data.
        """

        return self.data['nextpage']


    @property
    def uploaded_videos(self) -> t.List[Video.RelatedStream]:
        """
            List of uploaded videos from the current fetched data

            There are max. 30 videos per page
        """

        return [Video.RelatedStream(video_data) for video_data in self.data['relatedStreams']]



class Channel(NextPageChannel):
    """
        Represents a YouTube channel.

        Contains properties of `NextPageChannel`.
    """

    @property
    def id(self) -> str:
        """
            The channel's ID
        """

        return self.data['id']


    @property
    def name(self) -> str:
        """
            The channel's name
        """

        return self.data['name']


    @property
    def avatar_url(self) -> str:
        """
            The channel's avatar URL
        """

        return self.data['avatarUrl']


    @property
    def banner_url(self) -> str:
        """
            The channel's banner URL
        """

        return self.data['bannerUrl']


    @property
    def description(self) -> str:
        """
            The channel's description
        """

        return self.data['description']


    @property
    def subscriber_count(self) -> int:
        """
            The number of subscribers the channel has
        """

        return self.data['subscriberCount']


    @property
    def verified(self) -> bool:
        """
            Whether or not the channel is verified by YouTube (has a badge)
        """

        return self.data['verified']
