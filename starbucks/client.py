import socket

from starbucks.stream  import Stream
from starbucks.command import Command
from starbucks.buffer  import Buffer

class Client:
  def __init__(self, host, port):
    self.conn: socket.socket = self.connect(host, port)
    self.stream: Stream = Stream(self.conn)

    
  def connect(self, host: str, port: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s


  def send(self, cmd, *args):
    cmd = Command(cmd, *args)
    self.stream.send(cmd.to_bytes())


  def read(self) -> Buffer:
    return self.stream.read()
  