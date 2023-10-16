import socket
from starbucks.packet import Message as msg

class Server:
  HOST = "127.0.0.1"
  PORT = 1337
    
  def run(self):
    print("Starting starbucks server ...")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      
      s.bind((self.HOST, self.PORT))
      s.listen()
      
      # This will be in threads via cython. For now it's single threaded.
      while True:
        conn, addr = s.accept()
        print(f"Got connection from {addr}")
        self.do_work(conn)


  def do_work(self, conn):
    with conn:
      while True:
        data = msg.recv(conn)
        print(f"Data received: {data}")
        msg.send(conn, data)        