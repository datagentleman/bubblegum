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
