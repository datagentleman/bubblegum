import sys
import socket
import logging as log

from threading import Thread

from starbucks.command import Command as command
from starbucks.api     import API
from starbucks.stream  import Stream 

class Server:
  def __init__(self, host, port):
    self.host = host
    self.port = port
  
  def run(self):
    command.COMMANDS = API
 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      
      s.bind((self.host, self.port))
      s.listen()
    
      while True:
        conn, addr = s.accept()
        log.info(f"Got connection from {addr}")
        Thread(target=self.do_work, args=[conn]).start()


  def do_work(self, conn):
    with conn:
      while True:
        stream = Stream(conn)
        buf = stream.read()

        log.debug(f'Got data: {buf.data()}')
        command.run(command.from_bytes(buf), stream)