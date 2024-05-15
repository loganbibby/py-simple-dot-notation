class SimpleDotNotation:
    """
    Access a dictionary using dot-notation.
    """

    def __init__(self, data):
        self._data = data

    @property
    def value(self):
        return self._data

    def __getattr__(self, key):
        value = self._data.get(key)

        if isinstance(value, dict):
            return SimpleDotNotation(value)

        return value

    def get(self, keys):
        data = self

        for key in keys.split("."):
            data = getattr(data, key)

        return data
