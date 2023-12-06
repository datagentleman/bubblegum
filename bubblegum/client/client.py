from __future__ import annotations

import socket
import dataclasses
import numpy as np

from bubblegum.conn   import Conn
from bubblegum.buffer import Buffer

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


  def tcreate(self, tensor_name: str, shape: list(int)=None, dtype: str=None):
    return self.send('TCREATE', tensor_name, shape, dtype)
    

  def send(self, cmd: str, *args):
    buf = Buffer()

    buf.write(cmd)
    [buf.write(arg) for arg in args]

    self.conn.send(buf.data)
    return self.conn.read()
