import typing as t

from . import BasePipedModel


class Comments(BasePipedModel):
    class Comment(BasePipedModel):
        @property
        def author(self) -> str:
            """
                The name of the author of the comment
            """

            return self.data['author']


        @property
        def comment_id(self) -> str:
            """
                The comment ID
            """

            return self.data['commentId']


        @property
        def comment_text(self) -> str:
            """
                The text of the comment
            """

            return self.data['commentText']


        @property
        def commented_time(self) -> str:
            """
                The time the comment was made (format: `'x y ago'`).

                ### Note:
                The raw time from API also includes the `'(edited)'` suffix to mark comment as edited (if it was).
                By accessing this property, the suffix is automatically removed.
                If you for whatever reason want to keep the suffix, access this property directly via `Comment.data['commentedTime']`
            """

            time: str = self.data['commentedTime']

            return time.removesuffix(' (edited)')


        @property
        def is_edited(self) -> bool:
            """
                Whether or not the comment is edited.

                ### Note:
                This property checks whether there is `'(edited)'` in the `commentedTime` property, because that's where you get that from.
                See `Comments.Comment.commented_time`
            """

            time: str = self.data['commentedTime']

            return time.endswith('(edited)')


        @property
        def commentor_url(self) -> str:
            """
                The URL of the channel that made the comment
            """

            return self.data['commentorUrl']


        @property
        def replies_page(self) -> t.Optional[str]:
            """
                Same as `Comments.nextpage`, but to load replies.

                `None` means that there are no replies.
            """

            return self.data['repliesPage']


        @property
        def hearted(self) -> bool:
            """
                Whether or not the comment has been hearted
            """

            return self.data['hearted']


        @property
        def like_count(self) -> int:
            """
                The number of likes the comment has
            """

            return self.data['likeCount']


        @property
        def pinned(self) -> bool:
            """
                Whether or not the comment is pinned
            """

            return self.data['pinned']


        @property
        def thumbnail(self) -> str:
            """
                The thumbnail of the commentor's channel
            """

            return self.data['thumbnail']


        @property
        def verified(self) -> bool:
            """
                Whether or not the author of the comment is verified
            """

            return self.data['verified']



    def get_comments(self) -> t.List[Comment]:
        """
            Obtain a list of comments
        """

        return [self.Comment(comment_json) for comment_json in self.data['comments']]


    def __iter__(self) -> t.Iterator[Comment]:
        iter(self.get_comments())



    @property
    def disabled(self) -> bool:
        """
            Whether or not the comments are disabled
        """

        return self.data['disabled']



    @property
    def nextpage(self) -> t.Optional[str]:
        """
            A JSON encoded page, which is used for the nextpage endpoint.

            If there is no nextpage data, this returns `None`.
        """

        return self.data['nextpage']
