import socket

from threading         import Thread
from starbucks.buffer  import Buffer 
from starbucks.conn    import Conn

from starbucks.src.cython.tensor import CTensor as tensor

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
        client_conn, addr = s.accept()
        conn = Conn(client_conn)

        conn.read_handshake()
        Thread(target=client_handler, args=[conn]).start()


  def _connect_node(self, addr):
    host_port = ':'.join(map(str, addr))
    self.connected_nodes[host_port] = Node(addr[0], addr[1])
