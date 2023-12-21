from __future__ import annotations

import socket
import dataclasses
import numpy as np

from bubblegum.conn   import Conn
from bubblegum.buffer import Buffer
from bubblegum.tensor import Tensor 

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


  def tput(self, tensor_name: str, data: bytes):
    return self.send('TPUT', tensor_name.replace(":", "/"), data)


  def tset(self, tensor_name: str, data: bytes, index: int=0):
    return self.send('TSET', tensor_name.replace(":", "/"), data, index)


  def tget(self, tensor_name: str, num: int):
    status = self.send('TGET', tensor_name.replace(":", "/"), num)
    data   = self.conn.read('bytes')

    return status, data


  def tcreate(self, tensor_name: str, dtype: str=None, shape: list(int)=None):
    return self.send('TCREATE', tensor_name, dtype, shape)


  def tremove(self, tensor_name: str):
    return self.send('TREMOVE', tensor_name)
    
    
  def tload(self, tensor_name: str):
    status = self.send('TLOAD', tensor_name)
    tensor = None
    
    if status == 1:
      tensor = Tensor.decode(self.conn.read('bytes'))

    return status, tensor


  def tsave(self, tensor_name: str, dtype: str=None, shape: list(int)=None):
    return self.send('TSAVE', tensor_name, dtype, shape)


  def send(self, cmd: str, *args):
    buf2 = Buffer()

    # build command args
    if len(args) > 0:
      for arg in args: buf2.write(arg)
    
    self.conn.send(cmd, buf2.data)
    return self.conn.read('int')


