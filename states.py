from enum import Enum, auto

class LbaState(Enum):
    START = auto()
    READING = auto()
    WARNING = auto()
    REJECT = auto()