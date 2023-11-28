from __future__ import annotations

import socket
import dataclasses
import numpy as np

from bubblegum.conn   import Conn
from bubblegum.buffer import Buffer

import bubblegum.client.dataclasses as dataclass 

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


  def send(self, cmd: str, *args):
    buf = Buffer()

    buf.write(cmd)
    [buf.write(arg) for arg in args]

    self.conn.send(buf())
    return self.response(cmd)


  def response(self, cmd: str):
    match cmd:
      case 'TCREATE': 
        return self.decode(dataclass.Tensor)
      case default: return None


  def get_data_types(self, type: str):
    # This will parse things like: 'list[int]' =>/ ['list', 'int']
    type.replace('[', ' ').replace(']', '').split(' ')


  def decode(self, data: any):
    # Setting data attributes by name
    for field in dataclasses.fields(data):
      types = self.get_data_types(field.type)
      value = self.conn.read(*types)

      setattr(data, field.name, value)
