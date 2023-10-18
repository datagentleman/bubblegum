import socket
from starbucks.buffer import Buffer

class Stream:
  def __init__(self, source: socket.socket):
    self.source = source


  def read(self) -> bytes:
    n = int.from_bytes(self.source.recv(2), byteorder='big')
    return self.source.recv(n)
    

  def send(self, data: bytes):
    buf = Buffer().write(data)
    self.source.send(buf.raw())
  