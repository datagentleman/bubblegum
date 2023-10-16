from __future__ import annotations
import socket

# Low level reading/writing packets from/to tcp sockets

def read(conn: socket.socket):
  # read size - 2 bytes
  bytes = conn.recv(2)
  size = int.from_bytes(bytes, byteorder='big')
  
  # read and return data
  data = conn.recv(size)
  return data


def write(conn: socket.socket, data: bytearray|bytes) -> int:
  size = len(data).to_bytes(2)
  bytes = size + data
  
  conn.send(size + data)
  return len(bytes)


class Message:
  def __init__(self, name, *args):
    self.cmd: str = name
    self.args: list[str] = args


  def to_bytes(self) -> bytearray:
    cmd = write_packet(self.cmd.encode())
    
    args = [write_packet(key.encode()) for key in self.args]
    args_count = write_packet(len(args).to_bytes(2))

    return bytearray(cmd + args_count + b''.join(args))


  @staticmethod
  def from_bytes(data: bytearray|bytes) -> Message:
    cmd = read_packet(data).decode()
    
    args_count = int.from_bytes(read_packet(data), "big")
    args = [read_packet(data).decode() for _ in range(args_count)]

    return Message(cmd, *args)
   
    
def write_packet(data: bytearray|bytes) -> bytes|bytearray:
  size = len(data).to_bytes(2)
  return size + data


def read_packet(data: bytearray) -> bytes|bytearray:  
  bytes = data[:2]; del data[:2]
  
  size = int.from_bytes(bytes, byteorder='big')
  packet = data[:size]; del data[:size]

  return packet
      
      
      