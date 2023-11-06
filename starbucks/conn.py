import socket 

from starbucks.buffer import Buffer

# this class will manage clients connection to node
class Conn:
  def __init__(self, conn: socket.socket):
    self.conn = conn
    self.buf  = Buffer()
  
  
  # read next message 
  def read(self):
    if len(self.buf.data()) == 0: 
      self._load_buffer()
      
    return Buffer(self.buf.read())
    
    
  # send bytes
  # TODO: try to remove batch option. Make it cleaner.
  def send(self, buf: Buffer, batch: bool=False) -> int:
    data = buf.data() if batch else buf.raw()
    res  = Buffer(data)

    return self.conn.send(res.raw())


  def _load_buffer(self):
    n = int.from_bytes(self.conn.recv(2), byteorder='little')
    self.buf.append(self.conn.recv(n))
    

