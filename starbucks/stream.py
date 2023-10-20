import socket
from starbucks.buffer import Buffer

class Stream:
  def __init__(self, source: socket.socket):
    self.source = source
    self.buf = Buffer()


  def read(self) -> Buffer:
    if len(self.buf.data()) == 0:
      n = int.from_bytes(self.source.recv(2), byteorder='big')
      data = self.source.recv(n)
      self.buf.append(data)
    
    return Buffer(self.buf.read())


  def send(self, data: bytes):
    buf = Buffer().write(data)
    self.source.send(buf.raw())
  