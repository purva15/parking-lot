class InvalidAPIUsage(Exception):
    statusCode = 400

    def __init__(self, errorDescription, errorId, statusCode=None):
        super().__init__()
        self.errorDescription = errorDescription
        self.errorId = errorId
        if statusCode is not None:
            self.statusCode = statusCode

    def to_dict(self):
        rv = dict()
        rv['errorId'] = self.errorId
        rv['errorDescription'] = self.errorDescription
        return rv
