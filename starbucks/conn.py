import socket 

from starbucks.buffer  import Buffer
from starbucks.command import Command as command

# this class will manage clients connection to node
class Conn:
  def __init__(self, conn: socket.socket):
    self.conn = conn
    self.buf  = Buffer()

  # read next message. 
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


  # read handshake.
  def read_handshake(self) -> bytes:
    conn_type = self.read()
    self.send(Buffer().write("OK".encode()))

    return conn_type.read()


  # send handshake.
  # this will also ensure us that connection was accepted and we can transfer bytes.
  def send_handshake(self) -> bytes:
    # handshake should be reasonably fast
    self.conn.settimeout(0.5)
        
    self.send(Buffer().write("OK".encode()))
    self.read()

    # from this point on, we cannot have any timeouts on socket - ex: streaming, long running tasks, ...
    self.conn.settimeout(None)
    

  # get next command from client
  def get_cmd(self) -> command:
    return command.from_bytes(self.read())


  def _load_buffer(self):
    n = int.from_bytes(self.conn.recv(2), byteorder='little')
    self.buf.append(self.conn.recv(n))
    
    
  # needed when working with selec()
  def fileno(self):
    return self.conn.fileno()
  
