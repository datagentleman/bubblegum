from __future__ import annotations

import socket

from starbucks.stream  import Stream
from starbucks.command import Command
from starbucks.buffer  import Buffer

class Iterator:
  def __init__(self, client: Client):
    self.client = client


  @classmethod
  def run(cls, client: Client, path: str) -> Iterator:
    client.send('TSTREAM', path)
    return Iterator(client)


  def next(self):
    self.client.send_raw(b'NEXT')
    res = self.client.read()
    return res.data()


  def end(self):
    self.client.send_raw(b'END')


class Client:
  def __init__(self, host: str, port: str, type: str="CLIENT"):
    self.host: str = host
    self.port: str = port
    self.type: str = type

    self.conn: socket.socket = None
    self.stream: Stream = None


  def connect(self):
    self.conn   = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.stream = Stream(self.conn)
    
    self.conn.connect((self.host, self.port))
    self.__handshake()
    return self


  def __handshake(self):
    # handshake should be reasonably fast
    self.conn.settimeout(0.5)
    self.stream.send(Buffer().write(self.type.encode()))
    self.stream.read()
    
    # from this point on, we cannot have any timeouts on socket - ex: streaming, long running tasks, ...
    self.conn.settimeout(None)


  def send(self, cmd, *args):
    cmd = Command(cmd, *args)
    self.stream.send(cmd.to_bytes())

  def send_raw(self, data: bytes):
    self.stream.send(Buffer().write(data), batch=True)


  def read(self) -> Buffer:
    return self.stream.read()


  ### 
  ### WORKERS 
  ###

  # Run worker
  def wrun(self) -> Buffer:
    self.send('WRUN')
    return self.read()
  
  
  ### 
  ### TENSORS 
  ###
  
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


  # Stream tensor data
  def tstream(self, path: str) -> Iterator:
    return Iterator.run(self, path)
    