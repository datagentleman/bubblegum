from __future__ import annotations

import socket

from starbucks.stream      import Stream
from starbucks.command     import Command
from starbucks.buffer      import Buffer
from starbucks.data_stream import DataStream

class Client:
  def __init__(self, type: str="CLIENT"):
    self.type: str = type
    
    self.conn: socket.socket = None
    self.stream: Stream = None


  @classmethod
  def connect(cls, host: str, port: str) -> Client:
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((host, port))
    
    stream = Stream(conn)
    client = Client()
    
    client.conn   = conn
    client.stream = stream

    client.__handshake()
    return client


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
  def tstream(self, path: str) -> DataStream:
    return DataStream.run(self, path)