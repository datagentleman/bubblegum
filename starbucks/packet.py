from __future__ import annotations
import socket

class Message:
  def __init__(self, name, *args):
    self.cmd: str = name
    self.args: list[str] = args
  
  @classmethod
  def send(cls, conn: socket.socket, msg: str|bytearray|bytes) -> int:
    msg   = msg.encode() if isinstance(msg, str) else msg
    bytes = write_packet(msg)
    
    return conn.send(write_packet(bytes))


  @classmethod
  def recv(cls, conn: socket.socket) -> bytearray:
    n = int.from_bytes(conn.recv(2), byteorder='big')
    return bytearray(conn.recv(n))
  

def write_packet(data: bytearray|bytes) -> bytes|bytearray:
  size = len(data).to_bytes(2)
  return size + data


def read_packet(data: bytearray) -> bytes|bytearray:  
  bytes  = data[:2]; del data[:2]
  size   = int.from_bytes(bytes, byteorder='big')
  packet = data[:size]; del data[:size]

  return packet
