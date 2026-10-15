class Tyre:
    def __init__(self, position):
        self.position = position
        self.details = {"pressure": 4, "tread_depth": 3}

    def get_details(self):
        return {self.position: self.details}
