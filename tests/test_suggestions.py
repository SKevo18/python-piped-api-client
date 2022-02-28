from tests import CLIENT


def test_suggestions(search_query: str='Susan') -> None:
    """
        Obtains search suggestions for a query.
    """

    suggestions = CLIENT.get_search_suggestions(search_query)

    assert len(suggestions) > 0
    print(suggestions)



if __name__ == '__main__':
    test_suggestions()
