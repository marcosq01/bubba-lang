
class MemorySegment:
    def __init__(self, li, lf, ls, loa=0, ti=0, tf=0, ts=0) -> None:
        self.local_int = [0] * li
        self.local_float = [0.0] * lf
        self.local_string = [""] * ls
        self.local_obj_attr = [0] * loa
        self.temp_int = [0] * ti
        self.temp_float = [0.0] * tf
        self.temp_string = [""] * ts


