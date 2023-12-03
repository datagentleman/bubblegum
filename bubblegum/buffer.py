from __future__ import annotations

from bubblegum.reader import Reader
from bubblegum.writer import Writer

class Buffer(Reader, Writer):
  def __call__(self):
    return self.data
  