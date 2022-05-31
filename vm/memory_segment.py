
class MemorySegment:
    def __init__(self, li, lf, ls, ti=0, tf=0, ts=0) -> None:
        self.local_int = [None] * li
        self.local_float = [None] * lf
        self.local_string = [None] * ls
        self.temp_int = [None] * ti
        self.temp_float = [None] * tf
        self.temp_string = [None] * ts


