from tests import CLIENT


def test_comments(video_id: str='dQw4w9WgXcQ') -> None:
    """
        Prints out first 20 pages of comments from a video.
    """

    at_page = 0
    max_pages = 5
    total_comments = 0
    np = None

    while at_page < max_pages:
        comments = CLIENT.get_comments(video_id, nextpage=np)
        at_page += 1

        print('=' * 35, f'Page: {at_page}', '=' * 35)
        for comment in comments.get_comments():
            total_comments += 1
            print(f'Comment {comment.comment_id} by "{comment.author}" ({comment.commented_time}), {comment.like_count} likes: "{comment.comment_text}"')

        if comments.nextpage == None:
            print(f"No more comments! Total: {total_comments}, expected: {max_pages * 20}")
            break

        np = comments.nextpage
    
    print(f"Okay, that's enough comments... Total: {total_comments}, expected: {max_pages * 20}")



if __name__ == '__main__':
    test_comments()
