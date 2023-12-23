from __future__ import annotations

from bubblegum.connection import Connection
from bubblegum.buffer     import Buffer 

import bubblegum.buffer as buffer 

class Tensor:
  def __init__(self, name: str=None, conn: Connection=None):
    self.name  = self.replace_name(name) if name else name
    self.conn  = conn
    self.dtype = None
    self.shape = None
    

  def put(self, data: bytes):
    self.conn.send('TPUT', buffer.write(self.name, data))
    return self.conn.read('int')


  def get(self, num: int):
    self.conn.send('TGET', buffer.write(self.name, num))

    status = self.conn.read('int')
    data   = self.conn.read('bytes')

    return status, data


  def set(self, data: bytes, index: int=0):
    self.conn.send('TSET', buffer.write(self.name, data, index))
    return self.conn.read('int')
  

  def save(self, dtype: str=None, shape: list(int)=None):
    self.conn.send('TSAVE', buffer.write(self.name, dtype, shape))
    return self.conn.read('int')


  @classmethod
  def decode(cls, data: bytes):
    buf = Buffer(data)
    ten = Tensor()

    ten.name  = buf.read('str')
    ten.dtype = buf.read('str')
    ten.shape = buf.read('list[int]')
    return ten


  @classmethod
  def replace_name(cls, name: str):
    return name.replace(":", "/")
    