import socket 

from bubblegum.buffer  import Buffer
from bubblegum.reader  import Reader
from bubblegum.writer  import Writer

# this class will manage clients connection to node
class Conn(Buffer):
  def __init__(self, conn: socket.socket):
    self.conn = conn
    super().__init__()


  def read_length(self, len=4):
    return self.conn.recv(len)


  # send bytes
  def send(self, *items) -> int:
    for i in items: self.write(i)
    self.conn.send(self.data)
    self.data = bytearray()


  # read handshake
  def read_handshake(self) -> bytes:
    self.conn.settimeout(0.5)

    conn_type = self.read('str')
    self.send("OK")

    self.conn.settimeout(None)
    return conn_type


  # send handshake.
  # this will also ensure us that connection was accepted and we can transfer bytes.
  def send_handshake(self) -> bytes:
    # handshake should be reasonably fast
    self.conn.settimeout(0.5)

    self.send("OK")
    self.read('bytes')

    # from this point on, we cannot have any timeouts on socket - ex: streaming, long running tasks, ...
    self.conn.settimeout(None)


  # needed when working with select()
  def fileno(self):
    return self.conn.fileno()
