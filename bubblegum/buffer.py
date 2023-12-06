from __future__ import annotations

from bubblegum.reader import Reader
from bubblegum.writer import Writer

class Buffer(Reader, Writer):
  pass

def write(data: any) -> Writer:
  return Writer().write(data)
  