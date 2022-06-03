

from mimetypes import init


class ExecutionContext:
    def __init__(self, mem, addr) -> None:
        self.memory = mem
        self.address = addr

