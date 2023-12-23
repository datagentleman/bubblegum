from __future__ import annotations

import bubblegum.buffer as buffer

from bubblegum.connection    import Connection as Conn
from bubblegum.client.tensor import Tensor 

class Client:
  def __init__(self, type: str="CLIENT"):
    self.type: str = type
    self.conn = None


  def connect(self, host: str, port: str) -> Client:
    self.conn = Conn.connect(host, port)
    return self


  # TODO: call tload() or tcreate() 
  def tensor(self, name: str) -> Tensor:
    return Tensor(name, self.conn)


  # TODO: return Tensor
  def tcreate(self, name: str, dtype: str=None, shape: list(int)=None):
    self.conn.send('TCREATE', buffer.write(name, dtype, shape))
    return self.conn.read('int')


  def tremove(self, tensor_name: str):
    self.conn.send('TREMOVE', tensor_name)
    return self.conn.read('int')


  # TODO: return Tensor - implement decode()
  def tload(self, tensor_name: str):
    self.conn.send('TLOAD', tensor_name)

    status = self.conn.read('int')
    tensor = None

    # if status == 1:
    #   tensor = Tensor.decode(self.conn.read('bytes'))

    return status, tensor
