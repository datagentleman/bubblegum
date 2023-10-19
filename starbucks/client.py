import socket
from starbucks.stream import Stream

class Client:
  def __init__(self, host, port):
    self.conn: socket.socket = self.connect(host, port)
    self.stream: Stream = Stream(self.conn)

    
  def connect(self, host: str, port: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s


  def send(self, data):
    self.stream.send(data)


  def read(self) -> bytes:
    return self.stream.read()
  