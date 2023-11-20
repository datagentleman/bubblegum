from __future__ import annotations

import socket

from starbucks.conn        import Conn
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
    
    self.conn = Conn(conn)
    self.conn.send_handshake()

    return self


  def ping(self):
    self.send('PING')
    return self.read()


  def send(self, cmd: str, *args):
    buf = Buffer()
    
    buf.write(cmd)
    [buf.write(arg) for arg in args]
    
    self.conn.send(buf())


  def read(self, type_1: str, type_2: str=None) -> Buffer:
    return self.conn.read(type_1, type_2)

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
  