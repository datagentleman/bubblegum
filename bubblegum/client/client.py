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
    res = self.send('TPUT', tensor_name.replace(":", "/"), data)
    return res.read('int')


  def tget(self, tensor_name: str, num: int):
    res = self.send('TGET', tensor_name.replace(":", "/"), num)
    return res.read('int')


  def tcreate(self, tensor_name: str, dtype: str=None, shape: list(int)=None):
    res = self.send('TCREATE', tensor_name, dtype, shape)
    return res.read('int')


  def tremove(self, tensor_name: str):
    res = self.send('TREMOVE', tensor_name)
    return res.read('int') 
    
    
  def tload(self, tensor_name: str):
    res = self.send('TLOAD', tensor_name)

    status = res.read('int')
    tensor = None
    
    if status == 1:
      tensor = Tensor.decode(res.read('bytes'))
    
    return status, tensor


  def tsave(self, tensor_name: str, dtype: str=None, shape: list(int)=None):
    res = self.send('TSAVE', tensor_name, dtype, shape)
    return res.read('int')


  def send(self, cmd: str, *args):
    buf1 = Buffer().write(cmd)
    buf2 = Buffer()

    # build command args
    if len(args) > 0:
      for arg in args: buf2.write(arg)
      
    self.conn.send(buf1.data, buf2.data)
    return self.conn.read()


