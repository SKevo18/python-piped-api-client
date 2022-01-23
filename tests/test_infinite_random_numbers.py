from python_project_template import infinitum



def test_infinitum():
    """
        Tests the infinite random number generator.
    """

    for random in infinitum():
        assert type(random) == int
        break
