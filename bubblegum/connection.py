import socket 

from bubblegum.buffer  import Buffer

# this class will manage clients connection to node
class Connection(Buffer):
  def __init__(self, sock: socket.socket):
    super().__init__()
    self.conn = sock


  @classmethod
  def connect(cls, host: str, port: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    conn = Connection(s)
    conn.send_handshake()
    return conn


  def read_length(self, len=4):
    return self.conn.recv(len, socket.MSG_WAITALL)


  # send bytes
  def send(self, *items) -> int:
    for i in items: self.write(i)

    self.conn.send(self.data)
    self.data = bytearray()


  # read handshake
  def read_handshake(self):
    self.conn.settimeout(0.5)

    self.read('str')
    self.send("OK")

    self.conn.settimeout(None)

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
