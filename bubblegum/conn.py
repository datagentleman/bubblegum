import socket 

from bubblegum.buffer  import Buffer
from bubblegum.reader  import Reader
from bubblegum.writer  import Writer

# this class will manage clients connection to node
class Conn:
  def __init__(self, conn: socket.socket):
    self.conn = conn
    self.data = bytearray()


  # read next message
  def read(self) -> Buffer:
    n = int.from_bytes(self.conn.recv(4), byteorder='little')
    
    data =  self.conn.recv(n)
    return Buffer(data)


  # send bytes
  def send(self, data) -> int:
    # Before send we must append data size - other end must know how many bytes to read.
    buf = Buffer()
    buf.write(data)
    return self.conn.send(buf.data)


  # read handshake.
  def read_handshake(self) -> bytes:
    self.conn.settimeout(0.5)
    
    buf = self.read()
    conn_type = buf.read('str')

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

    buf = self.read()
    buf.read('bytes')

    # from this point on, we cannot have any timeouts on socket - ex: streaming, long running tasks, ...
    self.conn.settimeout(None)

    
  # needed when working with select()
  def fileno(self):
    return self.conn.fileno()
  
