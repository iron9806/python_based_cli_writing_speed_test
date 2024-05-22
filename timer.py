import datetime

class Timer:
    def __init__(self):
        self.vat = None  # IGONER this line its here cause I couldnt keep this block blank

    def start(self):
        self.start = datetime.datetime.now()
        return self.start

    def stop(self):
        self.stop = datetime.datetime.now()
        return str(self.stop - self.start)
