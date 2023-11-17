from __future__ import annotations

from starbucks.reader import Reader
from starbucks.writer import write

class Buffer:
  def __init__(self, packet = b''):
    self._data  = bytearray(packet)
    self.writer = write
    self.reader = Reader(self._data).read


  def write(self, data: any):
    self._data.extend(self.writer(data))
    return self


  def read(self, type_1: str, type_2: str=None) -> bytes:
    return self.reader(type_1, type_2)


  def data(self) -> bytes:
    return self._data
