from __future__ import annotations

from bubblegum.reader import Reader
from bubblegum.writer import Writer

class Buffer(Writer, Reader):
  pass

def write(*values: any) -> bytearray:
  buf = Buffer()

  [buf.write(val) for val in values]
  return buf.data
