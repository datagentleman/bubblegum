import socket
import selectors
import traceback
import logging as log

from bubblegum.connection import Connection as Conn

class Node:
  def __init__(self, host, port):
    self.host = host
    self.port = port

    self.connected_clients = {}
    self.select = selectors.DefaultSelector()


  # accept incoming connections
  def accept(self, sock: socket.socket):
    sock, addr = sock.accept()    
    conn = Conn(sock)

    log.info(f'accepted connection: {conn} from {addr} FD: {conn.fileno()}')

    conn.read_handshake()
    conn.conn.setblocking(False)

    # we can now add this connection to select pool
    self.select.register(conn, selectors.EVENT_READ)


  def run(self, run_command):
    self.create_socket_and_listen()

    # add server socket to select. It will accept incoming connections
    self.select.register(self.node_socket, selectors.EVENT_READ)

    # main select loop. All requests to node are handled here.
    while True:
      for event, _ in self.select.select():
        conn = event.fileobj

        try:
          # someone wants to connect
          if conn is self.node_socket:
            self.accept(conn)

          # get command from connected client
          else:
            run_command(conn, self)
            

        except ConnectionResetError as e:
          log.error(f"Connection reset by peer: {e}")
          self.select.unregister(conn)
          conn.conn.close()      

        except Exception as e:
          log.error(traceback.format_exc())
          return


  def create_socket_and_listen(self): 
    self.node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    self.node_socket.setblocking(False)
    self.node_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    self.node_socket.bind((self.host, self.port))
    self.node_socket.listen()
    