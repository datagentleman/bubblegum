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


  @staticmethod
  def from_bytes(data: bytearray|bytes) -> Message:
    cmd = read_packet(data).decode()
    
    # read number of arguments
    count = int.from_bytes(read_packet(data), "big")
    args  = [read_packet(data).decode() for _ in range(count)]
    
    return Message(cmd, *args)

   
   
  def to_bytes(self) -> bytearray:
    cmd   = write_packet(self.cmd.encode())
    args  = [write_packet(key.encode()) for key in self.args]
    count = write_packet(len(args).to_bytes(2))
    
    return bytearray(cmd + count + b''.join(args))  
  

def write_packet(data: bytearray|bytes) -> bytes|bytearray:
  size = len(data).to_bytes(2)
  return size + data


def read_packet(data: bytearray) -> bytes|bytearray:  
  bytes  = data[:2]; del data[:2]
  size   = int.from_bytes(bytes, byteorder='big')
  packet = data[:size]; del data[:size]

  return packet
