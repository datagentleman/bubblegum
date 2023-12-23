from __future__ import annotations

from bubblegum.connection import Connection
import bubblegum.buffer as buffer 

class Tensor:
  def __init__(self, name: str, conn: Connection):
    self.name = name.replace(":", "/")
    self.conn = conn


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
