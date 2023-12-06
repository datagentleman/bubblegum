from __future__ import annotations

from bubblegum.reader import Reader
from bubblegum.writer import Writer

class Buffer(Reader, Writer):
  pass

def write(*values: any) -> bytearray:
  buf = Buffer()

  [buf.write(val) for val in values]
  return buf.data
