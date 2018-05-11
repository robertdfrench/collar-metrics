class BarksTable(object):
    def __init__(self):
        self.barks = []

    def by_collar(self, collar_id):
        return self.barks

    def add(self, **kwargs):
        self.barks.append(kwargs)
