import typing as t


class BasePipedModel:
    """
        Base class for all Piped models.
    """

    def __init__(self, data: t.Dict[str, t.Any]) -> None:
        """
            ### Parameters:
            - `data` - The JSON (`dict`) data to initialize the model with.
        """

        self.data = data
