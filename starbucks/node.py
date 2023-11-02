import socket

from threading         import Thread
from starbucks.buffer  import Buffer 
from starbucks.stream  import Stream 

class Node:
  def __init__(self, host, port):
    self.host = host
    self.port = port

    self.connected_nodes = {}


  def run(self, client_handler: callable):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

      s.bind((self.host, self.port))
      s.listen()

      while True: 
        conn, addr = s.accept()
        stream = Stream(conn)

        conn_type = self.read_handshake(stream)
        if conn_type == b'NODE': 
          self._connect_node(addr)

        Thread(target=client_handler, args=[stream]).start()


  def _connect_node(self, addr):
    host_port = ':'.join(map(str, addr))
    self.connected_nodes[host_port] = Node(addr[0], addr[1])

  
  def read_handshake(self, stream: Stream) -> bytes:
    conn_type = stream.read()
    stream.send(Buffer().write("OK".encode()))

    return conn_type.read()
