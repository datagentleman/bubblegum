import os
import traceback
import logging as log

from starbucks.node    import Node
from starbucks.conn    import Conn
from starbucks.api     import PYTHON_API
from starbucks.config  import Config 
from starbucks.command import Command

log.basicConfig(format="\x1b[6;37;44m%(levelname)s\x1b[0m:%(message)s", level=log.DEBUG)

HOST = Config["server.host"]
PORT = Config["server.port"]

Command.COMMANDS = PYTHON_API

def handle_client(client_conn: Conn, cmd):
  cmd.run(client_conn)
  log.error('Client is dead ...')
  
    
if __name__ == '__main__':
  try:
    log.info(f'Starting starbucks node on host: {HOST} port: {PORT} pid: {os.getpid()}')
    Node(HOST, PORT).run(handle_client)
  except Exception as e:
    log.error(f'{traceback.format_exc()}')
