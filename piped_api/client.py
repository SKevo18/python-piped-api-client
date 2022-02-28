import typing as t

from requests import Session

from .models import BasePipedModel
from .models.comments import Comments
from .models.videos import Video
from .models.channels import NextPageChannel, Channel


_MDL = t.TypeVar('_MDL', bound=t.Type[BasePipedModel])


class APIError(Exception): """Raised when an API call fails"""



class PipedClient:
    """
        An API client for [Piped](https://piped.kavin.rocks).

        See also [Piped API docs](https://piped-docs.kavin.rocks/docs)
    """

    def __init__(self, base_api_url: str='https://pipedapi.kavin.rocks', session: t.Type[Session]=Session()) -> None:
        """
            ### Parameters:
            - `base_api_url` - The base URL to the instance's API. Trailing slashes will be stripped.
            - `session` - A class/subclass of `requests.Session` to use for all requests.
                For example, you could use [requests-cache](https://pypi.org/project/requests-cache/) to make all requests cacheable.
        """

        self.base_api_url = base_api_url.strip("/")
        self.session =  session



    def _get_json(self, uri: str, as_model: t.Optional[_MDL]=None, **kwargs) -> t.Union[_MDL, t.Dict[str, t.Any], t.List[t.Any]]:
        """
            Obtains JSON data from specific URI of the Piped API.

            ### Parameters:
            - `uri` - The URI to get JSON data from
            - `as_model` - The `BasePipedModel` to load the JSON data into. If this is `None`, the JSON data is returned as a `dict`.
            - `**kwargs` - Additional keyword arguments to pass to `requests.Session.get`
        """

        json: t.Union[dict, list] = self.session.get(f"{self.base_api_url}{uri}", **kwargs).json()

        if isinstance(json, dict) and json.get('error', None) is not None:
            raise APIError(f"Error: {json['error']}")

        if as_model is not None:
            return as_model(json)

        return json


    def get_video(self, video_id: str, **kwargs) -> Video:
        """
            Gets information about a specific video.

            ### Parameters:
            - `video_id` - The ID of the video to get information for
            - `**kwargs` - Additional keyword arguments to pass to `requests.Session.get`

            [Piped Documentation](https://piped-docs.kavin.rocks/docs/api-documentation/#streamsvideoid)
        """

        return self._get_json(f"/streams/{video_id}", Video, **kwargs)


    def get_comments(self, video_id: str, nextpage: t.Optional[t.Dict[str, t.Optional[str]]]=None, **kwargs) -> Comments:
        """
            Gets a list of comments for a specific video.

            ### Parameters:
            - `video_id` - The ID of the video to get comments for
            - `nextpage` - Nextpage data, obtained from `.models.comments.Comments.nextpage` property. If this is `None`, the first page of comments is returned.
                There are often 20 comments per page.
            - `**kwargs` - Additional keyword arguments to pass to `requests.Session.get`

            [Piped Documentation](https://piped-docs.kavin.rocks/docs/api-documentation/#commentsvideoid)
        """

        if nextpage is not None:
            kwargs.update({'params': {'nextpage': nextpage}})
            return self._get_json(f"/nextpage/comments/{video_id}", Comments, **kwargs)

        return self._get_json(f"/comments/{video_id}", Comments, **kwargs)


    def get_trending(self, country_code: str='US', **kwargs) -> t.List[Video.RelatedStream]:
        """
            Obtains trending videos for a specific country. If there are no trending videos (or `country_code` is invalid),
            an empty list is returned.

            ### Parameters:
            - `country_code` - The country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)) to get trending videos for. This is automatically capitalized by this package,
                since Piped for some reason doesn't accept lowercase country codes. Note: countries such as China or North Korea don't have trending videos, so they will always return an empty list.
            - `**kwargs` - Additional keyword arguments to pass to `requests.Session.get`

            [Piped Documentation](https://piped-docs.kavin.rocks/docs/api-documentation/#trending)
        """

        kwargs.update({'params': {'region': country_code.upper()}})

        return [Video.RelatedStream(trending_video) for trending_video in self._get_json(f"/trending", **kwargs)]


    def get_channel_by_id(self, channel_id: str, nextpage: t.Optional[t.Dict[str, t.Optional[str]]]=None, **kwargs) -> t.Union[NextPageChannel, Channel]:
        """
            Gets information about a specific channel by its ID.

            ### Parameters:
            - `channel_id` - The ID of the channel to get information for
            - `**kwargs` - Additional keyword arguments to pass to `requests.Session.get`

            [Piped Documentation](https://piped-docs.kavin.rocks/docs/api-documentation/#channelchannelid)
        """

        if nextpage is not None:
            kwargs.update({'params': {'nextpage': nextpage}})
            return self._get_json(f"/nextpage/channel/{channel_id}", NextPageChannel, **kwargs)

        return self._get_json(f"/channel/{channel_id}", Channel, **kwargs)



    def get_channel_by_name(self, channel_name: str, **kwargs) -> Channel:
        """
            Gets information about a specific channel by its name.

            ### Parameters:
            - `channel_name` - The name of the channel to get information for
            - `**kwargs` - Additional keyword arguments to pass to `requests.Session.get`

            [Piped Documentation](https://piped-docs.kavin.rocks/docs/api-documentation/#cname)
        """

        return self._get_json(f"/c/{channel_name}", Channel, **kwargs)


    def get_search_suggestions(self, search_query: str, **kwargs) -> t.List[str]:
        """
            Obtains search suggestions for a query.

            ### Parameters:
            - `search_query` - The query to get search suggestions for
            - `**kwargs` - Additional keyword arguments to pass to `requests.Session.get`

            [Piped Documentation](https://piped-docs.kavin.rocks/docs/api-documentation/#suggestions)
        """

        kwargs.update({'params': {'query': search_query}})

        return self._get_json(f"/suggestions", **kwargs)
