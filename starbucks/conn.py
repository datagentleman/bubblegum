import socket 

from starbucks.buffer  import Buffer
from starbucks.reader  import Reader
from starbucks.writer  import Writer

# this class will manage clients connection to node
class Conn:
  def __init__(self, conn: socket.socket):
    self.conn = conn
    self.data = bytearray()

    self.reader = Reader(self.data)
    self.writer = Writer(self.data)


  # read next message
  def read(self, type_1: str, type_2: str=None) -> bytes:
    if len(self.data) == 0:
      self._load_buffer()

    return self.reader.read(type_1, type_2)


  # send bytes
  def send(self, data: bytearray) -> int:
    return self.conn.send(data)


  # read handshake.
  def read_handshake(self) -> bytes:
    self.conn.settimeout(0.5)
    conn_type = self.read('str')
    
    res = Buffer().write("OK")
    self.send(res.data)

    self.conn.settimeout(None)
    return conn_type


  # send handshake.
  # this will also ensure us that connection was accepted and we can transfer bytes.
  def send_handshake(self) -> bytes:
    # handshake should be reasonably fast
    self.conn.settimeout(0.5)
    
    res = Buffer().write("OK")
    self.send(res.data)
    self.read('bytes')

    # from this point on, we cannot have any timeouts on socket - ex: streaming, long running tasks, ...
    self.conn.settimeout(None)
    

  def _load_buffer(self):
    n = int.from_bytes(self.conn.recv(4), byteorder='little')
    self.writer.write(self.conn.recv(n))
    
    
  # needed when working with selec()
  def fileno(self):
    return self.conn.fileno()
  
