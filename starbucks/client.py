from __future__ import annotations

import socket

from starbucks.stream      import Stream
from starbucks.command     import Command
from starbucks.buffer      import Buffer
from starbucks.data_stream import DataStream

class Client:
  def __init__(self, host: str, port: str, type: str="CLIENT"):
    self.host: str = host
    self.port: int = port
    self.type: str = type


  def connect(self) -> Client:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((self.host, self.port))
    
    self.conn = conn
    self.stream = Stream(conn)

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


  def read(self) -> Buffer:
    return self.stream.read()


  ### 
  ### WORKERS 
  ###

  # Run worker
  def wrun(self, name: str) -> Buffer:
    self.send('WRUN', name)
    return self.read()

  # Run list
  def wls(self) -> Buffer:
    self.send('WLS')
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
  def tstream(self, path: str) -> DataStream:
    return DataStream.run(self, path)