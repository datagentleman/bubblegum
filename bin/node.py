import os
import traceback
import logging as log

from enum import Enum

from bubblegum.conn     import Conn
from bubblegum.node     import Node
from bubblegum.config   import Config 
from bubblegum.commands import * 

import lib.commands as c_commands

log.basicConfig(format="\x1b[6;37;44m%(levelname)s\x1b[0m:%(message)s", level=log.DEBUG)

HOST = Config["server.host"]
PORT = Config["server.port"]

class status():
    OK  = 1
    ERR = 2

def run_command(conn: Conn, node: Node):
  msg = conn.read()
  
  # Conn is consider closed when it's ready for read but there is no data. 
  # We can unregister it from select loop and return.
  if len(msg.data) == 0: 
    node.select.unregister(conn)
    return
  
  cmd = msg.read('str')
  
  res_ok  = lambda data=None: conn.send(status.OK.to_bytes(4, byteorder='little'))
  res_err = lambda data=None: conn.send(status.ERR.to_bytes(4, byteorder='little'))

  match cmd:
    case "TCREATE":
      tensor_name = msg.read('str')
      Tensor.create(tensor_name)
      res_ok()

    case _:
      conn.send(b"COMMAND DOESN'T EXIST")
      raise TypeError()


def handle_client(client_conn: Conn, cmd):
  cmd.run(client_conn)
  log.error('Client is dead ...')


if __name__ == '__main__':
  try:
    log.info(f'Starting bubblegum node on host: {HOST} port: {PORT} pid: {os.getpid()}')
    Node(HOST, PORT).run(run_command)
  except Exception as e:
    log.error(f'{traceback.format_exc()}')
