import socket

from threading         import Thread
from starbucks.buffer  import Buffer 
from starbucks.conn    import Conn
from starbucks.api     import CYTHON_API, PYTHON_API

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
        
        cmd = conn.get_cmd()
        if cmd is None:
          conn.send(Buffer(b"COMMAND DOESN'T EXIST!"))
          continue
          
        # Based on given cmd, we must route request to cython or good old python.
        # Most of heavy tensor operations will be handled by cython.
        # if(CYTHON_API.get(cmd.name)):
        #   # call it with fd
        #   pass

        Thread(target=client_handler, args=[conn, cmd]).start()


  def _connect_node(self, addr):
    host_port = ':'.join(map(str, addr))
    self.connected_nodes[host_port] = Node(addr[0], addr[1])
