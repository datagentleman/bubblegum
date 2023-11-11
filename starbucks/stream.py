from __future__ import annotations

import socket
from enum import Enum

from starbucks.buffer import Buffer

class MSGType(Enum):
  CMD = 1
  MSG = 2

# TODO: change this to Conn class
class Stream:
  def __init__(self, source: socket.socket):
    self.source = source
    self.buf = Buffer()


  def read(self) -> Buffer:
    if len(self.buf.data()) == 0: 
      self.load_buffer()

    return Buffer(self.buf.read())


  def load_buffer(self):
    n = int.from_bytes(self.source.recv(2), byteorder='little')
    self.buf.append(self.source.recv(n))


  def send(self, buf: Buffer, batch: bool=False) -> int:
    data = buf.data() if batch else buf.raw()
    res  = Buffer(data)

    return self.source.send(res.raw())
  