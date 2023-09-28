from .CUT import cut
from .NER_RE import NER_RE

def NERRE(text: str) -> dict:
    return NER_RE(cut(text))