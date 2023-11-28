import os
import traceback
import logging as log

from bubblegum.conn     import Conn
from bubblegum.node     import Node
from bubblegum.config   import Config 
from bubblegum.commands import * 

import lib.commands as c_commands

log.basicConfig(format="\x1b[6;37;44m%(levelname)s\x1b[0m:%(message)s", level=log.DEBUG)

HOST = Config["server.host"]
PORT = Config["server.port"]

def run_command(conn: Conn, node: Node):
  cmd = conn.read('str')

  match cmd:
    # cython commands - running concurrently
    case "PING": c_commands.ping(conn.fileno())

    case "TPUT": 
      c_commands.put(conn.fileno())
      # since we will be dealing with this conn in cpp, we must remove it from python select() loop
      node.select.unregister(conn)

    # server
    case "HELLO": hello

    # workers
    case "WLS":  worker_ls
    case "WRUN": worker_run
    
    # tensors      
    case "TCREATE": tensor_create
    case "TREMOVE": tensor_remove
    case "TSTREAM": tensor_stream

    case _:
      conn.send(b"COMMAND DOESN'T EXIST")
  

def handle_client(client_conn: Conn, cmd):
  cmd.run(client_conn)
  log.error('Client is dead ...')
  
  
if __name__ == '__main__':
  try:
    log.info(f'Starting bubblegum node on host: {HOST} port: {PORT} pid: {os.getpid()}')
    Node(HOST, PORT).run(run_command)
  except Exception as e:
    log.error(f'{traceback.format_exc()}')
