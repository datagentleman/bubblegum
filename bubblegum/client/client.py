from __future__ import annotations

import bubblegum.buffer as buffer
import bubblegum.status as status 

from bubblegum.connection    import Connection as Conn
from bubblegum.client.tensor import Tensor 

class Client:
  def __init__(self, type: str="CLIENT"):
    self.type: str = type
    self.conn = None


  def connect(self, host: str, port: str) -> Client:
    self.conn = Conn.connect(host, port)
    return self


  # It loads tensor if exists, if not then it creates new one
  def tensor(self, name: str, dtype: str=None, shape: list(int)=None) -> Tensor:
    name = Tensor.replace_name(name)

    _, tensor = self.tload(name)
    if tensor: return tensor

    return Tensor(name, self.conn)


  # TODO: return Tensor
  def tcreate(self, name: str, dtype: str=None, shape: list(int)=None):
    name = Tensor.replace_name(name)
    self.conn.send('TCREATE', buffer.write(name, dtype, shape))
    return self.conn.read('int')


  def tremove(self, name: str):
    name = Tensor.replace_name(name)

    self.conn.send('TREMOVE', name)
    return self.conn.read('int')


  def tload(self, name: str):
    name = Tensor.replace_name(name)
    self.conn.send('TLOAD', name)

    code = self.conn.read('int')
    tensor = None

    if code == status.OK:
      tensor = Tensor.decode(self.conn.read('bytes'))
      tensor.conn = self.conn
      
    return status.OK, tensor
  
  