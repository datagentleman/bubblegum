from __future__ import annotations
import socket
from starbucks.buffer import Buffer

class Message:
  def __init__(self, name, *args):
    self.cmd: str = name
    self.args: list[str] = args
  
  
  @classmethod
  def send(cls, conn: socket.socket, msg: str|bytearray|bytes) -> int:
    msg = msg.encode() if isinstance(msg, str) else msg
    buf = Buffer()
    buf.write(msg)
    
    return conn.send(buf.data)


  @classmethod
  def recv(cls, conn: socket.socket) -> bytearray:
    n = int.from_bytes(conn.recv(2), byteorder='big')
    return bytearray(conn.recv(n))
