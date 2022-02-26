import typing as t

from requests import Session

from .models import BasePipedModel
from .models.comments import Comments


_MDL = t.TypeVar('_MDL', bound=BasePipedModel)



class PipedClient:
    """
        An API client for [Piped](https://piped.kavin.rocks).
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



    def _get_json(self, uri: str, as_model: t.Optional[_MDL]=None, **kwargs) -> t.Union[_MDL, t.Dict[str, t.Any]]:
        """
            Obtains JSON data from specific URI of the Piped API.

            ### Parameters:
            - `uri` - The URI to get JSON data from
            - `as_model` - The `BasePipedModel` to load the JSON data into. If this is `None`, the JSON data is returned as a `dict`.
            - `**kwargs` - Additional keyword arguments to pass to `requests.Session.get`
        """

        json = self.session.get(f"{self.base_api_url}{uri}", **kwargs).json()

        if as_model is not None:
            return as_model(json)

        return json



    def get_comments(self, video_id: str, nextpage: t.Optional[t.Dict[str, t.Optional[str]]]=None) -> Comments:
        """
            Gets a list of comments for a specific video.

            ### Parameters:
            - `video_id` - The ID of the video to get comments for
            - `nextpage` - Nextpage data, obtained from `.models.comments.Comments.nextpage` property. If this is `None`, the first page of comments is returned.
                There are often 20 comments per page.
        """

        if nextpage is not None:
            return self._get_json(f"/nextpage/comments/{video_id}", Comments, params={"nextpage": nextpage})

        else:
            return self._get_json(f"/comments/{video_id}", Comments)
