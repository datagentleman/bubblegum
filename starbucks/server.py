import socket
import logging as log

from threading import Thread

from starbucks.command import Command as command
from starbucks.buffer  import Buffer 
from starbucks.stream  import Stream 
from starbucks.api     import API

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
        stream = Stream(conn)

        self.read_handshake(stream)
        Thread(target=self.do_work, args=[stream]).start()


  def do_work(self, stream):
    while True:
      try:
        buf = stream.read()

        log.debug(f'Got data: {buf.data()}')
        command.run(command.from_bytes(buf), stream)
      except:
        log.error('Client is dead ...')
        break
      
  
  def read_handshake(self, stream: Stream):
    _  = stream.read()
    stream.send(Buffer().write("OK".encode()))
