from time import time


class Timer:
    def __init__(self, length, start=time()):
        self.length = length
        self.start = start

    def elapsed(self):
        return time() > self.start + self.length

    def reset(self, st=None):
        if st is None:
            st = time()
        self.start = st
