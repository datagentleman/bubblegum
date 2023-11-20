from __future__ import annotations

from starbucks.reader import Reader
from starbucks.writer import Writer

class Buffer:
  def __init__(self, packet = b''):
    self.data   = bytearray(packet)
    self.writer = Writer(self.data)
    self.reader = Reader(self.data)


  def __call__(self):
    return self.data
  
  def write(self, data: any):
    self.writer.write(data)
    return self


  def read(self, type_1: str, type_2: str=None) -> bytes:
    return self.reader.read(type_1, type_2)

