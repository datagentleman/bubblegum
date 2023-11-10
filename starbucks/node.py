import socket
import selectors
import logging as log

from starbucks.conn     import Conn

class Node:
  def __init__(self, host, port):
    self.host = host
    self.port = port

    self.connected_clients = {}
    self.select = selectors.DefaultSelector()
    

  # accept all connections
  def accept(self, sock):
    conn, addr = sock.accept()    
    conn = Conn(conn)

    log.info(f'accepted connection: {conn} from {addr}')

    conn.read_handshake()
    conn.conn.setblocking(False)

    # we can now add this connection to select pool
    self.select.register(conn, selectors.EVENT_READ)


  def run(self, run_command):
    self.create_socket_and_listen()

    # add server socket to select. It will accept incoming connections
    self.select.register(self.sock, selectors.EVENT_READ, self.accept)

    while True:
      for event, _ in self.select.select():
          conn = event.fileobj
          
          try:
            if event.data is not None:
              callback = event.data
              callback(conn)
            else:
              run_command(conn)

          except ConnectionResetError as e:
            log.error(f"Connection reset by peer: {e}")
            self.select.unregister(conn)
            conn.conn.close()         

          except Exception as e:
            log.error(f"ERROR: {e}")


  def create_socket_and_listen(self): 
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    self.sock.setblocking(False)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    self.sock.bind((self.host, self.port))
    self.sock.listen()
    