from tests import CLIENT


def test_channel_by_id(channel_id: str='UCuAXFkgsw1L7xaCfnd5JJOw') -> None:
    """
        Prints out information about a channel by its ID.
    """

    channel = CLIENT.get_channel_by_id(channel_id)
    assert channel.id == channel_id

    print(f"""
        Channel ID: {channel_id}
        Name: {channel.name}
        Description: {channel.description}
        Subscriber count: {channel.subscriber_count}
    """)



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



if __name__ == '__main__':
    test_channel_by_id()
    test_channel_by_name()
