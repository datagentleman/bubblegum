import socket

from starbucks.stream  import Stream
from starbucks.command import Command
from starbucks.buffer  import Buffer

class Client:
  def __init__(self, host: str, port: str, type: str="CLIENT"):
    self.host: str = host
    self.port: str = port
    self.type: str = type
    
    self.conn: socket.socket = None
    self.stream: Stream = None


  def connect(self):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    
    self.conn   = s
    self.stream = Stream(self.conn)
    
    self.__handshake()
    
    return self


  def __handshake(self):
    # handshake should be reasonably fast
    self.conn.settimeout(0.5)
    
    self.stream.send(Buffer().write(self.type.encode()))
    self.read()
    
    self.conn.settimeout(None)
    

  def send(self, cmd, *args):
    cmd = Command(cmd, *args)
    self.stream.send(cmd.to_bytes())


  def read(self) -> Buffer:
    return self.stream.read()
  
  #### 
  #### TENSORS 
  ####
  
  # Create tensor
  def tcreate(self, path: str) -> Buffer:
    self.send('TCREATE', path)
    return self.read()

    
  # Remove tensor
  def tremove(self, path: str) -> Buffer:
    self.send('TREMOVE', path)
    return self.read()


  # List tensors
  def tls(self, path: str='') -> Buffer:
    self.send('TLS', path)
    return self.read()
