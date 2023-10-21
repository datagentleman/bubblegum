import socket
from starbucks.buffer import Buffer

class Stream:
  def __init__(self, source: socket.socket):
    self.source = source
    self.buf = Buffer()


  def read(self) -> Buffer:
    if len(self.buf.data()) == 0: 
      self.load_buffer()
      
    return Buffer(self.buf.read())
    

  def load_buffer(self):
    n = int.from_bytes(self.source.recv(2), byteorder='big')
    self.buf.append(self.source.recv(n))    

                                                                                                                  
  def send(self, buf: Buffer, batch: bool=False):
    data = buf.data() if batch else buf.raw()
    res  = Buffer(data)
    
    self.source.send(res.raw())
  