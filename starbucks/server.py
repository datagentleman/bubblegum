import socket
import traceback

from threading import Thread

from starbucks.command import Command as command
from starbucks.api     import API
from starbucks.stream  import Stream 


class Server:
  HOST = "127.0.0.1"
  PORT = 1337
  
  def run(self):
    print("Starting starbucks server ...")

    command.COMMANDS = API
 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      
      s.bind((self.HOST, self.PORT))
      s.listen()
      
      while True:
        print(f'WAITING FOR CONN ..................')
        conn, addr = s.accept()
        print(f"Got connection from {addr}")
        Thread(target=self.do_work, args=[conn]).start()


  def do_work(self, conn):
    with conn:  
      while True:
        try:
          stream = Stream(conn)
          buf = stream.read()
          
          print(f'Got data: {buf.data()}')
          command.run(command.from_bytes(buf), stream)
        except Exception:
          print(f'We have error: {traceback.format_exc()}')
          break